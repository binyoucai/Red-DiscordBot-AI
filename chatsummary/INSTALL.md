# ChatSummary 安装指南

## 🚀 快速安装

### 前置要求

1. 已安装并配置好 **Red-DiscordBot** (v3.5.0+)
2. Python 3.8 或更高版本
3. （可选）OpenAI API Key 或兼容的 API 服务

### 安装步骤

#### 方法一：通过 Red-DiscordBot 命令安装（推荐）

如果你的插件已上传到 Git 仓库：

```bash
# 添加仓库
[p]repo add red-ai https://github.com/yourusername/Red-DiscordBot-AI

# 安装插件
[p]cog install red-ai chatsummary

# 加载插件
[p]load chatsummary
```

#### 方法二：手动安装

1. **定位 Red-DiscordBot 的 cogs 目录**

```bash
# 在 Red-DiscordBot 所在目录运行
[p]datapath

# 输出示例：/home/user/.local/share/Red-DiscordBot/data/instance_name
```

cogs 目录通常在：`[datapath]/cogs/`

2. **复制插件文件**

```bash
# 将整个 chatsummary 文件夹复制到 cogs 目录
cp -r chatsummary /path/to/redbot/data/instance_name/cogs/
```

或使用 Git：

```bash
cd /path/to/redbot/data/instance_name/cogs/
git clone https://github.com/yourusername/Red-DiscordBot-AI.git
cp -r Red-DiscordBot-AI/chatsummary ./
```

3. **安装依赖**

```bash
# 激活 Red-DiscordBot 的虚拟环境（如果使用）
source /path/to/redbot/venv/bin/activate

# 安装依赖
pip install aiohttp>=3.8.0
```

4. **加载插件**

在 Discord 中运行：

```
[p]load chatsummary
```

### 验证安装

运行以下命令检查插件是否成功加载：

```
[p]cog list

# 应该能看到 ChatSummary 在列表中
```

或直接查看帮助：

```
[p]help summary
```

## ⚙️ 初始配置

### 1. 启用插件

```
[p]summary config enable
```

### 2. 配置 OpenAI API（推荐但可选）

**⚠️ 重要：为了安全，请在与机器人的私聊中发送此命令！**

```
[p]summary config apikey sk-your-api-key-here
```

如果你不配置 API Key，插件仍然可以工作，但会使用基础统计功能而不是 AI 总结。

### 3. （可选）高级配置

```bash
# 设置自定义 API Base（如使用代理或 Azure）
[p]summary config apibase https://your-api-endpoint.com/v1

# 设置 AI 模型
[p]summary config model gpt-4

# 设置最大消息数量
[p]summary config maxmessages 200

# 设置总结结果发送频道
[p]summary config summarychannel #bot-summaries

# 不包含机器人消息
[p]summary config includebots false
```

### 4. 查看当前配置

```
[p]summary config show
```

## 🎯 快速测试

配置完成后，在任意文字频道运行：

```
[p]summary channel
```

如果一切正常，机器人将生成并发送该频道的聊天总结。

## 🔧 常见问题排查

### 插件加载失败

```bash
# 检查错误日志
[p]traceback

# 重新加载插件
[p]reload chatsummary
```

### 依赖缺失

如果出现 `ModuleNotFoundError: No module named 'aiohttp'` 错误：

```bash
# 确保在正确的 Python 环境中
pip install aiohttp>=3.8.0

# 或使用 Red-DiscordBot 的 pip
[p]pipinstall aiohttp>=3.8.0
```

### API 调用失败

1. 检查 API Key 是否正确
2. 检查网络连接
3. 检查 API 余额
4. 尝试使用不同的 API Base

```bash
# 重新设置 API Key
[p]summary config apikey NEW_API_KEY

# 如果使用代理，确保 Base URL 正确
[p]summary config apibase https://api.openai.com/v1
```

### 权限问题

确保机器人有以下权限：
- 读取消息历史
- 发送消息
- 嵌入链接（发送 Embed）
- 读取频道列表

## 📚 下一步

- 查看 [README.md](README.md) 了解详细功能说明
- 查看 [example_config.md](example_config.md) 了解配置示例
- 配置定时任务自动总结

## 💡 使用建议

1. **小规模测试**：先在一个低活跃度的频道测试
2. **逐步配置**：先手动总结，确认效果后再配置定时任务
3. **监控使用**：如果使用付费 API，注意监控调用次数和成本
4. **专用频道**：创建一个专门的频道接收总结结果

## 🆘 获取帮助

如遇到问题：
1. 查看 Red-DiscordBot 日志
2. 使用 `[p]traceback` 查看详细错误
3. 在 GitHub 提交 Issue
4. 加入 Red-DiscordBot 社区寻求帮助

---

安装完成！享受智能聊天总结功能吧！ 🎉

