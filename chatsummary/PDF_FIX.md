# PDF中文乱码问题修复指南

## 🎯 问题描述

如果你生成的PDF文件中中文显示为黑色方块（■■■），这是因为系统缺少中文字体或字体注册失败。

## ✅ v1.2.1 修复

**已修复**：TTC字体文件注册问题（这是导致乱码的主要原因）

### 主要改进

1. **正确注册TTC字体**
   - 使用 `subfontIndex=0` 参数
   - 支持 macOS/Linux/Windows 的TTC字体

2. **扩展字体支持**
   - macOS: PingFang, STHeiti, Hiragino Sans GB
   - Linux: AR PL UMing, Droid Sans, WenQuanYi  
   - Windows: 微软雅黑, 黑体, 宋体

3. **改进文本处理**
   - 修复特殊字符转义顺序
   - 启用CJK文本换行
   - 保留段落格式

## 🔍 检测字体

使用新增的诊断命令检测系统字体：

```bash
!summary config testfont
```

**这个命令会告诉你**：
- ✅ 系统中找到了哪些中文字体
- ✅ 哪些字体可以正常使用
- ❌ 是否存在字体问题
- 💡 如何解决问题

## 📝 立即测试

### 步骤1：更新代码

```bash
# 重新加载插件
!reload chatsummary
```

### 步骤2：检测字体

```bash
!summary config testfont
```

### 步骤3：生成测试PDF

```bash
# 生成一个简单的分类总结测试
!summary category 你的分类名
```

### 步骤4：检查结果

下载PDF文件，打开查看中文是否正常显示。

## 🔧 如果仍然乱码

### macOS

macOS 通常已内置中文字体，如果仍然乱码：

```bash
# 检查字体是否存在
ls /System/Library/Fonts/PingFang.ttc

# 查看日志
!traceback
```

### Linux

安装中文字体包：

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install fonts-arphic-uming fonts-wqy-zenhei

# CentOS/RHEL
sudo yum install wqy-zenhei-fonts

# Arch Linux
sudo pacman -S wqy-zenhei
```

安装后重启机器人：
```bash
# 在Discord中
!restart
```

### Windows

Windows通常已内置微软雅黑，如果缺失：

1. 打开控制面板
2. 进入"字体"
3. 确认是否有"微软雅黑"
4. 如果没有，从其他Windows系统复制或下载安装

## 📊 预期结果

修复后的PDF应该显示：

```
服务器名 - Summary Report

Generated: 2025-11-05 23:00:00 UTC
Server: 你的服务器

公告区 / announcements

这是一段中文总结内容，应该完全正常显示，
不会出现任何方块或乱码。

Messages: 150 | Users: 12 | Time: 2025-11-04...
```

## 🆘 获取帮助

如果按照以上步骤仍然无法解决：

1. **运行字体检测**：
   ```bash
   !summary config testfont
   ```
   将结果截图

2. **查看日志**：
   ```bash
   !traceback
   ```
   查找相关错误

3. **提供信息**：
   - 操作系统版本
   - Python版本
   - reportlab版本
   - 字体检测结果

4. **提交Issue**：
   [GitHub Issues](https://github.com/yourusername/Red-DiscordBot-AI/issues)

## 💡 技术说明

### TTC vs TTF

- **TTC (TrueType Collection)**: 包含多个字体的集合文件
  - 需要使用 `subfontIndex` 参数指定使用哪个字体
  - 例如：`TTFont('Chinese', 'PingFang.ttc', subfontIndex=0)`

- **TTF (TrueType Font)**: 单个字体文件
  - 直接注册即可
  - 例如：`TTFont('Chinese', 'simhei.ttf')`

### 字体优先级

系统按以下顺序尝试注册字体（使用第一个成功的）：

1. macOS PingFang (现代、清晰)
2. macOS STHeiti (传统黑体)
3. Linux AR PL UMing (开源明体)
4. Windows 微软雅黑 (现代、清晰)
5. 其他备选字体...

### 为什么之前会乱码

**原因**：TTC文件包含多个字体，但代码没有指定使用哪一个。

**修复**：添加 `subfontIndex=0` 参数，明确使用第一个字体。

## 🎉 验证修复

如果修复成功，你应该看到：

1. **testfont命令显示**：
   ```
   ✅ 可用于PDF
   macOS PingFang (或其他字体名称)
   ```

2. **PDF文件中**：
   - 标题正常显示中文
   - 正文内容清晰可读
   - 统计信息正确显示

3. **日志中**：
   ```
   成功注册中文字体: /System/Library/Fonts/PingFang.ttc
   ```

---

**更新时间**：2025-11-05
**修复版本**：v1.2.1

