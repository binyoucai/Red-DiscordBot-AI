# Excel 导出功能使用指南

## 📊 功能概述

Excel 导出功能允许你将 Discord 频道的聊天记录导出为详细的 Excel 表格文件。每个 Excel 文件包含完整的聊天信息和统计数据，方便进行数据分析、归档保存或离线查看。

## ✨ 主要特性

- **详细的聊天记录**：包含消息ID、时间、用户信息、内容、附件、反应等13列数据
- **统计信息**：自动生成消息统计、用户参与情况等汇总信息
- **灵活的导出选项**：支持单个频道、所有频道、指定分类的批量导出
- **标准化命名**：文件名格式为 `频道分类-频道名称.xlsx`
- **优化的表格格式**：自动调整列宽、冻结首行、美化样式

## 📋 Excel 表格内容

### 工作表1：聊天记录

包含以下14列信息：

| 列名 | 说明 | 示例 |
|------|------|------|
| 消息ID | Discord消息的唯一标识符 | 1234567890123456789 |
| 时间 | 消息发送时间 | 2025-11-08 10:30:15 |
| 用户名 | 发送者的Discord用户名 | User#1234 |
| 用户ID | 发送者的Discord用户ID | 987654321098765432 |
| 用户昵称 | 发送者在服务器内的昵称 | 小明 |
| 消息内容 | 消息的文字内容 | 大家好！今天天气不错 |
| **Embed内容** | **嵌入消息的完整信息** | **标题: XXX \| 描述: XXX \| 链接: XXX** |
| 附件 | 附件的URL链接（多个用逗号分隔） | https://cdn.discord... |
| 回复消息ID | 如果是回复，显示被回复消息的ID | 1234567890123456788 |
| 反应 | 消息的表情反应及数量 | 👍(5), ❤️(3) |
| 是否编辑 | 消息是否被编辑过 | 是/否 |
| 编辑时间 | 最后编辑时间 | 2025-11-08 10:35:20 |
| 是否置顶 | 消息是否被置顶 | 是/否 |
| 提及用户 | 消息中@的用户列表 | @User1, @User2 |

#### Embed内容详解

Embed（嵌入消息）是Discord中的富文本格式内容，包括：

- **标题**：Embed的标题
- **描述**：Embed的主要内容
- **链接**：相关的URL链接
- **作者**：Embed作者信息
- **字段**：自定义字段（名称: 值）
- **页脚**：底部的页脚文本
- **图片**：嵌入的图片URL
- **缩略图**：缩略图URL
- **视频**：视频URL

**示例**：
```
标题: Discord更新公告 | 描述: 我们发布了新功能... | 链接: https://discord.com | 图片: https://cdn.discord.com/...
```

多个Embed之间使用 `---` 分隔。

**表格特性**：
- 首行冻结，方便滚动浏览
- 蓝色标题行，清晰易读
- 自动调整列宽
- 消息按时间正序排列（最早的在最上面）

### 工作表2：统计信息

包含以下统计数据：

| 统计项目 | 说明 |
|----------|------|
| 频道名称 | 完整的频道路径（分类/频道名） |
| 消息总数 | 导出的消息总条数 |
| 参与用户数 | 发言的唯一用户数量 |
| 时间范围 | 从最早到最晚消息的时间跨度 |
| 包含附件的消息 | 带有附件的消息数量 |
| 包含Embed的消息 | 包含嵌入内容的消息数量 |
| 编辑过的消息 | 被编辑过的消息数量 |
| 置顶消息 | 被置顶的消息数量 |
| 回复消息 | 回复其他消息的数量 |
| 生成时间 | Excel文件生成时间 |

## 🚀 使用方法

### 基础命令

#### 1. 导出单个频道

```bash
# 导出当前频道
[p]summary export channel

# 导出指定频道
[p]summary export channel #general

# 导出指定频道的最近500条消息
[p]summary export channel #general 500
```

**参数说明**：
- `channel`（可选）：要导出的频道，不指定则导出当前频道
- `max_messages`（可选）：最大消息数量，0表示使用配置的默认值

**文件发送位置**：
- 如果配置了导出频道（`[p]summary config exportchannel`），文件将发送到导出频道
- 否则，如果配置了总结频道（`[p]summary config summarychannel`），文件将发送到总结频道
- 否则，文件将发送到当前频道

