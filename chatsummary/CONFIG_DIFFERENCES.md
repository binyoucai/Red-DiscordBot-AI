# 总结和导出配置的区别说明

从版本 2.0 开始，聊天总结和聊天记录导出功能的配置已经完全分离，您可以为每个功能设置不同的参数。

## 配置对比

| 配置项 | 总结功能 | 导出功能 |
|--------|---------|---------|
| **发送频道** | `[p]config summarychannel` | `[p]config exportchannel` |
| **最大消息数** | `[p]config maxmessages` (默认: 100) | `[p]config exportmaxmessages` (默认: 1000) |
| **排除频道** | `[p]config exclude` / `[p]config include` | `[p]config exportexclude` / `[p]config exportinclude` |
| **排除分类** | `[p]config excludecategory` / `[p]config includecategory` | `[p]config exportexcludecategory` / `[p]config exportincludecategory` |

## 为什么要分离？

### 1. 发送频道分离
- **场景**：总结文本适合发送到通知频道，而大量的 Excel 文件更适合存档频道
- **优势**：避免文件和文本消息混在一起，更好地组织内容

```bash
# 总结发送到机器人日志频道
[p]config summarychannel #bot-logs

# Excel文件发送到文件存档频道
[p]config exportchannel #file-archives
```

### 2. 最大消息数分离
- **场景**：AI 总结通常只需要最近 100-200 条消息来生成摘要，但导出聊天记录可能需要完整的历史记录
- **优势**：总结功能快速响应，导出功能提供完整数据

```bash
# 总结只处理最近100条消息（快速生成）
[p]config maxmessages 100

# 导出获取最近1000条消息（详细记录）
[p]config exportmaxmessages 1000

# 或者导出不限制数量（获取全部历史）
[p]config exportmaxmessages 0
```

### 3. 排除列表分离
- **场景**：某些频道不需要 AI 总结（如机器人命令频道），但可能需要导出完整记录
- **优势**：灵活控制每个功能的作用范围

```bash
# 排除机器人命令频道的总结（避免无意义的总结）
[p]config exclude #bot-commands

# 但仍然允许导出该频道的记录（用于审计）
# （不添加到导出排除列表即可）
```

```bash
# 排除管理员分类的总结（保护隐私）
[p]config excludecategory 管理区

# 也排除管理员分类的导出（双重保护）
[p]config exportexcludecategory 管理区
```

## 使用场景示例

### 场景 1：公开服务器
```bash
# 总结配置：只关注主要讨论频道
[p]config summarychannel #summaries
[p]config maxmessages 150
[p]config exclude #bot-commands
[p]config exclude #spam

# 导出配置：记录所有公开频道
[p]config exportchannel #archives
[p]config exportmaxmessages 0  # 不限制
# （不排除任何频道，完整记录）
```

### 场景 2：私密管理
```bash
# 总结配置：只总结工作频道
[p]config summarychannel #team-logs
[p]config maxmessages 100
[p]config excludecategory 管理区
[p]config excludecategory 私密讨论

# 导出配置：同样保护隐私
[p]config exportchannel #secure-archives
[p]config exportmaxmessages 500
[p]config exportexcludecategory 管理区
[p]config exportexcludecategory 私密讨论
```

### 场景 3：审计需求
```bash
# 总结配置：面向用户的日常总结
[p]config summarychannel #public-summaries
[p]config maxmessages 100
[p]config exclude #admin

# 导出配置：面向管理员的完整审计
[p]config exportchannel #admin-audit
[p]config exportmaxmessages 0  # 获取完整历史
# （不排除任何频道，包括 #admin）
```

## 配置查看

使用以下命令查看当前所有配置：

```bash
[p]config show
```

配置信息将显示：
- ✅ 总结最大消息数 vs 导出最大消息数
- ✅ 总结发送频道 vs 导出发送频道
- ✅ 总结排除频道/分类 vs 导出排除频道/分类
- ✅ 总结定时任务数 vs 导出定时任务数

## 快速配置模板

### 模板 1：默认配置（总结和导出使用相同设置）
```bash
[p]config enable
[p]config apikey sk-xxxxx
[p]config summarychannel #bot-logs
[p]config maxmessages 100
[p]config exportmaxmessages 1000
[p]config exclude #spam
```

### 模板 2：分离配置（总结和导出完全独立）
```bash
# 通用配置
[p]config enable
[p]config apikey sk-xxxxx

# 总结专用配置
[p]config summarychannel #summaries
[p]config maxmessages 100
[p]config exclude #bot-commands
[p]config excludecategory 归档

# 导出专用配置
[p]config exportchannel #archives
[p]config exportmaxmessages 0
[p]config exportexclude #spam
# （导出不排除归档分类，保留完整历史）
```

## 注意事项

1. **默认行为**：如果未设置导出专用配置，系统会使用以下默认值：
   - `export_channel`：使用 `summary_channel` 或当前频道
   - `export_max_messages`：1000 条
   - `export_excluded_channels/categories`：空列表（不排除任何频道）

2. **独立性**：总结的排除列表和导出的排除列表完全独立，互不影响

3. **兼容性**：旧版本配置会自动迁移，无需手动调整

4. **建议**：根据实际需求选择是否分离配置，没有必要时使用相同设置即可

## 常见问题

**Q：我需要分离配置吗？**  
A：不一定。如果您的总结和导出需求相同，使用默认设置即可。只有在有特殊需求时才需要分离。

**Q：我已经配置了总结的排除列表，导出会受影响吗？**  
A：不会。导出有独立的排除列表，默认为空（不排除任何频道）。

**Q：如何让导出也使用总结的排除列表？**  
A：手动将相同的频道/分类添加到导出排除列表：
```bash
[p]config exclude #admin
[p]config exportexclude #admin
```

**Q：可以只设置导出排除列表，不设置总结排除列表吗？**  
A：可以。两个列表完全独立，可以任意组合。

