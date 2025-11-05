# Red-DiscordBot-AI 插件集合

一个为 Red-DiscordBot 开发的 AI 增强插件集合，为你的 Discord 服务器带来智能功能。

## 📦 包含的插件

### ChatSummary - 智能聊天总结插件

强大的聊天频道总结工具，支持使用 AI 生成高质量的对话摘要。

**主要功能：**
- 📊 总结指定频道或全部频道，按分类分组显示
- ⏰ 支持单频道和全服务器定时任务
- 📁 智能分类管理，可排除整个分类
- 🤖 集成 OpenAI API 进行智能分析
- 📈 详细的统计信息和数据可视化
- ⚙️ 灵活的配置选项

**[查看详细文档 →](chatsummary/README.md)**

**[快速安装指南 →](chatsummary/INSTALL.md)**

## 🚀 快速开始

### 安装 ChatSummary

```bash
# 方法一：通过仓库安装
[p]repo add red-ai https://github.com/yourusername/Red-DiscordBot-AI
[p]cog install red-ai chatsummary
[p]load chatsummary

# 方法二：手动安装
# 将 chatsummary 文件夹复制到 Red-DiscordBot 的 cogs 目录
[p]load chatsummary
```

### 基础配置

```bash
# 启用插件
[p]summary config enable

# 配置 API Key（可选）
[p]summary config apikey YOUR_API_KEY

# 开始使用
[p]summary channel
```

## 📖 使用示例

### 总结频道

```bash
# 总结当前频道
[p]summary channel

# 总结指定频道
[p]summary channel #general
```

### 配置定时任务

```bash
# 单频道定时任务
# 每24小时自动总结 #general 频道
[p]summary schedule add #general 24

# 立即执行一次并开始定时任务
[p]summary schedule add #chat 12 true

# 全服务器定时任务
# 每24小时自动总结所有频道
[p]summary schedule addall 24

# 查看所有定时任务
[p]summary schedule list

# 手动运行定时任务
[p]summary schedule run #general
[p]summary schedule runall
```

### 总结频道

```bash
# 总结指定频道
[p]summary channel #general

# 总结特定分类
[p]summary category 公告区

# 总结所有频道（按分类分组显示）
[p]summary all

# 排除特定分类
[p]summary config excludecategory 管理区
[p]summary config excludecategory 归档
```

## 🛠️ 系统要求

- Red-DiscordBot v3.5.0 或更高版本
- Python 3.8+
- aiohttp 3.8.0+
- discord.py 2.0.0+

## 📋 功能对比

| 功能 | ChatSummary | 未来插件... |
|------|-------------|-------------|
| 频道总结 | ✅ | - |
| AI 分析 | ✅ | - |
| 定时任务 | ✅ | - |
| 统计分析 | ✅ | - |
| 多语言 | ✅ 中文 | - |

## 🔮 未来计划

- [ ] 情感分析插件
- [ ] 内容审核插件
- [ ] 智能问答插件
- [ ] 图片描述生成插件
- [ ] 语音转文字插件

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 开发指南

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot) - 优秀的 Discord 机器人框架
- [discord.py](https://github.com/Rapptz/discord.py) - Discord API 的 Python 封装
- OpenAI - 提供强大的 AI API

## 💬 支持

- 📖 [文档](chatsummary/README.md)
- 🐛 [报告 Bug](https://github.com/yourusername/Red-DiscordBot-AI/issues)
- 💡 [功能建议](https://github.com/yourusername/Red-DiscordBot-AI/issues)

## 📊 项目状态

![Development Status](https://img.shields.io/badge/status-active-success.svg)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Red-DiscordBot](https://img.shields.io/badge/Red--DiscordBot-3.5.0+-red.svg)

---

**注意**：使用此插件需要遵守 Discord 的服务条款和 OpenAI 的使用政策。请确保你的使用符合相关规定。

Made with ❤️ for the Discord community