#### 2. 导出所有频道（需要管理员权限）

```bash
# 导出所有频道到单个Excel文件（默认模式，推荐）
[p]summary export all

# 导出所有频道到单个Excel文件，每个频道最多1000条消息
[p]summary export all 1000

# 导出所有频道，每个频道一个独立的Excel文件（多文件模式）
[p]summary export all 0 False
```

**单文件模式（默认）**：
- 所有频道的聊天记录合并到一个Excel文件
- 每个频道是一个独立的工作表（Sheet）
- 第一个工作表是汇总统计信息，包含：
  - 服务器名称
  - 报告标题和生成时间
  - 总频道数和总消息数
  - 每个频道的详细统计表格
- 文件命名格式：`服务器名称_全服务器聊天记录_时间戳.xlsx`
- **优点**：文件管理方便、可快速切换查看不同频道、包含完整统计

**多文件模式**：
- 每个频道生成一个独立的Excel文件
- 适合需要单独分发各频道数据的场景

**注意事项**：
- 需要服务器管理权限
- 会自动排除已配置的排除频道和分类
- 按分类分组依次处理
- 单文件模式可能生成较大的Excel文件，请注意Discord文件大小限制

#### 3. 导出指定分类（需要管理员权限）

```bash
# 导出"公告区"分类到单个Excel文件（默认模式，推荐）
[p]summary export category 公告区

# 导出"聊天区"分类到单个Excel文件，每个频道最多500条消息
[p]summary export category 聊天区 500

# 导出未分类的频道，每个频道一个独立的Excel文件（多文件模式）
[p]summary export category 未分类 0 False
```

**单文件模式（默认）**：
- 该分类下所有频道的聊天记录合并到一个Excel文件
- 每个频道是一个独立的工作表（Sheet）
- 第一个工作表是汇总统计信息
- 文件命名格式：`服务器名称_分类名称_聊天记录_时间戳.xlsx`
- **优点**：整合分类数据、便于分类归档

## ⏰ 定时任务导出

### 添加定时导出任务

#### 1. 定时导出所有频道

```bash
# 每24小时自动导出所有频道到单个Excel文件
[p]summary export schedule addall 24

# 每周导出（168小时 = 7天），立即执行第一次
[p]summary export schedule addall 168 True 0 True

# 每天导出，每个频道一个独立文件
[p]summary export schedule addall 24 False

# 每天导出，每个频道最多1000条消息
[p]summary export schedule addall 24 True 1000
```

**参数说明**：
- `interval_hours`: 导出间隔（小时）
- `single_file`: 是否合并到单个文件（True/False，默认True）
- `max_messages`: 每个频道的最大消息数量（0=使用默认值）
- `run_now`: 是否立即执行一次（True/False，默认False）

#### 2. 定时导出指定分类

```bash
# 每24小时导出"公告区"分类
[p]summary export schedule addcategory 公告区 24

# 每周导出"项目讨论"分类
[p]summary export schedule addcategory 项目讨论 168

# 每天导出"聊天区"，每个频道最多500条消息，立即执行第一次
[p]summary export schedule addcategory 聊天区 24 True 500 True
```

#### 3. 定时导出指定频道

```bash
# 每12小时导出#general频道
[p]summary export schedule addchannel #general 12

# 每天导出#announcements，最多500条消息
[p]summary export schedule addchannel #announcements 24 500

# 每6小时导出#support，立即执行第一次
[p]summary export schedule addchannel #support 6 0 True
```

### 管理定时任务

#### 查看所有任务

```bash
[p]summary export schedule list
```

这将显示所有已配置的导出定时任务，包括：
- 任务ID
- 任务类型（所有频道/分类/频道）
- 导出间隔
- 文件模式（单文件/多文件）
- 消息数量限制
- 任务状态（启用/禁用）

#### 移除任务

```bash
# 先查看任务列表获取任务ID
[p]summary export schedule list

# 移除指定任务
[p]summary export schedule remove export_all
[p]summary export schedule remove export_cat_公告区
[p]summary export schedule remove export_ch_123456789
```

#### 手动执行任务

```bash
# 立即执行指定任务（不影响定时计划）
[p]summary export schedule run export_all
```

### 任务ID说明

定时任务的ID格式：
- 所有频道：`export_all`
- 指定分类：`export_cat_分类名称`
- 指定频道：`export_ch_频道ID`

