# ChatSummary - Discord 聊天总结插件

一个强大的 Red-DiscordBot 插件，用于智能总结 Discord 聊天频道的内容。支持使用 OpenAI API 生成高质量的聊天总结，也可以在没有 API 的情况下使用基础统计功能。

## ✨ 功能特性

- 📊 **指定频道总结**：总结任意指定的文字频道
- 🌐 **全服务器总结**：一键总结服务器中的所有频道，按分类分组显示
- ⏰ **定时任务**：支持单频道和全服务器定时总结任务
- 📁 **分类管理**：按频道分类组织总结，支持排除整个分类
- 🤖 **AI 驱动**：集成 OpenAI API 生成智能总结
- 📈 **统计分析**：显示消息数量、参与人数、时间范围等
- 📄 **PDF报告**：自动生成PDF格式的总结报告，方便保存和分享
- 📊 **Excel导出**：将频道聊天记录导出为详细的Excel表格，包含消息ID、时间、用户、内容、附件、反应等完整信息
- ⚙️ **灵活配置**：丰富的配置选项，满足各种需求
- 🔧 **排除控制**：可排除特定频道或整个分类

## 📦 安装

### 方法一：通过 Red-DiscordBot 命令安装

```
[p]repo add red-ai https://github.com/binyoucai/Red-DiscordBot-AI
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

#### `[p]summary all [生成PDF]`
总结服务器中所有文字频道（需要管理员权限）。默认会自动生成PDF报告。

**示例**：
```
# 总结所有频道并生成PDF（默认）
[p]summary all

# 总结所有频道但不生成PDF
[p]summary all false
```

#### `[p]summary category <分类名称> [生成PDF]`
总结指定分类下的所有频道（需要管理员权限）。默认会自动生成PDF报告。

**示例**：
```
# 总结"公告区"分类下的所有频道并生成PDF（默认）
[p]summary category 公告区

# 总结"聊天区"分类并生成PDF
[p]summary category 聊天区

# 总结未分类的频道但不生成PDF
[p]summary category 未分类 false
```

**PDF报告特性**：
- 📄 自动生成专业的PDF格式报告
- 🌍 支持中文内容（自动检测系统中文字体）
- 📊 包含完整的总结内容和统计信息
- 💾 自动上传到Discord供下载
- 🗑️ 发送后自动清理临时文件

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

#### `[p]summary schedule addall <间隔小时数> [立即运行]`
添加定时总结全部频道任务。定时任务会自动生成 PDF 报告并发送。

**示例**：
```
# 每24小时自动总结所有频道（自动生成PDF）
[p]summary schedule addall 24

# 添加并立即执行第一次
[p]summary schedule addall 24 true
```

#### `[p]summary schedule removeall`
移除全服务器定时总结任务。

**示例**：
```
[p]summary schedule removeall
```

#### `[p]summary schedule run <频道>`
手动立即执行指定频道的定时总结任务。

**示例**：
```
[p]summary schedule run #general
```

#### `[p]summary schedule runall`
手动立即执行全服务器定时总结任务。

**示例**：
```
[p]summary schedule runall
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

#### `[p]summary config exportmaxmessages <数量>`
设置Excel导出的最大消息数量（0表示不限制）。

**示例**：
```
# 设置导出最大1000条消息
[p]summary config exportmaxmessages 1000

# 设置为不限制
[p]summary config exportmaxmessages 0
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

#### `[p]summary config exportchannel [频道]`
设置Excel导出文件发送的目标频道。如果不指定频道，则使用总结频道或当前频道。

**示例**：
```
# 设置导出文件发送到指定频道
[p]summary config exportchannel #file-exports

# 恢复使用总结频道或当前频道
[p]summary config exportchannel
```

#### `[p]summary config exclude <频道>`
将频道添加到总结排除列表（不会被"全部总结"包含）。

**示例**：
```
[p]summary config exclude #admin
```

#### `[p]summary config include <频道>`
将频道从总结排除列表中移除。

**示例**：
```
[p]summary config include #admin
```

#### `[p]summary config exportexclude <频道>`
将频道添加到导出排除列表（不会被"全部导出"包含）。

**示例**：
```
[p]summary config exportexclude #admin
```

#### `[p]summary config exportinclude <频道>`
将频道从导出排除列表中移除。

**示例**：
```
[p]summary config exportinclude #admin
```

#### `[p]summary config excludecategory <分类名称>`
将整个分类添加到总结排除列表（该分类下的所有频道都不会被总结）。

**示例**：
```
# 排除管理员分类
[p]summary config excludecategory 管理区

