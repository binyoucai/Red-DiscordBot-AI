import discord
from redbot.core import commands, Config, checks
from redbot.core.bot import Red
from datetime import datetime, timedelta
import asyncio
from typing import Optional, List, Dict
import json
import logging

log = logging.getLogger("red.chatsummary")


class ChatSummary(commands.Cog):
    """聊天频道总结插件
    
    支持总结指定频道和全部频道，可配置定时任务自动总结。
    """
    
    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        
        # 默认配置
        default_guild = {
            "enabled": False,
            "api_key": None,
            "api_base": "https://api.openai.com/v1",
            "model": "gpt-3.5-turbo",
            "max_messages": 100,
            "summary_channel": None,
            "scheduled_tasks": {},  # {channel_id: {"interval": hours, "enabled": True}}
            "excluded_channels": [],
            "include_bots": False,
        }
        
        self.config.register_guild(**default_guild)
        
        # 定时任务字典
        self.scheduled_jobs = {}
        
        # 启动时加载定时任务
        self.bot.loop.create_task(self.load_scheduled_tasks())
    
    def cog_unload(self):
        """卸载时取消所有定时任务"""
        for task in self.scheduled_jobs.values():
            task.cancel()
    
    async def load_scheduled_tasks(self):
        """加载并启动所有已配置的定时任务"""
        await self.bot.wait_until_ready()
        
        for guild in self.bot.guilds:
            scheduled_tasks = await self.config.guild(guild).scheduled_tasks()
            
            for channel_id_str, task_config in scheduled_tasks.items():
                if task_config.get("enabled", False):
                    channel_id = int(channel_id_str)
                    interval = task_config.get("interval", 24)
                    self.start_scheduled_task(guild.id, channel_id, interval)
    
    def start_scheduled_task(self, guild_id: int, channel_id: int, interval_hours: int):
        """启动一个定时任务"""
        task_key = f"{guild_id}_{channel_id}"
        
        # 如果任务已存在，先取消
        if task_key in self.scheduled_jobs:
            self.scheduled_jobs[task_key].cancel()
        
        # 创建新任务
        task = self.bot.loop.create_task(
            self._scheduled_summary_loop(guild_id, channel_id, interval_hours)
        )
        self.scheduled_jobs[task_key] = task
    
    async def _scheduled_summary_loop(self, guild_id: int, channel_id: int, interval_hours: int):
        """定时任务循环"""
        while True:
            try:
                # 先等待指定时间
                await asyncio.sleep(interval_hours * 3600)
                
                guild = self.bot.get_guild(guild_id)
                if not guild:
                    continue
                
                channel = guild.get_channel(channel_id)
                if not channel:
                    continue
                
                # 执行总结
                await self._execute_summary(guild, channel)
                    
            except asyncio.CancelledError:
                break
            except Exception as e:
                log.error(f"定时任务执行错误 (Guild: {guild_id}, Channel: {channel_id}): {e}", exc_info=True)
    
    async def _execute_summary(self, guild: discord.Guild, channel: discord.TextChannel):
        """执行总结并发送结果"""
        try:
            # 生成总结
            summary = await self.generate_channel_summary(channel)
            
            # 发送到指定频道
            summary_channel_id = await self.config.guild(guild).summary_channel()
            if summary_channel_id:
                summary_channel = guild.get_channel(summary_channel_id)
                if summary_channel:
                    await summary_channel.send(embed=summary)
                    log.info(f"总结已发送到指定频道 {summary_channel.name} (Guild: {guild.name})")
                else:
                    log.warning(f"配置的总结频道不存在 (ID: {summary_channel_id}, Guild: {guild.name})")
                    await channel.send(embed=summary)
            else:
                # 发送到原频道
                await channel.send(embed=summary)
                log.info(f"总结已发送到原频道 {channel.name} (Guild: {guild.name})")
        except Exception as e:
            log.error(f"执行总结时出错 (Channel: {channel.name}, Guild: {guild.name}): {e}", exc_info=True)
    
    async def generate_channel_summary(self, channel: discord.TextChannel) -> discord.Embed:
        """生成频道总结"""
        guild = channel.guild
        max_messages = await self.config.guild(guild).max_messages()
        include_bots = await self.config.guild(guild).include_bots()
        
        # 获取消息
        messages = []
        async for message in channel.history(limit=max_messages):
            if not include_bots and message.author.bot:
                continue
            messages.append(message)
        
        messages.reverse()  # 按时间顺序排列
        
        if not messages:
            embed = discord.Embed(
                title=f"📊 频道总结 - {channel.name}",
                description="没有找到消息记录。",
                color=discord.Color.blue(),
                timestamp=datetime.utcnow()
            )
            return embed
        
        # 生成总结
        summary_text = await self.summarize_messages(guild, messages)
        
        # 创建统计信息
        user_count = len(set(m.author.id for m in messages))
        time_range = f"{messages[0].created_at.strftime('%Y-%m-%d %H:%M')} - {messages[-1].created_at.strftime('%Y-%m-%d %H:%M')}"
        
        embed = discord.Embed(
            title=f"📊 频道总结 - {channel.name}",
            description=summary_text,
            color=discord.Color.green(),
            timestamp=datetime.utcnow()
        )
        
        embed.add_field(name="📝 消息数量", value=str(len(messages)), inline=True)
        embed.add_field(name="👥 参与人数", value=str(user_count), inline=True)
        embed.add_field(name="⏰ 时间范围", value=time_range, inline=False)
        
        return embed
    
    async def summarize_messages(self, guild: discord.Guild, messages: List[discord.Message]) -> str:
        """使用 AI 总结消息"""
        api_key = await self.config.guild(guild).api_key()
        
        if not api_key:
            # 如果没有配置 API key，使用简单统计
            return self.simple_summary(messages)
        
        # 准备消息文本
        message_text = "\n".join([
            f"[{msg.created_at.strftime('%H:%M')}] {msg.author.name}: {msg.content[:200]}"
            for msg in messages
            if msg.content
        ])
        
        if not message_text:
            return "没有文本消息可以总结。"
        
        # 调用 AI API
        try:
            import aiohttp
            
            api_base = await self.config.guild(guild).api_base()
            model = await self.config.guild(guild).model()
            
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            prompt = f"""请总结以下Discord频道的聊天记录，用中文回答：

{message_text[:4000]}

请提供：
1. 主要讨论话题
2. 重要内容摘要
3. 关键结论或决定

保持简洁，不超过300字。"""
            
            data = {
                "model": model,
                "messages": [
                    {"role": "system", "content": "你是一个专业的聊天记录总结助手。"},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 500,
                "temperature": 0.7
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{api_base}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as resp:
                    if resp.status == 200:
                        result = await resp.json()
                        return result["choices"][0]["message"]["content"]
                    else:
                        return f"API 调用失败（状态码: {resp.status}），使用简单统计。\n\n" + self.simple_summary(messages)
        
        except Exception as e:
            return f"总结生成失败: {str(e)}\n\n使用简单统计:\n{self.simple_summary(messages)}"
    
    def simple_summary(self, messages: List[discord.Message]) -> str:
        """简单的统计总结（不使用 AI）"""
        if not messages:
            return "没有消息记录。"
        
        # 统计活跃用户
        user_msg_count = {}
        for msg in messages:
            user_msg_count[msg.author.name] = user_msg_count.get(msg.author.name, 0) + 1
        
        top_users = sorted(user_msg_count.items(), key=lambda x: x[1], reverse=True)[:5]
        
        summary = "**活跃用户统计：**\n"
        for i, (user, count) in enumerate(top_users, 1):
            summary += f"{i}. {user}: {count} 条消息\n"
        
        return summary
    
    @commands.group(name="summary", aliases=["总结"])
    @commands.guild_only()
    async def summary(self, ctx: commands.Context):
        """聊天总结命令组"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)
    
    @summary.command(name="channel", aliases=["频道"])
    async def summary_channel(self, ctx: commands.Context, channel: Optional[discord.TextChannel] = None):
        """总结指定频道的聊天记录
        
        参数:
            channel: 要总结的频道（不指定则总结当前频道）
        """
        if not await self.config.guild(ctx.guild).enabled():
            await ctx.send("❌ 聊天总结功能未启用。请管理员使用 `[p]summary enable` 启用。")
            return
        
        target_channel = channel or ctx.channel
        
        async with ctx.typing():
            summary_embed = await self.generate_channel_summary(target_channel)
            await ctx.send(embed=summary_embed)
    
    @summary.command(name="all", aliases=["全部", "全部频道"])
    @checks.admin_or_permissions(manage_guild=True)
    async def summary_all(self, ctx: commands.Context):
        """总结服务器中所有文字频道（需要管理员权限）"""
        if not await self.config.guild(ctx.guild).enabled():
            await ctx.send("❌ 聊天总结功能未启用。")
            return
        
        excluded_channels = await self.config.guild(ctx.guild).excluded_channels()
        
        await ctx.send("🔄 开始总结所有频道，这可能需要一些时间...")
        
        summaries = []
        for channel in ctx.guild.text_channels:
            if channel.id in excluded_channels:
                continue
            
            try:
                summary_embed = await self.generate_channel_summary(channel)
                summaries.append(summary_embed)
                log.info(f"成功总结频道 {channel.name} (Guild: {ctx.guild.name})")
            except Exception as e:
                log.error(f"总结频道 {channel.name} 时出错 (Guild: {ctx.guild.name}): {e}", exc_info=True)
        
        if not summaries:
            await ctx.send("❌ 没有可总结的频道。")
            return
        
        # 发送到指定频道或当前频道
        summary_channel_id = await self.config.guild(ctx.guild).summary_channel()
        target_channel = ctx.guild.get_channel(summary_channel_id) if summary_channel_id else ctx.channel
        
        await target_channel.send(f"## 📊 服务器全频道总结报告\n生成时间: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
        
        for embed in summaries:
            await target_channel.send(embed=embed)
            await asyncio.sleep(1)  # 避免速率限制
        
        await ctx.send(f"✅ 总结完成！共总结了 {len(summaries)} 个频道。")
    
    @summary.group(name="schedule", aliases=["定时", "任务"])
    @checks.admin_or_permissions(manage_guild=True)
    async def schedule(self, ctx: commands.Context):
        """定时任务管理"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)
    
    @schedule.command(name="add", aliases=["添加", "新增"])
    async def schedule_add(self, ctx: commands.Context, channel: discord.TextChannel, interval_hours: int, run_now: bool = False):
        """添加定时总结任务
        
        参数:
            channel: 要定时总结的频道
            interval_hours: 总结间隔（小时）
            run_now: 是否立即执行一次总结（默认为 False）
        """
        if interval_hours < 1:
            await ctx.send("❌ 间隔时间必须至少为 1 小时。")
            return
        
        async with self.config.guild(ctx.guild).scheduled_tasks() as tasks:
            tasks[str(channel.id)] = {
                "interval": interval_hours,
                "enabled": True,
                "channel_name": channel.name
            }
        
        # 启动定时任务
        self.start_scheduled_task(ctx.guild.id, channel.id, interval_hours)
        
        message = f"✅ 已添加定时任务：每 {interval_hours} 小时总结 {channel.mention}"
        
        # 如果指定立即执行
        if run_now:
            message += "\n🔄 正在立即执行第一次总结..."
            await ctx.send(message)
            async with ctx.typing():
                await self._execute_summary(ctx.guild, channel)
            await ctx.send(f"✅ 首次总结已完成！")
        else:
            await ctx.send(message)
    
    @schedule.command(name="remove", aliases=["删除", "移除"])
    async def schedule_remove(self, ctx: commands.Context, channel: discord.TextChannel):
        """移除定时总结任务
        
        参数:
            channel: 要移除任务的频道
        """
        async with self.config.guild(ctx.guild).scheduled_tasks() as tasks:
            if str(channel.id) in tasks:
                del tasks[str(channel.id)]
                
                # 取消任务
                task_key = f"{ctx.guild.id}_{channel.id}"
                if task_key in self.scheduled_jobs:
                    self.scheduled_jobs[task_key].cancel()
                    del self.scheduled_jobs[task_key]
                
                await ctx.send(f"✅ 已移除 {channel.mention} 的定时任务。")
            else:
                await ctx.send(f"❌ 频道 {channel.mention} 没有配置定时任务。")
    
    @schedule.command(name="list", aliases=["列表", "查看"])
    async def schedule_list(self, ctx: commands.Context):
        """查看所有定时任务"""
        tasks = await self.config.guild(ctx.guild).scheduled_tasks()
        
        if not tasks:
            await ctx.send("📋 当前没有配置任何定时任务。")
            return
        
        embed = discord.Embed(
            title="📋 定时总结任务列表",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        
        for channel_id_str, task_config in tasks.items():
            channel = ctx.guild.get_channel(int(channel_id_str))
            channel_name = channel.mention if channel else task_config.get("channel_name", "未知频道")
            interval = task_config.get("interval", "未知")
            enabled = "✅ 启用" if task_config.get("enabled", False) else "❌ 禁用"
            
            embed.add_field(
                name=f"{channel_name}",
                value=f"间隔: {interval} 小时\n状态: {enabled}",
                inline=True
            )
        
        await ctx.send(embed=embed)
    
    @schedule.command(name="run", aliases=["运行", "执行"])
    async def schedule_run(self, ctx: commands.Context, channel: discord.TextChannel):
        """手动立即执行指定频道的定时总结任务
        
        参数:
            channel: 要执行总结的频道
        """
        tasks = await self.config.guild(ctx.guild).scheduled_tasks()
        
        if str(channel.id) not in tasks:
            await ctx.send(f"❌ 频道 {channel.mention} 没有配置定时任务。")
            return
        
        await ctx.send(f"🔄 正在为 {channel.mention} 生成总结...")
        async with ctx.typing():
            await self._execute_summary(ctx.guild, channel)
        await ctx.send(f"✅ 总结已完成！")
    
    @summary.group(name="config", aliases=["配置", "设置"])
    @checks.admin_or_permissions(manage_guild=True)
    async def config_group(self, ctx: commands.Context):
        """配置管理"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)
    
    @config_group.command(name="enable", aliases=["启用"])
    async def config_enable(self, ctx: commands.Context):
        """启用聊天总结功能"""
        await self.config.guild(ctx.guild).enabled.set(True)
        await ctx.send("✅ 聊天总结功能已启用。")
    
    @config_group.command(name="disable", aliases=["禁用"])
    async def config_disable(self, ctx: commands.Context):
        """禁用聊天总结功能"""
        await self.config.guild(ctx.guild).enabled.set(False)
        await ctx.send("✅ 聊天总结功能已禁用。")
    
    @config_group.command(name="apikey", aliases=["api"])
    async def config_apikey(self, ctx: commands.Context, api_key: str):
        """设置 OpenAI API Key（私聊发送以保护密钥）
        
        参数:
            api_key: OpenAI API 密钥
        """
        await self.config.guild(ctx.guild).api_key.set(api_key)
        
        try:
            await ctx.message.delete()
        except:
            pass
        
        await ctx.author.send("✅ API Key 已设置成功！")
        await ctx.send("✅ API Key 已配置（已删除你的消息以保护密钥）。")
    
    @config_group.command(name="apibase", aliases=["base"])
    async def config_apibase(self, ctx: commands.Context, api_base: str):
        """设置 API Base URL
        
        参数:
            api_base: API 基础 URL（如：https://api.openai.com/v1）
        """
        await self.config.guild(ctx.guild).api_base.set(api_base)
        await ctx.send(f"✅ API Base URL 已设置为: {api_base}")
    
    @config_group.command(name="model", aliases=["模型"])
    async def config_model(self, ctx: commands.Context, model: str):
        """设置使用的 AI 模型
        
        参数:
            model: 模型名称（如：gpt-3.5-turbo, gpt-4）
        """
        await self.config.guild(ctx.guild).model.set(model)
        await ctx.send(f"✅ AI 模型已设置为: {model}")
    
    @config_group.command(name="maxmessages", aliases=["消息数量"])
    async def config_maxmessages(self, ctx: commands.Context, max_messages: int):
        """设置每次总结的最大消息数量
        
        参数:
            max_messages: 最大消息数量（10-1000）
        """
        if max_messages < 10 or max_messages > 1000:
            await ctx.send("❌ 消息数量必须在 10-1000 之间。")
            return
        
        await self.config.guild(ctx.guild).max_messages.set(max_messages)
        await ctx.send(f"✅ 最大消息数量已设置为: {max_messages}")
    
    @config_group.command(name="summarychannel", aliases=["总结频道"])
    async def config_summarychannel(self, ctx: commands.Context, channel: Optional[discord.TextChannel] = None):
        """设置总结结果发送的频道
        
        参数:
            channel: 目标频道（不指定则发送到原频道）
        """
        if channel:
            await self.config.guild(ctx.guild).summary_channel.set(channel.id)
            await ctx.send(f"✅ 总结结果将发送到: {channel.mention}")
        else:
            await self.config.guild(ctx.guild).summary_channel.set(None)
            await ctx.send("✅ 总结结果将发送到原频道。")
    
    @config_group.command(name="exclude", aliases=["排除"])
    async def config_exclude(self, ctx: commands.Context, channel: discord.TextChannel):
        """将频道添加到排除列表（不会被"全部总结"包含）
        
        参数:
            channel: 要排除的频道
        """
        async with self.config.guild(ctx.guild).excluded_channels() as excluded:
            if channel.id not in excluded:
                excluded.append(channel.id)
                await ctx.send(f"✅ 已将 {channel.mention} 添加到排除列表。")
            else:
                await ctx.send(f"❌ {channel.mention} 已在排除列表中。")
    
    @config_group.command(name="include", aliases=["包含"])
    async def config_include(self, ctx: commands.Context, channel: discord.TextChannel):
        """将频道从排除列表中移除
        
        参数:
            channel: 要包含的频道
        """
        async with self.config.guild(ctx.guild).excluded_channels() as excluded:
            if channel.id in excluded:
                excluded.remove(channel.id)
                await ctx.send(f"✅ 已将 {channel.mention} 从排除列表移除。")
            else:
                await ctx.send(f"❌ {channel.mention} 不在排除列表中。")
    
    @config_group.command(name="includebots", aliases=["包含机器人"])
    async def config_includebots(self, ctx: commands.Context, include: bool):
        """设置是否包含机器人消息
        
        参数:
            include: True 或 False
        """
        await self.config.guild(ctx.guild).include_bots.set(include)
        status = "包含" if include else "不包含"
        await ctx.send(f"✅ 总结将 {status} 机器人消息。")
    
    @config_group.command(name="show", aliases=["显示", "查看"])
    async def config_show(self, ctx: commands.Context):
        """显示当前配置"""
        config = await self.config.guild(ctx.guild).all()
        
        api_key_status = "✅ 已配置" if config["api_key"] else "❌ 未配置"
        enabled_status = "✅ 已启用" if config["enabled"] else "❌ 已禁用"
        
        summary_channel = ctx.guild.get_channel(config["summary_channel"]) if config["summary_channel"] else None
        summary_channel_text = summary_channel.mention if summary_channel else "原频道"
        
        excluded_channels = [
            ctx.guild.get_channel(ch_id).mention 
            for ch_id in config["excluded_channels"] 
            if ctx.guild.get_channel(ch_id)
        ]
        excluded_text = ", ".join(excluded_channels) if excluded_channels else "无"
        
        embed = discord.Embed(
            title="⚙️ 聊天总结配置",
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        
        embed.add_field(name="功能状态", value=enabled_status, inline=True)
        embed.add_field(name="API Key", value=api_key_status, inline=True)
        embed.add_field(name="AI 模型", value=config["model"], inline=True)
        embed.add_field(name="API Base", value=config["api_base"], inline=False)
        embed.add_field(name="最大消息数", value=str(config["max_messages"]), inline=True)
        embed.add_field(name="包含机器人", value="是" if config["include_bots"] else "否", inline=True)
        embed.add_field(name="总结发送频道", value=summary_channel_text, inline=True)
        embed.add_field(name="排除频道", value=excluded_text, inline=False)
        embed.add_field(name="定时任务数", value=str(len(config["scheduled_tasks"])), inline=True)
        
        await ctx.send(embed=embed)