## 💡 使用场景

### 场景1：数据备份

定期导出重要频道的聊天记录作为备份：

```bash
# 每月导出公告频道
[p]summary export channel #announcements

# 每周导出项目讨论
[p]summary export category 项目讨论
```

### 场景2：数据分析

导出聊天记录进行数据分析：

```bash
# 导出活跃频道进行用户参与分析
[p]summary export channel #general 5000

# 导出所有频道进行全服务器分析
[p]summary export all
```

### 场景3：归档管理

按月或按季度归档聊天记录：

```bash
# 月末导出所有频道
[p]summary export all

# 按分类归档
[p]summary export category 2024年项目
```

### 场景4：合规审计

为合规或审计需求导出完整记录：

```bash
# 导出指定时间段的消息（配合max_messages参数）
[p]summary export channel #compliance 10000
```

## ⚙️ 配置建议

### 消息数量设置

根据需求调整每次导出的消息数量：

```bash
# 小型频道：100-500条
[p]summary export channel #小频道 100

# 中型频道：500-1000条
[p]summary export channel #中频道 500

# 大型频道：1000-5000条
[p]summary export channel #大频道 1000

# 完整导出：设置为0使用配置的默认值或不限制
[p]summary export channel #频道 0
```

### 排除频道设置

在导出所有频道之前，建议先配置排除列表：

```bash
# 排除私密频道
[p]summary config exclude #admin
[p]summary config exclude #mod-chat

# 排除整个管理分类
[p]summary config excludecategory 管理区

# 然后执行批量导出
[p]summary export all
```

## 📊 Excel 文件处理建议

### 数据筛选和排序

导出的Excel文件可以直接使用Excel的强大功能：

1. **按用户筛选**：使用"用户名"列的筛选功能查看特定用户的消息
2. **按时间排序**：使用"时间"列排序查看时间线
3. **搜索关键词**：使用Ctrl+F搜索消息内容
4. **数据透视表**：创建透视表分析用户活跃度、消息分布等

### 数据导入其他工具

Excel文件可以轻松导入到：

- **数据分析工具**：Python pandas、R、Tableau等
- **数据库**：MySQL、PostgreSQL、MongoDB等
- **统计软件**：SPSS、SAS等
- **可视化工具**：Power BI、Grafana等

## ⚠️ 注意事项

### 文件大小限制

- Excel单个单元格最多支持32,767个字符
- 超长消息会自动截断
- 建议合理控制导出的消息数量

### 性能考虑

- 导出大量频道时会需要较长时间
- 建议在低峰期进行批量导出
- 每个频道导出后会自动等待2秒，避免Discord API限制

### 隐私和安全

- Excel文件包含完整的聊天记录，请妥善保管
- 不要将包含敏感信息的Excel文件分享给未授权人员
- 定期清理不需要的导出文件

### Discord文件大小限制

- 免费服务器：最大文件大小8MB
- Nitro服务器：最大文件大小50-100MB
- 如果Excel文件过大，可能无法通过Discord发送
- 建议：控制max_messages参数，或分多次导出

## 🔧 故障排除

### 问题1：Excel文件生成失败

**解决方法**：
```bash
# 确认已安装openpyxl库
pip install openpyxl

# 或重新安装插件
[p]cog uninstall chatsummary
[p]cog install red-ai chatsummary
```

### 问题2：文件无法发送（过大）

**解决方法**：
```bash
# 减少导出的消息数量
[p]summary export channel #频道 500

# 或分批导出不同的时间段
```

### 问题3：某些中文字符显示异常

**解决方法**：
- 确保使用最新版本的Excel或WPS打开
- 或使用Google Sheets导入查看

### 问题4：导出速度很慢

**解决方法**：
- 大量频道导出需要时间，请耐心等待
- 可以先导出单个频道测试
- 避免在高峰期执行批量导出

## 📚 相关命令

- `[p]summary config show` - 查看当前配置
- `[p]summary config exclude` - 排除频道
- `[p]summary config excludecategory` - 排除分类
- `[p]summary config maxmessages` - 设置默认消息数量

## 💬 反馈与支持

如果你在使用Excel导出功能时遇到问题或有改进建议，请：

1. 查看日志：`[p]logs`
2. 提交Issue到GitHub仓库
3. 联系插件开发者

---

**版本**：v1.1.0  
**更新日期**：2025-11-08