# 排除语音频道文字区
[p]summary config excludecategory 语音频道

# 排除未分类的频道
[p]summary config excludecategory 未分类
```

#### `[p]summary config includecategory <分类名称>`
将分类从总结排除列表中移除。

**示例**：
```
[p]summary config includecategory 管理区
```

#### `[p]summary config exportexcludecategory <分类名称>`
将整个分类添加到导出排除列表（该分类下的所有频道都不会被导出）。

**示例**：
```
# 排除管理员分类
[p]summary config exportexcludecategory 管理区

# 排除未分类的频道
[p]summary config exportexcludecategory 未分类
```

#### `[p]summary config exportincludecategory <分类名称>`
将分类从导出排除列表中移除。

**示例**：
```
[p]summary config exportincludecategory 管理区
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

### Excel 导出命令

#### `[p]summary export channel [频道] [最大消息数]`
导出指定频道的聊天记录到Excel表格。

**参数**：
- `channel`: 要导出的频道（不指定则导出当前频道）
- `max_messages`: 最大消息数量（0表示使用配置的默认值）

**示例**：
```
# 导出当前频道的聊天记录
[p]summary export channel

# 导出指定频道的聊天记录
[p]summary export channel #general

# 导出最近500条消息
[p]summary export channel #general 500
```

**Excel表格包含的信息**：
- 📋 聊天记录工作表（14列数据）：
  - 消息ID
  - 时间
  - 用户名、用户ID、用户昵称
  - 消息内容
  - **Embed内容**（嵌入消息：标题、描述、链接、图片、视频等）
  - 附件链接
  - 回复消息ID
  - 反应（表情和数量）
  - 是否编辑、编辑时间
  - 是否置顶
  - 提及的用户
- 📊 统计信息工作表：
  - 频道名称
  - 消息总数
  - 参与用户数
  - 时间范围
  - 附件消息数
  - **Embed消息数**
  - 编辑消息数
  - 置顶消息数
  - 回复消息数

**文件命名格式**：`频道分类-频道名称.xlsx`

#### `[p]summary export all [最大消息数] [单文件模式]`
导出所有频道的聊天记录到Excel（需要管理员权限）。

**参数**：
- `max_messages`：每个频道的最大消息数量（0=使用默认值）
- `single_file`：是否合并到单个Excel文件（True=单文件，False=多文件，默认为True）

**示例**：
```
# 导出所有频道到单个Excel文件（默认）
[p]summary export all

# 导出所有频道到单个Excel文件，每个频道最多1000条消息
[p]summary export all 1000

# 导出所有频道，每个频道一个独立的Excel文件
[p]summary export all 0 False
```

**单文件模式说明**：
- 所有频道的聊天记录合并到一个Excel文件
- 每个频道是一个独立的工作表（Sheet）
- 第一个工作表是汇总统计信息
- 文件命名：`服务器名称_全服务器聊天记录.xlsx`

#### `[p]summary export category <分类名称> [最大消息数] [单文件模式]`
导出指定分类下所有频道的聊天记录到Excel（需要管理员权限）。

**参数**：
- `category_name`：分类名称（使用"未分类"导出没有分类的频道）
- `max_messages`：每个频道的最大消息数量（0=使用默认值）
- `single_file`：是否合并到单个Excel文件（True=单文件，False=多文件，默认为True）

**示例**：
```
# 导出"公告区"分类到单个Excel文件（默认）
[p]summary export category 公告区

# 导出"聊天区"分类到单个Excel文件，每个频道最多500条消息
[p]summary export category 聊天区 500

# 导出未分类的频道，每个频道一个独立的Excel文件
[p]summary export category 未分类 0 False
```

**单文件模式说明**：
- 该分类下所有频道的聊天记录合并到一个Excel文件
- 每个频道是一个独立的工作表（Sheet）
- 第一个工作表是汇总统计信息
- 文件命名：`分类名称_聊天记录.xlsx`

### Excel 导出定时任务

#### `[p]summary export schedule addall <间隔小时数> [单文件模式] [最大消息数] [立即运行]`
添加定时导出所有频道的任务。

**参数**：
- `interval_hours`: 导出间隔（小时）
- `single_file`: 是否合并到单个文件（True/False，默认True）
- `max_messages`: 每个频道的最大消息数量（0=使用默认值）
- `run_now`: 是否立即执行一次（True/False，默认False）

**示例**：
```
# 每24小时自动导出所有频道到单个Excel文件
[p]summary export schedule addall 24

# 每周导出（168小时），立即执行第一次
[p]summary export schedule addall 168 True 0 True

# 每天导出，每个频道一个文件
[p]summary export schedule addall 24 False
```

