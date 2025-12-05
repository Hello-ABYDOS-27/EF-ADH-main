# 逃离学校剧本

## 项目简介

**逃离学校剧本**是一款基于Pygame开发的2D冒险解谜游戏。游戏讲述了一名中学生在参加学校组织的公益活动时，意外来到了一所废弃医院，玩家需要探索场景、解决谜题，最终逃离困境。

## 游戏特色

- 🎮 **简单易上手的操作**：使用WASD控制角色移动，E键互动
- 🎨 **精美的2D像素风格**：精心设计的游戏场景和角色动画
- 🎵 **沉浸式音效**：每个场景都配有独特的背景音乐和音效
- 📖 **丰富的剧情**：包含多条剧情线和隐藏内容
- 🏠 **多样化的场景**：从废弃医院到咖啡厅，每个场景都有独特的谜题和挑战
- ⚙️ **可配置的游戏设置**：支持调整分辨率、帧率和快捷键

## 技术栈

- **开发语言**：Python 3.11
- **游戏引擎**：Pygame
- **版本控制**：Git
- **代码风格**：PEP 8

## 安装与运行

### 前提条件

- Python 3.8 或更高版本
- Git（可选，用于克隆仓库）

### 安装步骤

1. **克隆仓库**（或直接下载源码）
   ```bash
   git clone https://github.com/Hello-ABYDOS-27/EF-ADH-main.git
   cd EF-ADH-main
   ```

2. **创建虚拟环境**（可选但推荐）
   ```bash
   python -m venv .venv
   ```

3. **激活虚拟环境**
   - Windows：
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux：
     ```bash
     source .venv/bin/activate
     ```

4. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

### 运行游戏

```bash
python 1.py
```

## 游戏操作

| 按键 | 功能 |
|------|------|
| W | 向上移动 |
| A | 向左移动 |
| S | 向下移动 |
| D | 向右移动 |
| E | 开门/互动 |
| 空格 | 暂停游戏 |
| ESC | 关闭菜单/返回 |

## 游戏场景

### 1. 废弃医院
- 游戏的初始场景
- 探索医院内部，寻找逃离线索
- 解决大门谜题，开启新篇章

### 2. 咖啡厅
- 穿过废弃医院大门后到达的场景
- 与NPC互动，获取更多剧情信息
- 解锁新的挑战和谜题

### 3. 结婚现场（待更新）
- 后续更新将开放的新场景
- 更多精彩剧情和谜题等待探索

## 项目结构

```
EF-ADH-main/
├── 1.py                    # 游戏主程序
├── requirements.txt         # 项目依赖
├── .gitignore              # Git忽略配置
├── README.md               # 项目说明文档
├── test/                   # 测试相关文件
│   └── 游戏所有废案/        # 游戏开发废案历史
├── scenes/                 # 场景文件
│   ├── hospital.py         # 废弃医院场景
│   └── cafe.py            # 咖啡厅场景
├── ui/                     # UI组件
│   ├── dialog.py           # 对话框系统
│   └── ui_components.py    # UI组件库
├── utils/                  # 工具函数
│   └── collision.py        # 碰撞检测
├── player_idle_down.png    # 玩家资源图片
├── player_idle_left.png
├── player_idle_right.png
├── player_idle_up.png
├── player_walk_down.png
├── player_walk_left.png
├── player_walk_right.png
├── player_walk_up.png
├── player_walk1.png
├── player_walk3.png
├── cafe_bgm.mp3            # 音频资源
├── hospital_bgm.mp3
├── menu_bgm.mp3
└── open_gate.WAV
```

## 开发团队

| 角色 | 成员 | 职责 |
|------|------|------|
| 核心开发者 | 黄 | 代码实现、功能开发 |
| UI设计师 | 凉乞钞_official | UI样式、动画编辑 |
| 主策划 | 矢车菊 | 游戏玩法设计、剧情架构 |
| 玩法顾问 | 坚林 | 冒险解谜玩法建议 |
| 美术负责人 | 沫沫 | 角色/场景美术风格定义 |
| 视觉设计 | 筱 | UI界面设计、颜色搭配 |
| 资源制作 | 京华 | 图片资源绘制、素材处理 |

## 版本历史

- **v1.0.0** (2025-11-24)：初始版本发布，包含废弃医院场景
- **v1.0.1** (2025-11-25)：修复角色移动bug，优化动画效果
- **v1.0.2** (2025-11-30)：新增咖啡厅场景，扩展剧情
- **v1.0.3** (2025-12-02)：优化游戏性能，修复碰撞检测问题
- **v1.0.4** (2025-12-03)：新增游戏设置功能，支持调整分辨率和帧率
- **v1.0.5** (2025-12-05)：修复UI显示问题，优化游戏体验

## 贡献指南

1. **Fork 仓库**：在GitHub上fork项目到自己的账号
2. **创建分支**：从main分支创建新的功能分支
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **开发功能**：实现新功能或修复bug
4. **提交代码**：编写清晰的提交信息
   ```bash
   git commit -m "feat: 添加新功能描述"
   ```
5. **Push 分支**：将代码推送到自己的fork仓库
   ```bash
   git push origin feature/your-feature-name
   ```
6. **创建 Pull Request**：在GitHub上提交Pull Request，描述你的更改

## 行为准则

- 尊重团队成员，友好沟通
- 遵循PEP 8代码风格
- 编写清晰的代码注释
- 提交前确保代码可以正常运行
- 不要提交与游戏无关的文件

## 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 联系方式

- **GitHub Issues**：[提交问题](https://github.com/Hello-ABYDOS-27/EF-ADH-main/issues)
- **开发团队邮箱**：[efadh-team@example.com](mailto:efadh-team@example.com)（示例）

## 鸣谢

感谢所有为项目做出贡献的团队成员和测试玩家！

---

**© 2025 逃离学校剧本开发团队**

*享受游戏，享受开发！*