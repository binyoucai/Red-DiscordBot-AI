from .chatsummary import ChatSummary


async def setup(bot):
    """加载ChatSummary cog"""
    await bot.add_cog(ChatSummary(bot))

