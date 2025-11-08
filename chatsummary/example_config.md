# ChatSummary 配置示例

## 基础配置示例

```bash
# 1. 启用插件
[p]summary config enable

# 2. 配置 OpenAI API（在私聊中执行）
[p]summary config apikey sk-xxxxxxxxxxxxxxxxxxxxx

# 3. 设置模型（可选，默认为 gpt-3.5-turbo）
[p]summary config model gpt-3.5-turbo

# 4. 设置每次总结的最大消息数（可选，默认为 100）
[p]summary config maxmessages 150
```

## 使用国内 API 代理示例

```bash
# 配置 API Base URL
[p]summary config apibase https://api.chatanywhere.com.cn/v1

# 配置 API Key
[p]summary config apikey sk-xxxxxxxxxxxxxxxxxxxxx

# 设置模型
[p]summary config model gpt-3.5-turbo
```

## 使用 Azure OpenAI 示例

```bash
# 配置 Azure API Base
[p]summary config apibase https://your-resource.openai.azure.com/openai/deployments/your-deployment

# 配置 API Key
[p]summary config apikey your-azure-api-key

# 设置模型
[p]summary config model gpt-35-turbo
```

## 定时任务配置示例

### 场景 1：每日总结主要频道

```bash
# 每天总结 #general 频道（24小时）
[p]summary schedule add #general 24

# 每天总结 #announcements 频道
[p]summary schedule add #announcements 24

# 查看所有定时任务
[p]summary schedule list
```

### 场景 2：高频总结活跃频道

```bash
# 每6小时总结活跃聊天频道
[p]summary schedule add #chat 6

# 每12小时总结讨论频道
[p]summary schedule add #discussion 12
```

### 场景 3：设置总结结果发送频道

```bash
# 创建或使用一个专门的总结频道
[p]summary config summarychannel #daily-summaries

# 现在所有总结都会发送到 #daily-summaries 频道
```

## 高级配置示例

### 排除特定频道

```bash
# 排除单个频道
[p]summary config exclude #admin
[p]summary config exclude #mod-chat

# 排除私密频道
[p]summary config exclude #staff-only

# 查看当前配置
[p]summary config show
```

### 排除整个分类

```bash
# 排除整个管理员分类（比逐个排除频道更高效）
[p]summary config excludecategory 管理区

# 排除语音频道文字区
[p]summary config excludecategory 语音频道

# 排除归档分类
[p]summary config excludecategory 归档

# 排除未分类的频道
[p]summary config excludecategory 未分类

# 查看当前配置
[p]summary config show
```

### 配置消息过滤

```bash
# 不包含机器人消息
[p]summary config includebots false

# 设置较少的消息数量（适合低活跃度频道）
[p]summary config maxmessages 50
```

## 完整配置流程示例

```bash
# ===== 步骤 1: 基础配置 =====
[p]summary config enable
[p]summary config apikey sk-xxxxxxxxxxxxxxxxxxxxx
[p]summary config model gpt-3.5-turbo

# ===== 步骤 2: 设置总结发送频道 =====
[p]summary config summarychannel #bot-summaries

# 可选：设置Excel导出文件发送频道（如果不设置，则使用总结频道）
[p]summary config exportchannel #file-exports

# 可选：设置导出功能的最大消息数
[p]summary config exportmaxmessages 1000

# ===== 步骤 3: 配置定时任务 =====
# 选项 A: 单频道定时任务
# 主要频道每天总结一次
[p]summary schedule add #general 24
[p]summary schedule add #chat 24

# 重要频道每12小时总结一次
[p]summary schedule add #important 12

# 选项 B: 全服务器定时任务（每天总结所有频道）
[p]summary schedule addall 24

# ===== 步骤 4: 排除不需要总结的频道/分类 =====
# 排除单个频道（仅总结功能）
[p]summary config exclude #admin
[p]summary config exclude #bot-commands

# 或排除整个分类（仅总结功能，更高效）
[p]summary config excludecategory 管理区
[p]summary config excludecategory 归档

# 可选：单独配置导出功能的排除列表
[p]summary config exportexclude #admin
[p]summary config exportexcludecategory 管理区

# ===== 步骤 5: 其他设置 =====
[p]summary config maxmessages 200
[p]summary config includebots false

# ===== 步骤 6: 查看配置 =====
[p]summary config show
[p]summary schedule list
```

