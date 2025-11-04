# ChatSummary - Discord 聊天总结插件

一个强大的 Red-DiscordBot 插件，用于智能总结 Discord 聊天频道的内容。支持使用 OpenAI API 生成高质量的聊天总结，也可以在没有 API 的情况下使用基础统计功能。

## ✨ 功能特性

- 📊 **指定频道总结**：总结任意指定的文字频道
- 🌐 **全服务器总结**：一键总结服务器中的所有频道
- ⏰ **定时任务**：配置自动定时总结任务
- 🤖 **AI 驱动**：集成 OpenAI API 生成智能总结
- 📈 **统计分析**：显示消息数量、参与人数、时间范围等
- ⚙️ **灵活配置**：丰富的配置选项，满足各种需求

## 📦 安装

### 方法一：通过 Red-DiscordBot 命令安装

```
[p]repo add red-ai https://github.com/yourusername/Red-DiscordBot-AI
[p]cog install red-ai chatsummary
[p]load chatsummary
```

### 方法二：手动安装

1. 将 `chatsummary` 文件夹复制到 Red-DiscordBot 的 `cogs` 目录
2. 使用命令加载插件：
```
[p]load chatsummary
```

## 🚀 快速开始

### 1. 启用插件

```
[p]summary config enable
```

### 2. 配置 OpenAI API（可选但推荐）

```
[p]summary config apikey YOUR_API_KEY
```

**注意**：为了保护你的 API Key，建议在私聊中使用此命令。

### 3. 开始使用

```
# 总结当前频道
[p]summary channel

# 总结指定频道
[p]summary channel #频道名称

# 总结所有频道（需要管理员权限）
[p]summary all
```

## 📖 详细命令说明

### 基础命令

#### `[p]summary channel [频道]`
总结指定频道的聊天记录。如果不指定频道，则总结当前频道。

**示例**：
```
[p]summary channel
[p]summary channel #general
```

#### `[p]summary all`
总结服务器中所有文字频道（需要管理员权限）。

**示例**：
```
[p]summary all
```

### 定时任务管理

#### `[p]summary schedule add <频道> <间隔小时数>`
为指定频道添加定时总结任务。

**示例**：
```
# 每24小时总结一次 #general 频道
[p]summary schedule add #general 24

# 每12小时总结一次 #chat 频道
[p]summary schedule add #chat 12
```

#### `[p]summary schedule remove <频道>`
移除指定频道的定时任务。

**示例**：
```
[p]summary schedule remove #general
```

#### `[p]summary schedule list`
查看所有已配置的定时任务。

**示例**：
```
[p]summary schedule list
```

### 配置管理

#### `[p]summary config enable`
启用聊天总结功能。

#### `[p]summary config disable`
禁用聊天总结功能。

#### `[p]summary config apikey <API_KEY>`
设置 OpenAI API Key。建议在私聊中使用此命令以保护密钥。

**示例**：
```
[p]summary config apikey sk-xxxxxxxxxxxxxxxxxxxxx
```

#### `[p]summary config apibase <URL>`
设置 API Base URL（如果使用第三方 API 服务）。

**示例**：
```
# 使用官方 API
[p]summary config apibase https://api.openai.com/v1

# 使用代理或第三方服务
[p]summary config apibase https://your-proxy.com/v1
```

#### `[p]summary config model <模型名称>`
设置使用的 AI 模型。

**示例**：
```
[p]summary config model gpt-3.5-turbo
[p]summary config model gpt-4
```

#### `[p]summary config maxmessages <数量>`
设置每次总结的最大消息数量（10-1000）。

**示例**：
```
[p]summary config maxmessages 200
```

#### `[p]summary config summarychannel [频道]`
设置总结结果发送的目标频道。如果不指定频道，则发送到原频道。

**示例**：
```
# 设置发送到指定频道
[p]summary config summarychannel #summaries

# 恢复发送到原频道
[p]summary config summarychannel
```

#### `[p]summary config exclude <频道>`
将频道添加到排除列表（不会被"全部总结"包含）。

**示例**：
```
[p]summary config exclude #admin
```

#### `[p]summary config include <频道>`
将频道从排除列表中移除。

**示例**：
```
[p]summary config include #admin
```

#### `[p]summary config includebots <true/false>`
设置是否在总结中包含机器人消息。

**示例**：
```
[p]summary config includebots false
```

#### `[p]summary config show`
显示当前所有配置。

**示例**：
```
[p]summary config show
```

## 🔧 高级配置

### 使用第三方 API 服务

如果你使用的是兼容 OpenAI API 的第三方服务（如 Azure OpenAI、国内代理等），可以通过配置 API Base URL 来使用：

```
[p]summary config apibase https://your-service.com/v1
[p]summary config apikey YOUR_API_KEY
```

### 不使用 AI 功能

如果你没有 OpenAI API Key，插件仍然可以工作，但会使用基础的统计功能而不是 AI 生成的总结。基础功能包括：
- 消息数量统计
- 活跃用户排名
- 时间范围显示

## 📊 总结示例

生成的总结包含以下信息：

```
📊 频道总结 - general

[AI 生成的总结内容]

主要讨论话题：
- 话题1
- 话题2

重要内容摘要：
...

📝 消息数量: 150
👥 参与人数: 12
⏰ 时间范围: 2025-11-03 10:00 - 2025-11-04 08:00
```

## ⚙️ 权限要求

- **普通用户**：可以使用 `summary channel` 命令总结频道
- **管理员**：需要 `管理服务器` 权限才能：
  - 使用 `summary all` 总结所有频道
  - 配置定时任务
  - 修改插件设置

## 🤝 常见问题

### Q: 如何获取 OpenAI API Key？

A: 访问 [OpenAI 官网](https://platform.openai.com/) 注册账号并创建 API Key。

### Q: 总结生成失败怎么办？

A: 检查以下几点：
1. API Key 是否正确配置
2. API Base URL 是否正确
3. 账户是否有足够的余额
4. 网络连接是否正常

如果 API 调用失败，插件会自动回退到基础统计模式。

### Q: 定时任务会自动保存吗？

A: 是的，所有配置（包括定时任务）都会自动保存，即使机器人重启也会恢复。

### Q: 可以同时运行多个定时任务吗？

A: 可以！你可以为不同的频道配置不同的定时任务，它们会独立运行。

### Q: 总结会包含图片和附件吗？

A: 当前版本主要总结文字消息。未来版本可能会支持图片描述和附件统计。

## 📝 更新日志

### v1.0.0 (2025-11-04)
- ✨ 初始版本发布
- 📊 支持指定频道和全服务器总结
- ⏰ 支持定时任务配置
- 🤖 集成 OpenAI API
- ⚙️ 丰富的配置选项

## 💡 技术支持

如有问题或建议，请：
1. 提交 Issue 到 GitHub 仓库
2. 联系开发者

## 📄 许可证

MIT License

## 🙏 致谢

感谢 Red-DiscordBot 团队提供的优秀框架！

