# ChatSummary 快速开始指南

## 🎯 5分钟快速上手

### 第一步：加载插件

```
[p]load chatsummary
```

### 第二步：启用功能

```
[p]summary config enable
```

### 第三步：开始使用

```
[p]summary channel
```

就这么简单！插件会立即生成当前频道的聊天总结。

## 💡 实用场景示例

### 场景 1：每日早会总结

**需求**：每天早上 9 点自动总结昨天的讨论内容

**设置**：
```bash
# 1. 创建一个专门的总结频道
创建频道: #daily-summaries

# 2. 配置总结发送位置
[p]summary config summarychannel #daily-summaries

# 3. 添加每24小时运行的定时任务
[p]summary schedule add #general 24

# 4. 如果想立即看效果
[p]summary schedule run #general
```

### 场景 2：活跃频道实时总结

**需求**：高活跃度聊天频道每6小时自动总结

**设置**：
```bash
# 为活跃频道设置短间隔
[p]summary schedule add #chat 6
[p]summary schedule add #discussion 6

# 增加消息采样数量
[p]summary config maxmessages 200
```

### 场景 3：项目协作总结

**需求**：总结项目相关频道，排除闲聊频道

**设置**：
```bash
# 配置要总结的项目频道
[p]summary schedule add #project-alpha 12
[p]summary schedule add #project-beta 12

# 排除不需要总结的频道
[p]summary config exclude #off-topic
[p]summary config exclude #random
[p]summary config exclude #memes

# 不包含机器人消息（只看人类讨论）
[p]summary config includebots false
```

### 场景 4：周报生成

**需求**：每周五下午生成本周所有频道的总结

**设置**：
```bash
# 每168小时（7天）运行一次
[p]summary schedule add #general 168
[p]summary schedule add #announcements 168
[p]summary schedule add #discussion 168

# 或者手动触发周报
[p]summary all
```

### 场景 5：使用第三方 API 服务

**需求**：使用国内 API 代理或 Azure OpenAI

**设置**：
```bash
# 使用国内代理示例
[p]summary config apibase https://api.chatanywhere.com.cn/v1
[p]summary config apikey sk-xxxxxxxxxxxxxxxxxxxxx
[p]summary config model gpt-3.5-turbo

# 或使用 Azure OpenAI
[p]summary config apibase https://your-resource.openai.azure.com/openai/deployments/your-deployment
[p]summary config apikey your-azure-api-key
[p]summary config model gpt-35-turbo
```

## 🎨 常用命令速查

### 日常使用

| 命令 | 说明 | 示例 |
|------|------|------|
| `[p]summary channel` | 总结当前频道 | `[p]summary channel` |
| `[p]summary channel #频道名` | 总结指定频道 | `[p]summary channel #general` |
| `[p]summary all` | 总结所有频道 | `[p]summary all` |

### 定时任务管理

| 命令 | 说明 | 示例 |
|------|------|------|
| `[p]summary schedule add` | 添加定时任务 | `[p]summary schedule add #chat 24` |
| `[p]summary schedule add ... true` | 添加并立即运行 | `[p]summary schedule add #chat 24 true` |
| `[p]summary schedule remove` | 删除定时任务 | `[p]summary schedule remove #chat` |
| `[p]summary schedule list` | 查看所有任务 | `[p]summary schedule list` |
| `[p]summary schedule run` | 手动运行任务 | `[p]summary schedule run #chat` |

### 配置命令

| 命令 | 说明 | 示例 |
|------|------|------|
| `[p]summary config enable` | 启用功能 | - |
| `[p]summary config disable` | 禁用功能 | - |
| `[p]summary config apikey` | 设置 API Key | `[p]summary config apikey sk-xxx` |
| `[p]summary config model` | 设置模型 | `[p]summary config model gpt-4` |
| `[p]summary config maxmessages` | 设置消息数 | `[p]summary config maxmessages 200` |
| `[p]summary config show` | 查看配置 | - |

## 💰 成本估算（使用 OpenAI API）

### GPT-3.5-Turbo 价格参考

- 每次总结约消耗：1000-2000 tokens
- 价格：约 $0.001-0.002 per 总结
- 每天总结4次：约 $0.004-0.008/天
- 每月成本：约 $0.12-0.24/频道

### 节省成本的建议

1. **使用合适的间隔**：不需要太频繁的总结
2. **限制消息数量**：`maxmessages 100` 通常够用
3. **排除低价值频道**：使用 `config exclude`
4. **使用国内代理**：有些服务价格更便宜
5. **混合使用**：重要频道用 AI，其他用基础统计

## 🔍 故障排查流程

### 问题：总结没有生成

**排查步骤**：
```bash
# 1. 检查是否启用
[p]summary config show

# 2. 查看配置状态
功能状态应该是 "✅ 已启用"

# 3. 尝试手动总结测试
[p]summary channel

# 4. 检查机器人权限
确保机器人有"读取消息历史"和"发送消息"权限
```

### 问题：API 调用失败

**排查步骤**：
```bash
# 1. 检查 API Key
[p]summary config show
# API Key 状态应该是 "✅ 已配置"

# 2. 测试 API 连接
在私聊中重新设置 API Key
[p]summary config apikey YOUR_KEY

# 3. 检查 API Base
[p]summary config apibase https://api.openai.com/v1

# 4. 如果仍然失败，插件会自动使用基础统计模式
```

### 问题：定时任务没有运行

**排查步骤**：
```bash
# 1. 检查任务列表
[p]summary schedule list

# 2. 确认任务状态为"启用"
# 状态应该显示 "✅ 启用"

# 3. 手动测试任务
[p]summary schedule run #频道名

# 4. 如果机器人重启，任务会自动恢复
```

## 📝 最佳实践清单

- [ ] ✅ 在私聊中配置 API Key
- [ ] 📊 先在测试频道试用
- [ ] ⏰ 根据频道活跃度设置合适的间隔
- [ ] 📁 创建专门的总结频道
- [ ] 🚫 排除私密和管理员频道
- [ ] 💾 定期查看配置状态
- [ ] 📉 监控 API 使用量和成本
- [ ] 🔄 及时更新插件版本

## 🆘 获取更多帮助

- 📖 [完整文档](README.md)
- 🔧 [安装指南](INSTALL.md)
- ⚙️ [配置示例](example_config.md)
- 💬 [GitHub Issues](https://github.com/yourusername/Red-DiscordBot-AI/issues)

## 🎓 进阶技巧

### 技巧 1：自定义总结时间

虽然插件不直接支持定时触发（如每天特定时间），但你可以：
- 使用系统 cron 或 Windows 任务计划器
- 配合 Red-DiscordBot 的其他调度插件

### 技巧 2：多服务器配置

每个 Discord 服务器的配置是独立的：
```bash
# 在服务器 A
[p]summary config model gpt-3.5-turbo

# 在服务器 B
[p]summary config model gpt-4
```

### 技巧 3：批量配置

为多个频道设置相同的定时任务：
```bash
[p]summary schedule add #channel1 24
[p]summary schedule add #channel2 24
[p]summary schedule add #channel3 24
```

### 技巧 4：测试不同模型

```bash
# 测试 GPT-3.5
[p]summary config model gpt-3.5-turbo
[p]summary channel #test

# 测试 GPT-4（更好但更贵）
[p]summary config model gpt-4
[p]summary channel #test
```

---

现在你已经准备好充分利用 ChatSummary 了！🎉

有问题？查看[完整文档](README.md)或[提交 Issue](https://github.com/yourusername/Red-DiscordBot-AI/issues)。

