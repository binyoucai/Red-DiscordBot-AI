# 更新日志

## [v1.2.1] - 2025-11-05

### 🐛 重要修复

#### PDF中文字体问题
- 🔧 **修复TTC字体注册**：正确使用 `subfontIndex` 参数注册TTC字体文件
- 📝 **改进文本处理**：修复XML特殊字符处理顺序，保留换行格式
- 🔍 **增强字体检测**：扩展字体搜索列表，支持更多中文字体
- 📊 **详细日志**：添加字体注册成功/失败的详细日志
- 🎯 **CJK支持**：启用CJK文本换行支持

#### 新增诊断命令
- 🔤 **testfont 命令**：`[p]summary config testfont` 检测系统可用字体
- ✅ 显示找到的字体路径
- ✅ 测试字体是否可以正常注册
- ✅ 提供安装建议

### 🔧 技术改进

- 支持的字体格式：TTC和TTF
- 支持的操作系统：macOS、Linux、Windows
- 新增字体选项：
  - macOS: PingFang, STHeiti, Hiragino Sans GB
  - Linux: AR PL UMing, Droid Sans, WenQuanYi
  - Windows: 微软雅黑, 黑体, 宋体

### 📚 文档更新

- 更新 PDF_GUIDE.md 添加故障排查章节
- 说明字体检测命令的使用方法

---

## [v1.2.0] - 2025-11-05

### ✨ 新增功能

#### PDF报告生成
- 📄 **自动生成PDF**：`summary all` 和 `summary category` 命令现在自动生成PDF报告
- 📊 **专业格式**：使用reportlab生成结构化的PDF文档
- 🌍 **中文支持**：自动检测并使用系统中文字体（macOS/Linux/Windows）
- 💾 **自动上传**：PDF文件自动上传到Discord频道
- 🗑️ **自动清理**：发送后自动删除临时文件
- ⚙️ **可选功能**：可以通过参数关闭PDF生成（`false`）

#### PDF内容
- 📝 包含服务器名称和生成时间
- 📁 按分类和频道组织内容
- 💬 完整的总结文本
- 📊 统计信息（消息数、用户数、时间范围）
- 📄 每个频道独立分页

### 📦 依赖更新
- 新增 `reportlab>=4.0.0` - PDF生成库
- 新增 `Pillow>=9.0.0` - 图像处理支持

---

## [v1.1.1] - 2025-11-05

### ✨ 新增功能

#### 分类总结
- 📁 **category 命令**：`summary category <分类名>` 可以只总结指定分类下的所有频道
- 🎯 **精准控制**：无需排除其他分类，直接指定要总结的分类
- 📋 **支持未分类**：可以专门总结没有分类的频道

### 📚 文档更新

- 更新 README.md 添加 category 命令说明
- 更新 QUICKSTART.md 添加场景 5：只总结特定分类
- 更新 example_config.md 添加只总结特定分类示例
- 更新根目录 README.md 添加 category 命令示例

---

## [v1.1.0] - 2025-11-05

### ✨ 新增功能

#### 频道分类管理
- 📁 **分类显示**：总结标题现在显示"分类 / 频道名"格式
- 📊 **按分类分组**：使用 `summary all` 时按分类分组显示所有频道
- 🔧 **排除分类**：新增 `excludecategory` 和 `includecategory` 命令，可一次性排除整个分类
- 🎯 **未分类支持**：支持排除没有分类的频道

#### 全服务器定时任务
- ⏰ **addall 命令**：`summary schedule addall <间隔>` 添加全服务器定时总结任务
- 🗑️ **removeall 命令**：`summary schedule removeall` 移除全服务器定时任务
- ▶️ **runall 命令**：`summary schedule runall` 手动运行全服务器定时任务
- 🔄 **自动恢复**：机器人重启后自动恢复全服务器定时任务

#### 新增配置选项
- `excluded_categories`：排除的分类列表配置项
- 支持通过分类名称快速管理大量频道

### 🔧 改进

- **错误处理**：改进了网络错误时的处理，typing 失败不影响主要功能
- **日志优化**：使用 Python logging 模块替代 print 语句
- **代码重构**：提取 `_execute_all_summary` 和 `_is_channel_excluded` 方法提高代码复用
- **配置展示**：`config show` 命令现在显示排除的分类列表

### 📚 文档更新

- 更新 README.md 添加新功能说明
- 更新 QUICKSTART.md 添加新的使用场景
- 更新 example_config.md 添加分类管理示例
- 添加 CHANGELOG.md 记录版本变更

### 🎨 用户体验

- 更清晰的频道组织结构
- 更高效的配置管理（分类级别）
- 更灵活的定时任务选项
- 更友好的错误提示

---

## [v1.0.0] - 2025-11-04

### 🎉 首次发布

#### 核心功能
- 📊 单频道总结功能
- 🌐 全服务器总结功能
- ⏰ 定时任务系统
- 🤖 OpenAI API 集成
- 📈 统计分析功能

#### 配置选项
- API Key 管理
- API Base URL 配置
- 模型选择
- 消息数量限制
- 频道排除
- 机器人消息过滤

#### 定时任务
- 单频道定时总结
- 任务启用/禁用
- 手动运行任务
- 任务列表查看

#### 文档
- 完整的 README.md
- 详细的 INSTALL.md 安装指南
- QUICKSTART.md 快速开始指南
- example_config.md 配置示例

---

## 计划中的功能

### v1.2.0（规划中）
- 🖼️ 支持图片内容识别和描述
- 📊 导出总结为 PDF/文档
- 🌐 多语言总结支持
- 📅 指定时间范围的总结
- 🎨 自定义总结模板

### v1.3.0（规划中）
- 🔍 关键词提取和标签
- 📈 趋势分析
- 🤖 更多 AI 模型支持
- 💬 互动式总结

---

## 升级指南

### 从 v1.0.0 升级到 v1.1.0

1. **更新代码**：
```bash
# 如果通过 Git 安装
cd /path/to/Red-DiscordBot/cogs/chatsummary
git pull

# 如果手动安装
# 下载最新版本并替换文件
```

2. **重新加载插件**：
```bash
[p]reload chatsummary
```

3. **无需额外配置**：
   - 现有配置自动兼容
   - 新增的 `excluded_categories` 配置项会自动初始化为空列表
   - 现有定时任务继续正常运行

4. **使用新功能**（可选）：
```bash
# 尝试新的分类排除功能
[p]summary config excludecategory 管理区

# 尝试全服务器定时任务
[p]summary schedule addall 24

# 查看更新后的配置
[p]summary config show
```

---

## 贡献

欢迎提交 Issue 和 Pull Request！

如果你有好的想法或发现了 Bug，请：
1. 查看现有的 Issues
2. 创建新的 Issue 描述问题或建议
3. Fork 项目并提交 PR

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