#### `[p]summary export schedule addcategory <分类名称> <间隔小时数> [单文件模式] [最大消息数] [立即运行]`
添加定时导出指定分类的任务。

**示例**：
```
# 每24小时导出"公告区"分类
[p]summary export schedule addcategory 公告区 24

# 每周导出"项目讨论"分类，每个频道最多1000条消息
[p]summary export schedule addcategory 项目讨论 168 True 1000
```

#### `[p]summary export schedule addchannel <频道> <间隔小时数> [最大消息数] [立即运行]`
添加定时导出指定频道的任务。

**示例**：
```
# 每12小时导出#general频道
[p]summary export schedule addchannel #general 12

# 每天导出#announcements，最多500条消息
[p]summary export schedule addchannel #announcements 24 500
```

#### `[p]summary export schedule list`
查看所有导出定时任务。

**示例**：
```
[p]summary export schedule list
```

#### `[p]summary export schedule remove <任务ID>`
移除导出定时任务。

**示例**：
```
# 先查看任务列表获取任务ID
[p]summary export schedule list

# 移除指定任务
[p]summary export schedule remove export_all
```

#### `[p]summary export schedule run <任务ID>`
手动立即执行指定的导出任务。

**示例**：
```
[p]summary export schedule run export_all
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

## 📚 配置分离说明

从 v2.1 开始，总结功能和导出功能的配置已经完全分离，您可以为它们设置不同的参数。

### 配置项对比

| 功能 | 发送频道 | 最大消息数 | 排除频道 | 排除分类 |
|------|---------|-----------|---------|---------|
| **总结** | `summarychannel` | `maxmessages` (100) | `exclude` / `include` | `excludecategory` / `includecategory` |
| **导出** | `exportchannel` | `exportmaxmessages` (1000) | `exportexclude` / `exportinclude` | `exportexcludecategory` / `exportincludecategory` |

### 为什么分离？

1. **不同的使用场景**：
   - 总结：快速生成摘要，通常只需要最近的消息
   - 导出：完整的数据记录，可能需要全部历史

2. **不同的发送目标**：
   - 总结文本适合发送到通知频道
   - Excel 文件更适合存档到专门的文件频道

3. **灵活的控制**：
   - 可以排除某些频道的总结，但仍然导出它们的记录
   - 或者只总结重要频道，但导出所有频道

### 详细说明

请参阅 [`CONFIG_DIFFERENCES.md`](CONFIG_DIFFERENCES.md) 获取完整的配置分离说明、使用场景和最佳实践。

## ⚙️ 权限要求

- **普通用户**：可以使用 `summary channel` 和 `export channel` 命令
- **管理员**：需要 `管理服务器` 权限才能：
  - 使用 `summary all` 和 `export all` 等批量命令
  - 配置定时任务
  - 修改插件设置

## 🤝 常见问题

### Q: 总结和导出的配置有什么区别？

A: 从 v2.1 开始，总结和导出功能的配置完全独立：
- **发送频道**：总结消息和 Excel 文件可以发送到不同的频道
- **最大消息数**：总结通常只需要最近的消息（默认100），导出可以获取更多历史记录（默认1000）
- **排除列表**：可以分别控制哪些频道参与总结或导出

详细说明请查看 `CONFIG_DIFFERENCES.md` 文档。

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

A: 当前版本主要总结文字消息。Excel导出功能会记录附件的URL链接。未来版本可能会支持图片描述和附件统计。

### Q: Excel导出需要安装额外的库吗？

A: 是的，需要安装 `openpyxl` 库。插件的 requirements.txt 中已经包含了这个依赖，使用 `[p]cog install` 时会自动安装。

### Q: Excel文件的大小有限制吗？

A: Excel 单个单元格最多支持 32,767 个字符。对于超长消息，会自动截断。建议合理设置 max_messages 参数来控制导出的消息数量。

## 📝 更新日志

### v1.1.0 (2025-11-08)
- ✨ 新增 Excel 导出功能
- 📊 支持导出单个频道、所有频道、指定分类的聊天记录
- 📋 Excel 包含详细的聊天信息（14列数据）和统计信息
- 🎨 支持导出 Embed（嵌入消息）内容，包括标题、描述、链接、图片、视频等
- 📁 支持单文件模式：将多个频道合并到一个Excel文件，每个频道一个工作表
- 📊 汇总统计工作表：提供所有频道的完整统计信息
- ⏰ **Excel 导出定时任务**：支持定时自动导出所有频道、指定分类、指定频道
- 🔧 定时任务现在自动生成 PDF 报告

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

