# PDF 报告功能指南

## 📄 功能概述

ChatSummary 插件现在支持自动生成 PDF 格式的总结报告！在使用 `summary all` 或 `summary category` 命令时，会自动生成并上传 PDF 文件到 Discord。

## 🎯 支持的命令

### 1. 全服务器总结 + PDF

```bash
# 默认生成PDF
[p]summary all

# 不生成PDF
[p]summary all false
```

### 2. 分类总结 + PDF

```bash
# 默认生成PDF
[p]summary category 公告区

# 不生成PDF
[p]summary category 聊天区 false
```

## 📊 PDF报告内容

生成的 PDF 报告包含：

1. **报告标题**
   - 服务器名称
   - 报告类型（全服务器/特定分类）

2. **生成信息**
   - 生成时间（UTC）
   - 服务器信息

3. **每个频道的总结**
   - 分类名称 / 频道名称
   - AI 生成的总结内容（支持Markdown格式渲染）
   - 统计信息：
     - 消息数量
     - 参与人数
     - 时间范围

4. **格式特点**
   - 每个频道独立一页
   - 清晰的层次结构
   - 专业的排版
   - **PDF大纲/书签**：每个频道自动生成书签，方便快速导航
   - **自动渲染Markdown格式**：
     - 标题（#、##、###）
     - 列表（-、*）
     - 粗体（**文本**）
     - 段落换行

## 📑 PDF大纲/书签功能

**新功能！** PDF报告现在自动包含可导航的大纲书签：

### 功能特点

- 📑 **自动书签**：每个频道总结自动生成书签
- 🔖 **快速导航**：在PDF阅读器左侧面板显示大纲
- 📍 **精准定位**：点击书签直接跳转到对应频道
- 🎯 **层次清晰**：按"分类 / 频道名"格式显示

### 使用方法

在支持书签的PDF阅读器中打开生成的PDF文件：

**Adobe Acrobat Reader**:
- 点击左侧的"书签"图标（📑）
- 查看所有频道列表
- 点击任意书签快速跳转

**macOS 预览**:
- 点击"显示"菜单 → "目录"
- 或使用快捷键 `⌘⌥3`
- 在侧边栏查看书签列表

**浏览器**:
- Chrome/Edge: 点击PDF工具栏的"大纲"按钮
- 在侧边栏查看书签

### 书签示例

```
📊 服务器名 - Summary Report
  ├─ 公告栏 / announcements
  ├─ 公告栏 / updates  
  ├─ 讨论区 / general
  ├─ 讨论区 / tech-talk
  └─ 未分类 / random
```

## 📝 Markdown格式支持

**新功能！** PDF报告现在支持自动渲染AI返回的Markdown格式内容：

### 支持的格式

| Markdown语法 | 效果 | 示例 |
|-------------|------|------|
| `# 标题` | 一级标题 | 大号粗体标题 |
| `## 标题` | 二级标题 | 中号粗体标题 |
| `### 标题` | 三级标题 | 小号粗体标题 |
| `- 列表项` | 无序列表 | • 列表项 |
| `* 列表项` | 无序列表 | • 列表项 |
| `**粗体**` | 粗体文本 | **粗体** |

### 渲染效果

**原始AI返回**：
```
# 会议总结

## 概要
本次会议主要讨论了AI选股平台的开发进度。

## 重点
- AI选股平台完成了初步开发
- 扫描了2025年热门股票
- 发现了3只股价>=10美元的股票

**下一步计划**：继续优化算法
```

**PDF中显示**：
- "会议总结" 显示为大号粗体标题
- "概要" 显示为中号粗体标题
- "重点" 显示为中号粗体标题
- 三个要点显示为项目符号列表
- "下一步计划" 显示为粗体

## 🌍 中文支持

PDF 生成器会自动检测并使用系统中文字体：

- **macOS**: PingFang
- **Linux**: AR PL UMing
- **Windows**: 微软雅黑

如果未找到中文字体，将使用英文字体（仍可显示内容）。

## 📦 依赖要求

确保安装了以下依赖：

```bash
pip install reportlab>=4.0.0
pip install Pillow>=9.0.0
```

或者使用插件的 requirements.txt：

```bash
pip install -r requirements.txt
```

## 💡 使用示例

### 场景 1：生成周报PDF

```bash
# 配置总结发送到专门的频道
[p]summary config summarychannel #weekly-reports

# 生成全服务器总结PDF
[p]summary all

# 结果：
# 1. Discord中显示所有总结
# 2. 自动生成PDF文件
# 3. PDF上传到频道
# 4. 可以直接下载保存
```

### 场景 2：特定分类报告

```bash
# 只生成公告区的PDF报告
[p]summary category 公告区

# 文件名: summary_公告区_20251105.pdf
```

### 场景 3：不需要PDF的快速查看

```bash
# 只在Discord中查看，不生成PDF
[p]summary all false
```

## 🔧 故障排查

### 问题1：PDF生成失败

**可能原因**：
- reportlab 未安装
- 系统缺少必要的字体

**解决方法**：
```bash
# 安装依赖
pip install reportlab Pillow

# 查看日志
[p]traceback
```

### 问题2：中文显示为方块 ⭐ 已修复

**v1.2.1 更新**：已修复TTC字体文件注册问题

**检测字体**：
```bash
# 使用新命令检测系统字体
[p]summary config testfont
```

这个命令会：
- ✅ 扫描系统中的中文字体
- ✅ 测试字体是否可以正常注册
- ✅ 显示可用的字体列表
- ✅ 提供安装建议

### 问题3：中文仍然显示为方块

**原因**：系统没有中文字体

**解决方法**：
- macOS: 已内置中文字体，无需处理
- Linux: 安装中文字体
  ```bash
  sudo apt-get install fonts-arphic-uming
  ```
- Windows: 确保安装了微软雅黑字体

### 问题3：PDF文件太大无法上传

**原因**：Discord 有文件大小限制（8MB/25MB）

**解决方法**：
- 减少 `maxmessages` 配置
- 分批总结（使用 category 而不是 all）
- 排除不重要的频道

## 📈 性能考虑

### PDF 生成时间

- 单个频道：1-2 秒
- 10 个频道：10-20 秒
- 50 个频道：1-2 分钟

**性能优化**：PDF生成在单独的线程中运行，不会阻塞Discord机器人的其他功能。

### 文件大小估算

- 单个频道：~50-100KB
- 10 个频道：~500KB-1MB
- 50 个频道：~2-5MB

## 🎨 自定义

目前 PDF 样式是固定的，未来版本可能支持：
- ⏳ 自定义颜色主题
- ⏳ 选择不同的模板
- ⏳ 添加服务器图标
- ⏳ 更多统计图表

## 📝 最佳实践

1. **定期生成PDF备份**
   ```bash
   # 每周生成一次全服务器报告
   [p]summary all
   # 下载并存档PDF文件
   ```

2. **分类管理PDF**
   ```bash
   # 不同分类生成独立PDF
   [p]summary category 公告区
   [p]summary category 项目讨论
   [p]summary category 团队协作
   ```

3. **控制文件大小**
   ```bash
   # 调整消息数量
   [p]summary config maxmessages 50
   
   # 排除不重要的分类
   [p]summary config excludecategory 闲聊区
   ```

## 🆘 获取帮助

如果遇到问题：
1. 查看 [安装指南](INSTALL.md)
2. 查看 [常见问题](README.md#常见问题)
3. 提交 [GitHub Issue](https://github.com/yourusername/Red-DiscordBot-AI/issues)

---

**提示**：PDF 功能默认启用，如果你不需要 PDF，可以在命令中添加 `false` 参数。