## 测试配置

配置完成后，建议进行测试：

```bash
# 测试单个频道总结
[p]summary channel #general

# 如果正常工作，可以测试全服务器总结（慎用，可能较慢）
[p]summary all
```

## 日常使用命令

```bash
# 手动总结当前频道
[p]summary channel

# 手动总结指定频道
[p]summary channel #channel-name

# 查看定时任务状态
[p]summary schedule list

# 查看当前配置
[p]summary config show
```

## 故障排除

如果总结失败，按以下步骤检查：

```bash
# 1. 检查配置
[p]summary config show

# 2. 检查是否启用
[p]summary config enable

# 3. 如果使用 API，确认 API Key 是否正确
[p]summary config apikey YOUR_NEW_KEY

# 4. 尝试更换 API Base（如果使用代理）
[p]summary config apibase https://api.openai.com/v1

# 5. 降低消息数量重试
[p]summary config maxmessages 50
```

## 新功能使用示例

### 全服务器自动总结（自动生成PDF）

```bash
# 每天自动总结所有频道（会自动生成并发送PDF报告）
[p]summary schedule addall 24

# 配置总结发送频道
[p]summary config summarychannel #daily-reports

# 排除不需要的分类
[p]summary config excludecategory 管理区
[p]summary config excludecategory 归档

# 立即测试一次（也会生成PDF）
[p]summary schedule runall
```

### 按分类管理总结范围

```bash
# 大型服务器有很多分类，只想总结部分分类
# 方法：排除不需要的分类

# 排除语音相关分类
[p]summary config excludecategory 语音频道
[p]summary config excludecategory 音乐机器人

# 排除归档和临时分类
[p]summary config excludecategory 归档
[p]summary config excludecategory 临时频道

# 排除管理分类
[p]summary config excludecategory 管理区
[p]summary config excludecategory 审核区

# 查看配置
[p]summary config show

# 现在只会总结未被排除的分类
[p]summary all
```

### 周报/月报自动生成（含PDF）

```bash
# 每周自动生成周报（168小时 = 7天，自动生成PDF）
[p]summary schedule addall 168

# 配置专门的周报频道
[p]summary config summarychannel #weekly-reports

# 或者每月生成月报（720小时 = 30天，自动生成PDF）
[p]summary schedule addall 720

# 注意：定时任务会自动生成PDF报告并发送到配置的频道
```

### 只总结特定分类

```bash
# 只想看公告相关的内容
[p]summary category 公告区

# 或者只看聊天区的讨论
[p]summary category 聊天区

# 定期生成某个分类的报告
# 可以配合定时任务（暂不支持分类定时任务，但可以手动运行）
[p]summary category 项目讨论区
```

## 最佳实践

1. **API Key 安全**：始终在私聊中配置 API Key
2. **定时任务设置**：避免设置过短的间隔（建议至少6小时）
3. **使用分类排除**：优先使用 `excludecategory` 而不是逐个排除频道
4. **总结频道**：创建专门的频道接收所有总结
5. **消息数量**：根据频道活跃度调整，活跃频道可以增加到 200-500
6. **成本控制**：如果使用付费 API，注意控制调用频率
7. **全服务器任务**：大型服务器使用全服务器定时任务更方便
8. **PDF生成**：定时任务会自动生成PDF报告，确保服务器有足够的存储空间和中文字体支持

## Excel 导出使用示例

### 导出单个频道的完整聊天记录

```bash
# 导出当前频道的聊天记录
[p]summary export channel

# 导出指定频道
[p]summary export channel #general

# 导出最近1000条消息
[p]summary export channel #general 1000
```

### 批量导出聊天记录

```bash
# 导出所有频道到单个Excel文件（推荐，默认模式）
[p]summary export all

# 导出指定分类到单个Excel文件
[p]summary export category 公告区

# 导出所有频道到单个Excel文件，每个频道最多500条消息
[p]summary export all 500

# 导出所有频道，每个频道一个独立的Excel文件（多文件模式）
[p]summary export all 0 False

# 导出指定分类，每个频道一个独立的Excel文件
[p]summary export category 聊天区 0 False
```

### Excel 表格特性

**单文件导出模式**（推荐）：
- 所有频道合并到一个Excel文件
- 第一个工作表：汇总统计信息
  - 服务器名称、报告标题
  - 总频道数、总消息数
  - 每个频道的详细统计表格
- 后续工作表：每个频道一个Sheet
  - 包含14列详细聊天记录
  - 自动调整列宽
  - 冻结首行便于浏览

**单频道导出**：
导出的Excel文件包含两个工作表：

1. **聊天记录工作表**：
   - 包含14列详细信息
   - 自动调整列宽以适应内容
   - 冻结首行便于浏览
   - 消息按时间顺序排列

2. **统计信息工作表**：
   - 频道基本信息
   - 消息统计数据
   - 用户参与情况
   - 生成时间等

### 常见使用场景

```bash
# 场景1: 导出重要公告频道作为备份
[p]summary export channel #announcements

# 场景2: 导出某个项目讨论分类的完整记录（单文件）
[p]summary export category 项目讨论

# 场景3: 月度归档 - 导出所有频道到单个Excel文件
[p]summary export all

# 场景4: 导出活跃频道的最近聊天
[p]summary export channel #chat 1000

# 场景5: 按分类整理归档（每个分类一个Excel文件）
[p]summary export category 公告区
[p]summary export category 聊天区
[p]summary export category 技术讨论

# 场景6: 需要分发给不同人员（多文件模式）
[p]summary export category 项目A 0 False
```

## Excel 导出定时任务使用示例

### 设置自动备份

```bash
# 每天自动导出所有频道到单个Excel文件
[p]summary export schedule addall 24

# 配置导出文件发送频道
[p]summary config summarychannel #backups

# 立即测试一次
[p]summary export schedule run export_all
```

### 分类定时导出

```bash
# 每周导出"公告区"分类
[p]summary export schedule addcategory 公告区 168

# 每天导出"项目讨论"分类，每个频道最多1000条消息
[p]summary export schedule addcategory 项目讨论 24 True 1000

# 每月导出"归档"分类
[p]summary export schedule addcategory 归档 720
```

### 频道定时导出

```bash
# 每12小时导出支持频道
[p]summary export schedule addchannel #support 12

# 每天导出重要频道
[p]summary export schedule addchannel #important 24 500
```

### 查看和管理任务

```bash
# 查看所有导出定时任务
[p]summary export schedule list

# 移除不需要的任务
[p]summary export schedule remove export_cat_归档

# 手动执行指定任务
[p]summary export schedule run export_all
```

### 企业级备份方案

```bash
# 每周完整备份（单文件模式，便于归档）
[p]summary export schedule addall 168

# 每天增量备份重要分类
[p]summary export schedule addcategory 重要文档 24
[p]summary export schedule addcategory 项目讨论 24

# 每小时备份实时支持频道
[p]summary export schedule addchannel #support 1 500

# 配置备份文件接收频道
[p]summary config summarychannel #server-backups
```

## 推荐配置模板

### 小型服务器（< 100人）
```bash
[p]summary config maxmessages 100
[p]summary schedule add #general 24
[p]summary schedule add #chat 24
```

### 中型服务器（100-1000人）
```bash
[p]summary config maxmessages 150
[p]summary schedule add #general 12
[p]summary schedule add #chat 12
[p]summary schedule add #discussion 24
```

### 大型服务器（> 1000人）
```bash
[p]summary config maxmessages 200
[p]summary schedule add #general 6
[p]summary schedule add #chat 6
[p]summary schedule add #discussion 12
[p]summary schedule add #announcements 24
```

