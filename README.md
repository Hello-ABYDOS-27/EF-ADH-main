# 多语言版本 | Multi-language Version | 多語言版本

> 选择您的语言 | Select your language | 選擇您的語言
> - [中文-简体](#中文-简体)
> - [中文-繁体](#中文-繁体)
> - [English](#english)
> - [日本語](#日本語)
> - [中文-文言](#中文-文言)

---

## 中文-简体

### 逃离学校剧本

#### 项目简介

**逃离学校剧本**是一款基于Pygame开发的2D冒险解谜游戏。游戏讲述了一名中学生在参加学校组织的公益活动时，意外来到了一所废弃医院，玩家需要探索场景、解决谜题，最终逃离困境。

#### 游戏特色

- 🎮 **简单易上手的操作**：使用WASD控制角色移动，E键互动
- 🎨 **精美的2D像素风格**：精心设计的游戏场景和角色动画
- 🎵 **沉浸式音效**：每个场景都配有独特的背景音乐和音效
- 📖 **丰富的剧情**：包含多条剧情线和隐藏内容
- 🏠 **多样化的场景**：从废弃医院到咖啡厅，每个场景都有独特的谜题和挑战
- ⚙️ **可配置的游戏设置**：支持调整分辨率、帧率和快捷键

#### 技术栈

- **开发语言**：Python 3.11
- **游戏引擎**：Pygame
- **版本控制**：Git
- **代码风格**：PEP 8

#### 下载与运行

##### 下载游戏

1. **从Releases页面下载**：
   - 访问GitHub仓库：[https://github.com/Hello-ABYDOS-27/EF-ADH-main](https://github.com/Hello-ABYDOS-27/EF-ADH-main)
   - 找到右侧红色框标记的 "Releases" 部分
   - 点击 "Create a new release"（如果已发布，会显示最新版本）
   - 下载最新版本的游戏压缩包
   - 下载完成后，解压压缩包到您想要安装游戏的位置

##### 运行游戏

1. **打开游戏目录**：
   - 解压后，进入解压后的文件夹 `EF-ADH-main`

2. **运行游戏**：
   - 找到并双击 `game.exe` 文件
   - 游戏将自动启动

##### 注意事项

- 游戏仅支持Windows系统
- 确保您的系统已安装DirectX或OpenGL图形库
- 首次运行游戏可能需要一些时间加载资源
- 建议关闭其他占用大量系统资源的程序，以获得最佳游戏体验

#### 游戏操作

| 按键 | 功能 |
|------|------|
| W | 向上移动 |
| A | 向左移动 |
| S | 向下移动 |
| D | 向右移动 |
| E | 开门/互动 |
| 空格 | 暂停游戏 |
| ESC | 关闭菜单/返回 |

#### 游戏场景

##### 1. 废弃医院
- 游戏的初始场景
- 探索医院内部，寻找逃离线索
- 解决大门谜题，开启新篇章

##### 2. 咖啡厅
- 穿过废弃医院大门后到达的场景
- 与NPC互动，获取更多剧情信息
- 解锁新的挑战和谜题

##### 3. 结婚现场（待更新）
- 后续更新将开放的新场景
- 更多精彩剧情和谜题等待探索

#### 项目结构

```
EF-ADH-main/
├── main.py                 # 游戏主程序
├── requirements.txt         # 项目依赖
├── .gitignore              # Git忽略配置
├── README.md               # 项目说明文档
├── audio/                  # 音频资源
│   ├── cafe_bgm.mp3        # 咖啡厅背景音乐
│   ├── hospital_bgm.mp3    # 废弃医院背景音乐
│   ├── menu_bgm.mp3        # 主菜单背景音乐
│   └── open_gate.WAV       # 开门音效
├── images/                 # 图片资源
│   ├── github.webp         # GitHub图标
│   ├── player_idle_down.png # 玩家向下站立动画帧
│   ├── player_idle_left.png # 玩家向左站立动画帧
│   ├── player_idle_right.png # 玩家向右站立动画帧
│   ├── player_idle_up.png  # 玩家向上站立动画帧
│   ├── player_walk1.png    # 玩家行走备用动画帧1
│   ├── player_walk3.png    # 玩家行走备用动画帧3
│   ├── player_walk_down.png # 玩家向下行走动画帧
│   ├── player_walk_left.png # 玩家向左行走动画帧
│   ├── player_walk_right.png # 玩家向右行走动画帧
│   └── player_walk_up.png  # 玩家向上行走动画帧
├── test/                   # 测试相关文件
│   └── 游戏所有废案/        # 游戏开发废案历史
├── scenes/                 # 场景文件
│   ├── hospital.py         # 废弃医院场景
│   └── cafe.py            # 咖啡厅场景
├── ui/                     # UI组件
│   ├── dialog.py           # 对话框系统
│   └── ui_components.py    # UI组件库
└── utils/                  # 工具函数
    └── collision.py        # 碰撞检测
```

#### 文件功能说明

##### 核心文件

| 文件名 | 类型 | 功能说明 |
|--------|------|----------|
| main.py | Python代码 | 游戏的主程序文件，包含游戏的初始化、主循环、事件处理和场景管理 |
| requirements.txt | 文本文件 | 项目依赖列表，包含游戏运行所需的所有Python库 |
| README.md | Markdown文档 | 项目说明文档，包含项目简介、安装步骤、游戏操作等信息 |
| .gitignore | 文本文件 | Git忽略配置，指定不需要被Git跟踪的文件和目录 |

##### 音频资源

| 文件名 | 类型 | 功能说明 |
|--------|------|----------|
| audio/cafe_bgm.mp3 | 音频 | 咖啡厅场景的背景音乐 |
| audio/hospital_bgm.mp3 | 音频 | 废弃医院场景的背景音乐 |
| audio/menu_bgm.mp3 | 音频 | 主菜单和副本选择界面的背景音乐 |
| audio/open_gate.WAV | 音频 | 开门音效，用于玩家打开大门时播放 |

##### 图片资源

| 文件名 | 类型 | 功能说明 |
|--------|------|----------|
| images/github.webp | 图片 | GitHub图标，用于项目相关链接 |
| images/player_idle_down.png | 图片 | 玩家向下站立的 idle 动画帧 |
| images/player_idle_left.png | 图片 | 玩家向左站立的 idle 动画帧 |
| images/player_idle_right.png | 图片 | 玩家向右站立的 idle 动画帧 |
| images/player_idle_up.png | 图片 | 玩家向上站立的 idle 动画帧 |
| images/player_walk1.png | 图片 | 玩家行走的备用动画帧1 |
| images/player_walk3.png | 图片 | 玩家行走的备用动画帧3 |
| images/player_walk_down.png | 图片 | 玩家向下行走的动画帧 |
| images/player_walk_left.png | 图片 | 玩家向左行走的动画帧 |
| images/player_walk_right.png | 图片 | 玩家向右行走的动画帧 |
| images/player_walk_up.png | 图片 | 玩家向上行走的动画帧 |

##### 场景文件

| 文件名 | 类型 | 功能说明 |
|--------|------|----------|
| scenes/hospital.py | Python代码 | 废弃医院场景的实现，包含场景绘制、碰撞检测和互动逻辑 |
| scenes/cafe.py | Python代码 | 咖啡厅场景的实现，包含场景绘制、碰撞检测和互动逻辑 |

##### UI组件文件

| 文件名 | 类型 | 功能说明 |
|--------|------|----------|
| ui/dialog.py | Python代码 | 对话框系统的实现，用于显示游戏剧情和角色对话 |
| ui/ui_components.py | Python代码 | 通用UI组件库，包含按钮、滑块、菜单等UI元素的实现 |

##### 工具函数文件

| 文件名 | 类型 | 功能说明 |
|--------|------|----------|
| utils/collision.py | Python代码 | 碰撞检测工具，用于检测玩家与游戏对象之间的碰撞 |

##### 测试文件

| 文件名 | 类型 | 功能说明 |
|--------|------|----------|
| test/游戏所有废案/ | 目录 | 游戏开发过程中的废案历史，包含废弃的设计方案和代码 |
| test/游戏所有废案/介绍.md | Markdown文档 | 废案历史的介绍和说明 |
| test/游戏所有废案/scenes/ | 目录 | 废弃的场景代码 |
| test/游戏所有废案/ui/ | 目录 | 废弃的UI组件代码 |
| test/游戏所有废案/utils/ | 目录 | 废弃的工具函数代码 |

#### 开发团队

| 角色 | 成员 | 职责 |
|------|------|------|
| 核心开发者 | 黄 | 代码实现、功能开发 |
| UI设计师 | 凉乞钞_official | UI样式、动画编辑 |
| 主策划 | 矢车菊 | 游戏玩法设计、剧情架构 |
| 玩法顾问 | 坚林 | 冒险解谜玩法建议 |
| 美术负责人 | 沫沫 | 角色/场景美术风格定义 |
| 视觉设计 | 筱 | UI界面设计、颜色搭配 |
| 资源制作 | 京华 | 图片资源绘制、素材处理 |

#### 版本历史

- **v1.0.0** (2025-11-24)：初始版本发布，包含废弃医院场景
- **v1.0.1** (2025-11-25)：修复角色移动bug，优化动画效果
- **v1.0.2** (2025-11-30)：新增咖啡厅场景，扩展剧情
- **v1.0.3** (2025-12-02)：优化游戏性能，修复碰撞检测问题
- **v1.0.4** (2025-12-03)：新增游戏设置功能，支持调整分辨率和帧率
- **v1.0.5** (2025-12-05)：修复UI显示问题，优化游戏体验
- **v1.1.0** (2025-12-06)：优化资源文件结构，将音频和图片文件整理到专门目录

#### 游戏开发废案历史

##### 废案一：模块化拆分方案

**方案概述**：
将游戏拆分为多个独立的小模块，每个模块负责特定功能，如场景渲染、角色控制、UI交互等。目的是提高开发效率，方便团队成员独立开发和测试。

**预期优势**：
- 便于团队协作，降低代码冲突
- 模块化设计便于维护和扩展
- 独立测试，提高代码质量
- 可以根据需求灵活替换模块

**实际挑战**：
- 模块间接口设计复杂，集成难度大
- 跨模块调用导致性能开销
- 团队沟通成本增加
- 模块依赖关系复杂，构建时间长

**废除原因**：
拆分后的模块在实际运行中出现显示问题，导致游戏无法正常启动。具体表现为模块加载顺序混乱，资源依赖关系错误，最终导致游戏崩溃。

**废除日期**：2025年12月3日

##### 经验教训

1. **模块化设计需要谨慎**：在进行模块化拆分前，必须充分考虑模块间的依赖关系和接口设计
2. **测试驱动开发**：每个模块在开发过程中都需要进行充分的单元测试和集成测试
3. **渐进式拆分**：避免一次性大规模拆分，建议采用渐进式拆分策略，逐步验证拆分效果
4. **文档先行**：在进行模块化设计前，必须编写详细的设计文档，明确模块间的接口和依赖关系
5. **团队协作机制**：建立有效的团队协作机制，确保模块开发人员之间的良好沟通

#### 贡献指南

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

#### 行为准则

- 尊重团队成员，友好沟通
- 遵循PEP 8代码风格
- 编写清晰的代码注释
- 提交前确保代码可以正常运行
- 不要提交与游戏无关的文件

#### 许可证

本项目采用自定义许可证，详见LICENSE文件。许可证内容包括轻度使用和重度使用的不同条款，旨在平衡开源共享与保护原创作品权益。

#### 联系方式

- **GitHub Issues**：[提交问题](https://github.com/Hello-ABYDOS-27/EF-ADH-main/issues)
- **开发团队邮箱**：[efadh-team@example.com](mailto:efadh-team@example.com)（示例）

#### 鸣谢

感谢所有为项目做出贡献的团队成员和测试玩家！

---

## 中文-繁体

### 逃離學校劇本

#### 專案簡介

**逃離學校劇本**是一款基於Pygame開發的2D冒險解謎遊戲。遊戲講述了一名中學生在參加學校組織的公益活動時，意外來到了一所廢棄醫院，玩家需要探索場景、解決謎題，最終逃離困境。

#### 遊戲特色

- 🎮 **簡單易上手的操作**：使用WASD控制角色移動，E鍵互動
- 🎨 **精美的2D像素風格**：精心設計的遊戲場景和角色動畫
- 🎵 **沉浸式音效**：每個場景都配有獨特的背景音樂和音效
- 📖 **豐富的劇情**：包含多條劇情線和隱藏內容
- 🏠 **多樣化的場景**：從廢棄醫院到咖啡廳，每個場景都有獨特的謎題和挑戰
- ⚙️ **可配置的遊戲設定**：支持調整解析度、幀率和快捷鍵

#### 技術棧

- **開發語言**：Python 3.11
- **遊戲引擎**：Pygame
- **版本控制**：Git
- **代碼風格**：PEP 8

#### 下載與運行

##### 下載遊戲

1. **從Releases頁面下載**：
   - 訪問GitHub倉庫：[https://github.com/Hello-ABYDOS-27/EF-ADH-main](https://github.com/Hello-ABYDOS-27/EF-ADH-main)
   - 找到右側紅色框標記的 "Releases" 部分
   - 點擊 "Create a new release"（如果已發布，會顯示最新版本）
   - 下載最新版本的遊戲壓縮包
   - 下載完成後，解壓縮包到您想要安裝遊戲的位置

##### 運行遊戲

1. **打開遊戲目錄**：
   - 解壓後，進入解壓後的文件夾 `EF-ADH-main`

2. **運行遊戲**：
   - 找到並雙擊 `game.exe` 文件
   - 遊戲將自動啟動

##### 注意事項

- 遊戲僅支持Windows系統
- 確保您的系統已安裝DirectX或OpenGL圖形庫
- 首次運行遊戲可能需要一些時間加載資源
- 建議關閉其他佔用大量系統資源的程序，以獲得最佳遊戲體驗

#### 遊戲操作

| 按鍵 | 功能 |
|------|------|
| W | 向上移動 |
| A | 向左移動 |
| S | 向下移動 |
| D | 向右移動 |
| E | 開門/互動 |
| 空格 | 暫停遊戲 |
| ESC | 關閉菜單/返回 |

#### 遊戲場景

##### 1. 廢棄醫院
- 遊戲的初始場景
- 探索醫院內部，尋找逃離線索
- 解決大門謎題，開啟新篇章

##### 2. 咖啡廳
- 穿過廢棄醫院大門後到達的場景
- 與NPC互動，獲取更多劇情信息
- 解鎖新的挑戰和謎題

##### 3. 結婚現場（待更新）
- 後續更新將開放的新場景
- 更多精彩劇情和謎題等待探索

#### 專案結構

```
EF-ADH-main/
├── main.py                 # 遊戲主程序
├── requirements.txt         # 專案依賴
├── .gitignore              # Git忽略配置
├── README.md               # 專案說明文件
├── audio/                  # 音訊資源
│   ├── cafe_bgm.mp3        # 咖啡廳背景音樂
│   ├── hospital_bgm.mp3    # 廢棄醫院背景音樂
│   ├── menu_bgm.mp3        # 主菜單背景音樂
│   └── open_gate.WAV       # 開門音效
├── images/                 # 圖片資源
│   ├── github.webp         # GitHub圖標
│   ├── player_idle_down.png # 玩家向下站立動畫幀
│   ├── player_idle_left.png # 玩家向左站立動畫幀
│   ├── player_idle_right.png # 玩家向右站立動畫幀
│   ├── player_idle_up.png  # 玩家向上站立動畫幀
│   ├── player_walk1.png    # 玩家行走備用動畫幀1
│   ├── player_walk3.png    # 玩家行走備用動畫幀3
│   ├── player_walk_down.png # 玩家向下行走動畫幀
│   ├── player_walk_left.png # 玩家向左行走動畫幀
│   ├── player_walk_right.png # 玩家向右行走動畫幀
│   └── player_walk_up.png  # 玩家向上行走動畫幀
├── test/                   # 測試相關文件
│   └── 遊戲所有廢案/        # 遊戲開發廢案歷史
├── scenes/                 # 場景文件
│   ├── hospital.py         # 廢棄醫院場景
│   └── cafe.py            # 咖啡廳場景
├── ui/                     # UI組件
│   ├── dialog.py           # 對話框系統
│   └── ui_components.py    # UI組件庫
└── utils/                  # 工具函數
    └── collision.py        # 碰撞檢測
```

#### 文件功能說明

##### 核心文件

| 文件名 | 類型 | 功能說明 |
|--------|------|----------|
| main.py | Python代碼 | 遊戲的主程序文件，包含遊戲的初始化、主循環、事件處理和場景管理 |
| requirements.txt | 文本文件 | 專案依賴列表，包含遊戲運行所需的所有Python庫 |
| README.md | Markdown文件 | 專案說明文件，包含專案簡介、安裝步驟、遊戲操作等信息 |
| .gitignore | 文本文件 | Git忽略配置，指定不需要被Git跟蹤的文件和目錄 |

##### 音訊資源

| 文件名 | 類型 | 功能說明 |
|--------|------|----------|
| audio/cafe_bgm.mp3 | 音訊 | 咖啡廳場景的背景音樂 |
| audio/hospital_bgm.mp3 | 音訊 | 廢棄醫院場景的背景音樂 |
| audio/menu_bgm.mp3 | 音訊 | 主菜單和副本選擇界面的背景音樂 |
| audio/open_gate.WAV | 音訊 | 開門音效，用於玩家打開大門時播放 |

##### 圖片資源

| 文件名 | 類型 | 功能說明 |
|--------|------|----------|
| images/github.webp | 圖片 | GitHub圖標，用於專案相關鏈接 |
| images/player_idle_down.png | 圖片 | 玩家向下站立的 idle 動畫幀 |
| images/player_idle_left.png | 圖片 | 玩家向左站立的 idle 動畫幀 |
| images/player_idle_right.png | 圖片 | 玩家向右站立的 idle 動畫幀 |
| images/player_idle_up.png | 圖片 | 玩家向上站立的 idle 動畫幀 |
| images/player_walk1.png | 圖片 | 玩家行走的備用動畫幀1 |
| images/player_walk3.png | 圖片 | 玩家行走的備用動畫幀3 |
| images/player_walk_down.png | 圖片 | 玩家向下行走的動畫幀 |
| images/player_walk_left.png | 圖片 | 玩家向左行走的動畫幀 |
| images/player_walk_right.png | 圖片 | 玩家向右行走的動畫幀 |
| images/player_walk_up.png | 圖片 | 玩家向上行走的動畫幀 |

##### 場景文件

| 文件名 | 類型 | 功能說明 |
|--------|------|----------|
| scenes/hospital.py | Python代碼 | 廢棄醫院場景的實現，包含場景繪製、碰撞檢測和互動邏輯 |
| scenes/cafe.py | Python代碼 | 咖啡廳場景的實現，包含場景繪製、碰撞檢測和互動邏輯 |

##### UI組件文件

| 文件名 | 類型 | 功能說明 |
|--------|------|----------|
| ui/dialog.py | Python代碼 | 對話框系統的實現，用於顯示遊戲劇情和角色對話 |
| ui/ui_components.py | Python代碼 | 通用UI組件庫，包含按鈕、滑塊、菜單等UI元素的實現 |

##### 工具函數文件

| 文件名 | 類型 | 功能說明 |
|--------|------|----------|
| utils/collision.py | Python代碼 | 碰撞檢測工具，用於檢測玩家與遊戲物件之間的碰撞 |

##### 測試文件

| 文件名 | 類型 | 功能說明 |
|--------|------|----------|
| test/遊戲所有廢案/ | 目錄 | 遊戲開發過程中的廢案歷史，包含廢棄的設計方案和代碼 |
| test/遊戲所有廢案/介紹.md | Markdown文件 | 廢案歷史的介紹和說明 |
| test/遊戲所有廢案/scenes/ | 目錄 | 廢棄的場景代碼 |
| test/遊戲所有廢案/ui/ | 目錄 | 廢棄的UI組件代碼 |
| test/遊戲所有廢案/utils/ | 目錄 | 廢棄的工具函數代碼 |

#### 開發團隊

| 角色 | 成員 | 職責 |
|------|------|------|
| 核心開發者 | 黃 | 代碼實現、功能開發 |
| UI設計師 | 涼乞鈔_official | UI樣式、動畫編輯 |
| 主策劃 | 矢車菊 | 遊戲玩法設計、劇情架構 |
| 玩法顧問 | 堅林 | 冒險解謎玩法建議 |
| 美術負責人 | 沫沫 | 角色/場景美術風格定義 |
| 視覺設計 | 筱 | UI界面設計、顏色搭配 |
| 資源製作 | 京華 | 圖片資源繪製、素材處理 |

#### 版本歷史

- **v1.0.0** (2025-11-24)：初始版本發布，包含廢棄醫院場景
- **v1.0.1** (2025-11-25)：修復角色移動bug，優化動畫效果
- **v1.0.2** (2025-11-30)：新增咖啡廳場景，擴展劇情
- **v1.0.3** (2025-12-02)：優化遊戲性能，修復碰撞檢測問題
- **v1.0.4** (2025-12-03)：新增遊戲設定功能，支持調整解析度和幀率
- **v1.0.5** (2025-12-05)：修復UI顯示問題，優化遊戲體驗
- **v1.1.0** (2025-12-06)：優化資源文件結構，將音訊和圖片文件整理到專門目錄

#### 遊戲開發廢案歷史

##### 廢案一：模組化拆分方案

**方案概述**：
將遊戲拆分為多個獨立的小模組，每個模組負責特定功能，如場景渲染、角色控制、UI互動等。目的是提高開發效率，方便團隊成員獨立開發和測試。

**預期優勢**：
- 便於團隊協作，降低代碼衝突
- 模組化設計便於維護和擴展
- 獨立測試，提高代碼質量
- 可以根據需求靈活替換模組

**實際挑戰**：
- 模組間介面設計複雜，集成難度大
- 跨模組調用導致性能開銷
- 團隊溝通成本增加
- 模組依賴關係複雜，構建時間長

**廢除原因**：
拆分後的模組在實際運行中出現顯示問題，導致遊戲無法正常啟動。具體表現為模組載入順序混亂，資源依賴關係錯誤，最終導致遊戲崩潰。

**廢除日期**：2025年12月3日

##### 經驗教訓

1. **模組化設計需要謹慎**：在進行模組化拆分前，必須充分考慮模組間的依賴關係和介面設計
2. **測試驅動開發**：每個模組在開發過程中都需要進行充分的單元測試和集成測試
3. **漸進式拆分**：避免一次性大規模拆分，建議採用漸進式拆分策略，逐步驗證拆分效果
4. **文檔先行**：在進行模組化設計前，必須編寫詳細的設計文檔，明確模組間的介面和依賴關係
5. **團隊協作機制**：建立有效的團隊協作機制，確保模組開發人員之間的良好溝通

#### 貢獻指南

1. **Fork 倉庫**：在GitHub上fork專案到自己的帳號
2. **建立分支**：從main分支建立新的功能分支
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **開發功能**：實現新功能或修復bug
4. **提交代碼**：編寫清晰的提交資訊
   ```bash
   git commit -m "feat: 添加新功能描述"
   ```
5. **Push 分支**：將代碼推送到自己的fork倉庫
   ```bash
   git push origin feature/your-feature-name
   ```
6. **建立 Pull Request**：在GitHub上提交Pull Request，描述你的更改

#### 行為準則

- 尊重團隊成員，友好溝通
- 遵循PEP 8代碼風格
- 編寫清晰的代碼註釋
- 提交前確保代碼可以正常運行
- 不要提交與遊戲無關的文件

#### 許可證

本專案採用自定義許可證，詳見LICENSE文件。許可證內容包括輕度使用和重度使用的不同條款，旨在平衡開源共享與保護原創作品權益。

#### 聯繫方式

- **GitHub Issues**：[提交問題](https://github.com/Hello-ABYDOS-27/EF-ADH-main/issues)
- **開發團隊郵箱**：[efadh-team@example.com](mailto:efadh-team@example.com)（範例）

#### 鳴謝

感謝所有為專案做出貢獻的團隊成員和測試玩家！

---

## English

### Escape School Script

#### Project Introduction

**Escape School Script** is a 2D adventure puzzle game developed with Pygame. The game tells the story of a middle school student who accidentally arrives at an abandoned hospital during a school-organized charity event. Players need to explore scenes, solve puzzles, and ultimately escape from the predicament.

#### Game Features

- 🎮 **Simple and easy-to-use controls**：Use WASD to move characters, E to interact
- 🎨 **Beautiful 2D pixel art style**：Carefully designed game scenes and character animations
- 🎵 **Immersive sound effects**：Each scene has unique background music and sound effects
- 📖 **Rich storyline**：Contains multiple storylines and hidden content
- 🏠 **Diverse scenes**：From abandoned hospitals to cafes, each scene has unique puzzles and challenges
- ⚙️ **Configurable game settings**：Support for adjusting resolution, frame rate, and shortcuts

#### Tech Stack

- **Development Language**：Python 3.11
- **Game Engine**：Pygame
- **Version Control**：Git
- **Code Style**：PEP 8

#### Download and Run

##### Download the Game

1. **Download from the Releases page**：
   - Visit the GitHub repository：[https://github.com/Hello-ABYDOS-27/EF-ADH-main](https://github.com/Hello-ABYDOS-27/EF-ADH-main)
   - Find the "Releases" section marked by the red box on the right
   - Click "Create a new release"（if already released, the latest version will be displayed）
   - Download the latest version of the game zip package
   - After downloading, extract the zip package to the location where you want to install the game

##### Run the Game

1. **Open the game directory**：
   - After extraction, enter the extracted folder `EF-ADH-main`

2. **Run the game**：
   - Find and double-click the `game.exe` file
   - The game will start automatically

##### Notes

- The game only supports Windows systems
- Ensure your system has DirectX or OpenGL graphics libraries installed
- The first run may take some time to load resources
- It is recommended to close other programs that consume a lot of system resources for the best gaming experience

#### Game Controls

| Key | Function |
|------|------|
| W | Move up |
| A | Move left |
| S | Move down |
| D | Move right |
| E | Open door/Interact |
| Space | Pause game |
| ESC | Close menu/Return |

#### Game Scenes

##### 1. Abandoned Hospital
- The initial scene of the game
- Explore the hospital interior, find escape clues
- Solve the door puzzle to start a new chapter

##### 2. Cafe
- The scene reached after passing through the abandoned hospital gate
- Interact with NPCs to get more plot information
- Unlock new challenges and puzzles

##### 3. Wedding Scene (Coming Soon)
- A new scene to be opened in future updates
- More exciting plots and puzzles to explore

#### Project Structure

```
EF-ADH-main/
├── main.py                 # Game main program
├── requirements.txt         # Project dependencies
├── .gitignore              # Git ignore configuration
├── README.md               # Project documentation
├── audio/                  # Audio resources
│   ├── cafe_bgm.mp3        # Cafe background music
│   ├── hospital_bgm.mp3    # Abandoned hospital background music
│   ├── menu_bgm.mp3        # Main menu background music
│   └── open_gate.WAV       # Door opening sound effect
├── images/                 # Image resources
│   ├── github.webp         # GitHub icon
│   ├── player_idle_down.png # Player idle down animation frame
│   ├── player_idle_left.png # Player idle left animation frame
│   ├── player_idle_right.png # Player idle right animation frame
│   ├── player_idle_up.png  # Player idle up animation frame
│   ├── player_walk1.png    # Player walk alternate animation frame 1
│   ├── player_walk3.png    # Player walk alternate animation frame 3
│   ├── player_walk_down.png # Player walk down animation frame
│   ├── player_walk_left.png # Player walk left animation frame
│   ├── player_walk_right.png # Player walk right animation frame
│   └── player_walk_up.png  # Player walk up animation frame
├── test/                   # Test related files
│   └── 游戏所有废案/        # Game development discarded history
├── scenes/                 # Scene files
│   ├── hospital.py         # Abandoned hospital scene
│   └── cafe.py            # Cafe scene
├── ui/                     # UI components
│   ├── dialog.py           # Dialog system
│   └── ui_components.py    # UI component library
└── utils/                  # Utility functions
    └── collision.py        # Collision detection
```

#### File Function Description

##### Core Files

| File Name | Type | Function Description |
|--------|------|----------|
| main.py | Python code | The main program file of the game, including game initialization, main loop, event handling, and scene management |
| requirements.txt | Text file | Project dependency list, including all Python libraries required for the game to run |
| README.md | Markdown document | Project description document, including project introduction, installation steps, game controls, etc. |
| .gitignore | Text file | Git ignore configuration, specifying files and directories that do not need to be tracked by Git |

##### Audio Resources

| File Name | Type | Function Description |
|--------|------|----------|
| audio/cafe_bgm.mp3 | Audio | Background music for the cafe scene |
| audio/hospital_bgm.mp3 | Audio | Background music for the abandoned hospital scene |
| audio/menu_bgm.mp3 | Audio | Background music for the main menu and dungeon selection interface |
| audio/open_gate.WAV | Audio | Door opening sound effect, played when the player opens the door |

##### Image Resources

| File Name | Type | Function Description |
|--------|------|----------|
| images/github.webp | Image | GitHub icon, used for project-related links |
| images/player_idle_down.png | Image | Player idle down animation frame |
| images/player_idle_left.png | Image | Player idle left animation frame |
| images/player_idle_right.png | Image | Player idle right animation frame |
| images/player_idle_up.png | Image | Player idle up animation frame |
| images/player_walk1.png | Image | Player walk alternate animation frame 1 |
| images/player_walk3.png | Image | Player walk alternate animation frame 3 |
| images/player_walk_down.png | Image | Player walk down animation frame |
| images/player_walk_left.png | Image | Player walk left animation frame |
| images/player_walk_right.png | Image | Player walk right animation frame |
| images/player_walk_up.png | Image | Player walk up animation frame |

##### Scene Files

| File Name | Type | Function Description |
|--------|------|----------|
| scenes/hospital.py | Python code | Implementation of the abandoned hospital scene, including scene drawing, collision detection, and interaction logic |
| scenes/cafe.py | Python code | Implementation of the cafe scene, including scene drawing, collision detection, and interaction logic |

##### UI Component Files

| File Name | Type | Function Description |
|--------|------|----------|
| ui/dialog.py | Python code | Implementation of the dialog system, used to display game plot and character dialog |
| ui/ui_components.py | Python code | General UI component library, including implementations of buttons, sliders, menus, and other UI elements |

##### Utility Function Files

| File Name | Type | Function Description |
|--------|------|----------|
| utils/collision.py | Python code | Collision detection tool, used to detect collisions between players and game objects |

##### Test Files

| File Name | Type | Function Description |
|--------|------|----------|
| test/游戏所有废案/ | Directory | Discarded history during game development, including discarded design schemes and code |
| test/游戏所有废案/介绍.md | Markdown document | Introduction and explanation of discarded history |
| test/游戏所有废案/scenes/ | Directory | Discarded scene code |
| test/游戏所有废案/ui/ | Directory | Discarded UI component code |
| test/游戏所有废案/utils/ | Directory | Discarded utility function code |

#### Development Team

| Role | Member | Responsibility |
|------|------|------|
| Core Developer | 黄 | Code implementation, feature development |
| UI Designer | 凉乞钞_official | UI style, animation editing |
| Main Planner | 矢车菊 | Gameplay design, plot architecture |
| Gameplay Consultant | 坚林 | Adventure puzzle gameplay suggestions |
| Art Director | 沫沫 | Character/scene art style definition |
| Visual Design | 筱 | UI interface design, color matching |
| Resource Production | 京华 | Image resource drawing, material processing |

#### Version History

- **v1.0.0** (2025-11-24)：Initial version release, including abandoned hospital scene
- **v1.0.1** (2025-11-25)：Fixed character movement bugs, optimized animation effects
- **v1.0.2** (2025-11-30)：Added cafe scene, expanded plot
- **v1.0.3** (2025-12-02)：Optimized game performance, fixed collision detection issues
- **v1.0.4** (2025-12-03)：Added game settings function, support for adjusting resolution and frame rate
- **v1.0.5** (2025-12-05)：Fixed UI display issues, optimized game experience
- **v1.1.0** (2025-12-06)：Optimized resource file structure, organized audio and image files into dedicated directories

#### Game Development Discarded History

##### Discarded Plan 1: Modular Split Scheme

**Scheme Overview**：
Split the game into multiple independent small modules, each responsible for specific functions such as scene rendering, character control, UI interaction, etc. The purpose is to improve development efficiency and facilitate independent development and testing by team members.

**Expected Advantages**：
- Facilitates team collaboration, reduces code conflicts
- Modular design is easy to maintain and extend
- Independent testing improves code quality
- Modules can be flexibly replaced according to needs

**Actual Challenges**：
- Complex interface design between modules, high integration difficulty
- Performance overhead caused by cross-module calls
- Increased team communication costs
- Complex module dependency relationships, long build time

**Reasons for Abandonment**：
The split modules had display issues during actual operation, causing the game to fail to start normally. Specifically, the module loading order was chaotic, resource dependency relationships were incorrect, and eventually the game crashed.

**Abandonment Date**：December 3, 2025

##### Lessons Learned

1. **Modular design requires caution**：Before conducting modular splitting, fully consider the dependencies and interface design between modules
2. **Test-driven development**：Each module needs to undergo sufficient unit testing and integration testing during development
3. **Progressive splitting**：Avoid large-scale splitting at once, it is recommended to adopt a progressive splitting strategy and gradually verify the splitting effect
4. **Documentation first**：Before conducting modular design, detailed design documents must be written to clarify the interfaces and dependencies between modules
5. **Team collaboration mechanism**：Establish an effective team collaboration mechanism to ensure good communication between module developers

#### Contribution Guide

1. **Fork the repository**：Fork the project to your own account on GitHub
2. **Create a branch**：Create a new feature branch from the main branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Develop features**：Implement new features or fix bugs
4. **Commit code**：Write clear commit messages
   ```bash
   git commit -m "feat: Add new feature description"
   ```
5. **Push branch**：Push the code to your own fork repository
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create Pull Request**：Submit a Pull Request on GitHub, describing your changes

#### Code of Conduct

- Respect team members, communicate friendly
- Follow PEP 8 code style
- Write clear code comments
- Ensure the code can run normally before submission
- Do not submit files unrelated to the game

#### License

This project adopts a custom license, see the LICENSE file for details. The license content includes different terms for light use and heavy use, aiming to balance open source sharing and protection of original work rights.

#### Contact Information

- **GitHub Issues**：[Submit Issues](https://github.com/Hello-ABYDOS-27/EF-ADH-main/issues)
- **Development Team Email**：[efadh-team@example.com](mailto:efadh-team@example.com) (Example)

#### Acknowledgments

Thank you to all team members and test players who have contributed to the project！

---

## 日本語

### 学校脱出スクリプト

#### プロジェクト紹介

**学校脱出スクリプト**はPygameで開発された2Dアドベンチャーパズルゲームです。学校主催のボランティア活動に参加していた中学生が、偶然廃墟病院に迷い込み、プレイヤーは場所を探索し、謎を解いて最終的に脱出するストーリーです。

#### ゲームの特徴

- 🎮 **操作が簡単**：WASDでキャラクターを移動、Eキーでインタラクション
- 🎨 **美しい2Dピクセルスタイル**：精心設計されたゲームシーンとキャラクターアニメーション
- 🎵 **没入型サウンド**：各シーンに独自のBGMと効果音が設定
- 📖 **豊富なストーリー**：複数のストーリーラインと隠しコンテンツを含む
- 🏠 **多様なシーン**：廃墟病院からカフェまで、各シーンに独自の謎と挑戦が待つ
- ⚙️ **設定可能なゲーム設定**：解像度、フレームレート、ショートカットキーの調整が可能

#### 技術スタック

- **開発言語**：Python 3.11
- **ゲームエンジン**：Pygame
- **バージョン管理**：Git
- **コードスタイル**：PEP 8

#### ダウンロードと実行

##### ゲームのダウンロード

1. **Releasesページからダウンロード**：
   - GitHubリポジトリにアクセス：[https://github.com/Hello-ABYDOS-27/EF-ADH-main](https://github.com/Hello-ABYDOS-27/EF-ADH-main)
   - 右側の赤い枠でマークされた"Releases"セクションを見つける
   - "Create a new release"をクリック（既にリリースされている場合は最新バージョンが表示）
   - 最新バージョンのゲームzipファイルをダウンロード
   - ダウンロード後、zipファイルをゲームをインストールしたい場所に解凍

##### ゲームの実行

1. **ゲームディレクトリを開く**：
   - 解凍後、解凍されたフォルダ`EF-ADH-main`に入る

2. **ゲームを実行する**：
   - `game.exe`ファイルを見つけてダブルクリック
   - ゲームが自動的に起動

##### 注意事項

- ゲームはWindowsシステムのみをサポート
- システムにDirectXまたはOpenGLグラフィックスライブラリがインストールされていることを確認
- 初回実行時はリソースの読み込みに時間がかかる場合がある
- 最適なゲーム体験のため、他のシステムリソースを大量に消費するプログラムは閉じておくことを推奨

#### ゲーム操作

| キー | 機能 |
|------|------|
| W | 上に移動 |
| A | 左に移動 |
| S | 下に移動 |
| D | 右に移動 |
| E | ドアを開く/インタラクション |
| スペース | ゲームを一時停止 |
| ESC | メニューを閉じる/戻る |

#### ゲームシーン

##### 1. 廃墟病院
- ゲームの初期シーン
- 病院内部を探索し、脱出の手がかりを見つける
- ドアの謎を解いて新しい章を開く

##### 2. カフェ
- 廃墟病院の門を通って到着するシーン
- NPCと対話して、より多くのストーリー情報を入手
- 新しい挑戦と謎を解き明かす

##### 3. 結婚式場（更新予定）
- 今後の更新でオープン予定の新シーン
- より多くのエキサイティングなストーリーと謎が待っている

#### プロジェクト構造

```
EF-ADH-main/
├── main.py                 # ゲームメインプログラム
├── requirements.txt         # プロジェクト依存関係
├── .gitignore              # Git無視設定
├── README.md               # プロジェクトドキュメント
├── audio/                  # オーディオリソース
│   ├── cafe_bgm.mp3        # カフェのBGM
│   ├── hospital_bgm.mp3    # 廃墟病院のBGM
│   ├── menu_bgm.mp3        # メインメニューのBGM
│   └── open_gate.WAV       # ドアを開く効果音
├── images/                 # 画像リソース
│   ├── github.webp         # GitHubアイコン
│   ├── player_idle_down.png # プレイヤーの下向きアイドルアニメーションフレーム
│   ├── player_idle_left.png # プレイヤーの左向きアイドルアニメーションフレーム
│   ├── player_idle_right.png # プレイヤーの右向きアイドルアニメーションフレーム
│   ├── player_idle_up.png  # プレイヤーの上向きアイドルアニメーションフレーム
│   ├── player_walk1.png    # プレイヤーの歩行予備アニメーションフレーム1
│   ├── player_walk3.png    # プレイヤーの歩行予備アニメーションフレーム3
│   ├── player_walk_down.png # プレイヤーの下向き歩行アニメーションフレーム
│   ├── player_walk_left.png # プレイヤーの左向き歩行アニメーションフレーム
│   ├── player_walk_right.png # プレイヤーの右向き歩行アニメーションフレーム
│   └── player_walk_up.png  # プレイヤーの上向き歩行アニメーションフレーム
├── test/                   # テスト関連ファイル
│   └── 游戏所有废案/        # ゲーム開発の廃案履歴
├── scenes/                 # シーンファイル
│   ├── hospital.py         # 廃墟病院シーン
│   └── cafe.py            # カフェシーン
├── ui/                     # UIコンポーネント
│   ├── dialog.py           # ダイアログシステム
│   └── ui_components.py    # UIコンポーネントライブラリ
└── utils/                  # ユーティリティ関数
    └── collision.py        # 衝突検出
```

#### ファイル機能説明

##### コアファイル

| ファイル名 | タイプ | 機能説明 |
|--------|------|----------|
| main.py | Pythonコード | ゲームのメインプログラムファイルで、ゲームの初期化、メインループ、イベント処理、シーン管理を含む |
| requirements.txt | テキストファイル | プロジェクトの依存関係リストで、ゲームの実行に必要なすべてのPythonライブラリを含む |
| README.md | Markdownドキュメント | プロジェクトの説明ドキュメントで、プロジェクトの概要、インストール手順、ゲーム操作などの情報を含む |
| .gitignore | テキストファイル | Gitの無視設定で、Gitで追跡する必要のないファイルとディレクトリを指定する |

##### オーディオリソース

| ファイル名 | タイプ | 機能説明 |
|--------|------|----------|
| audio/cafe_bgm.mp3 | オーディオ | カフェシーンのBGM |
| audio/hospital_bgm.mp3 | オーディオ | 廃墟病院シーンのBGM |
| audio/menu_bgm.mp3 | オーディオ | メインメニューとダンジョン選択画面のBGM |
| audio/open_gate.WAV | オーディオ | プレイヤーがドアを開くときに再生されるドアを開く効果音 |

##### 画像リソース

| ファイル名 | タイプ | 機能説明 |
|--------|------|----------|
| images/github.webp | 画像 | プロジェクト関連リンクに使用されるGitHubアイコン |
| images/player_idle_down.png | 画像 | プレイヤーの下向きアイドルアニメーションフレーム |
| images/player_idle_left.png | 画像 | プレイヤーの左向きアイドルアニメーションフレーム |
| images/player_idle_right.png | 画像 | プレイヤーの右向きアイドルアニメーションフレーム |
| images/player_idle_up.png | 画像 | プレイヤーの上向きアイドルアニメーションフレーム |
| images/player_walk1.png | 画像 | プレイヤーの歩行予備アニメーションフレーム1 |
| images/player_walk3.png | 画像 | プレイヤーの歩行予備アニメーションフレーム3 |
| images/player_walk_down.png | 画像 | プレイヤーの下向き歩行アニメーションフレーム |
| images/player_walk_left.png | 画像 | プレイヤーの左向き歩行アニメーションフレーム |
| images/player_walk_right.png | 画像 | プレイヤーの右向き歩行アニメーションフレーム |
| images/player_walk_up.png | 画像 | プレイヤーの上向き歩行アニメーションフレーム |

##### シーンファイル

| ファイル名 | タイプ | 機能説明 |
|--------|------|----------|
| scenes/hospital.py | Pythonコード | 廃墟病院シーンの実装で、シーンの描画、衝突検出、インタラクションロジックを含む |
| scenes/cafe.py | Pythonコード | カフェシーンの実装で、シーンの描画、衝突検出、インタラクションロジックを含む |

##### UIコンポーネントファイル

| ファイル名 | タイプ | 機能説明 |
|--------|------|----------|
| ui/dialog.py | Pythonコード | ダイアログシステムの実装で、ゲームのストーリーとキャラクターの会話を表示するために使用 |
| ui/ui_components.py | Pythonコード | 汎用UIコンポーネントライブラリで、ボタン、スライダー、メニューなどのUI要素の実装を含む |

##### ユーティリティ関数ファイル

| ファイル名 | タイプ | 機能説明 |
|--------|------|----------|
| utils/collision.py | Pythonコード | 衝突検出ツールで、プレイヤーとゲームオブジェクト間の衝突を検出するために使用 |

##### テストファイル

| ファイル名 | タイプ | 機能説明 |
|--------|------|----------|
| test/游戏所有废案/ | ディレクトリ | ゲーム開発中の廃案履歴で、廃棄された設計方案とコードを含む |
| test/游戏所有废案/介绍.md | Markdownドキュメント | 廃案履歴の紹介と説明 |
| test/游戏所有废案/scenes/ | ディレクトリ | 廃棄されたシーンコード |
| test/游戏所有废案/ui/ | ディレクトリ | 廃棄されたUIコンポーネントコード |
| test/游戏所有废案/utils/ | ディレクトリ | 廃棄されたユーティリティ関数コード |

#### 開発チーム

| 役割 | メンバー | 責任 |
|------|------|------|
| コア開発者 | 黄 | コード実装、機能開発 |
| UIデザイナー | 凉乞钞_official | UIスタイル、アニメーション編集 |
| メインプランナー | 矢车菊 | ゲームプレイ設計、ストーリー構築 |
| ゲームプレイコンサルタント | 坚林 | アドベンチャーパズルゲームプレイの提案 |
| アートディレクター | 沫沫 | キャラクター/シーンのアートスタイル定義 |
| ビジュアルデザイン | 筱 | UIインターフェース設計、カラーマッチング |
| リソース制作 | 京华 | 画像リソースの描画、素材処理 |

#### バージョン履歴

- **v1.0.0** (2025-11-24)：初期バージョンリリース、廃墟病院シーンを含む
- **v1.0.1** (2025-11-25)：キャラクターの移動バグを修正、アニメーション効果を最適化
- **v1.0.2** (2025-11-30)：カフェシーンを追加、ストーリーを拡張
- **v1.0.3** (2025-12-02)：ゲームパフォーマンスを最適化、衝突検出問題を修正
- **v1.0.4** (2025-12-03)：ゲーム設定機能を追加、解像度とフレームレートの調整をサポート
- **v1.0.5** (2025-12-05)：UI表示問題を修正、ゲーム体験を最適化
- **v1.1.0** (2025-12-06)：リソースファイル構造を最適化、オーディオと画像ファイルを専用ディレクトリに整理

#### ゲーム開発廃案履歴

##### 廃案一：モジュール化分割方案

**方案概要**：
ゲームを複数の独立した小さなモジュールに分割し、各モジュールはシーンレンダリング、キャラクターコントロール、UIインタラクションなどの特定の機能を担当。チームメンバーの独立開発とテストを容易にし、開発効率を向上させることを目的とする。

**予期される利点**：
- チーム協力を容易にし、コード衝突を削減
- モジュール化設計は保守と拡張が容易
- 独立テストによりコード品質が向上
- ニーズに応じてモジュールを柔軟に置き換え可能

**実際の課題**：
- モジュール間のインターフェース設計が複雑で、統合難度が高い
- クロスモジュール呼び出しによるパフォーマンスオーバーヘッド
- チームのコミュニケーションコストが増加
- モジュール依存関係が複雑で、構築時間が長い

**廃棄理由**：
分割されたモジュールは実際の運行中に表示問題が発生し、ゲームが正常に起動できなくなった。具体的には、モジュールのロード順序が混乱し、リソースの依存関係が誤っているため、最終的にゲームがクラッシュした。

**廃棄日**：2025年12月3日

##### 教訓

1. **モジュール化設計には注意が必要**：モジュール化分割を行う前に、モジュール間の依存関係とインターフェース設計を十分に考慮する必要がある
2. **テスト駆動開発**：各モジュールは開発過程で十分な単体テストと統合テストを受ける必要がある
3. **漸進的な分割**：一度に大規模な分割を避け、漸進的な分割戦略を採用して、分割効果を段階的に検証することを推奨
4. **ドキュメント先行**：モジュール化設計を行う前に、詳細な設計ドキュメントを作成し、モジュール間のインターフェースと依存関係を明確にする必要がある
5. **チーム協力メカニズム**：効果的なチーム協力メカニズムを確立し、モジュール開発者間の良好なコミュニケーションを確保する

#### 貢献ガイド

1. **リポジトリをフォーク**：GitHubでプロジェクトを自分のアカウントにフォーク
2. **ブランチを作成**：mainブランチから新しい機能ブランチを作成
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **機能を開発**：新機能を実装またはバグを修正
4. **コードをコミット**：明確なコミットメッセージを書く
   ```bash
   git commit -m "feat: 新機能の説明を追加"
   ```
5. **ブランチをプッシュ**：コードを自分のフォークリポジトリにプッシュ
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Pull Requestを作成**：GitHubでPull Requestを提出し、変更内容を説明

#### 行動規範

- チームメンバーを尊重し、友好的にコミュニケーション
- PEP 8コードスタイルに従う
- 明確なコードコメントを書く
- 提出前にコードが正常に実行できることを確認
- ゲームと無関係なファイルを提出しない

#### ライセンス

本プロジェクトはカスタムライセンスを採用し、詳細はLICENSEファイルを参照。ライセンス内容には軽度使用と重度使用の異なる条項が含まれ、オープンソース共有とオリジナル作品の権利保護のバランスを図ることを目的とする。

#### 連絡先

- **GitHub Issues**：[問題を提出](https://github.com/Hello-ABYDOS-27/EF-ADH-main/issues)
- **開発チームメール**：[efadh-team@example.com](mailto:efadh-team@example.com)（例）

#### 謝辞

プロジェクトに貢献したすべてのチームメンバーとテストプレイヤーに感謝します！

---

## 中文-文言

### 逃學劇本

#### 項目敘略

**逃學劇本**者，乃用Pygame所造之2D冒險解謎遊戲也。其述一學子，因參與校中公益，誤入廢棄醫院。玩家當探索場景，解破謎題，終得逃脫困境。

#### 遊戲之善

- 🎮 **操作簡便**：以WASD移動角色，E鍵互動
- 🎨 **像素精美**：場景與角色動畫，皆精心設計
- 🎵 **音效沉浸**：每場景各有獨特之背景音樂與音效
- 📖 **劇情豐富**：含多線劇情與隱藏內容
- 🏠 **場景多樣**：自廢醫至咖啡館，每處皆有獨特之謎題與挑戰
- ⚙️ **設置可調**：支持調整解析度、幀率與快捷鍵

#### 技術之棧

- **開發語言**：Python 3.11
- **遊戲引擎**：Pygame
- **版本控制**：Git
- **代碼風格**：PEP 8

#### 下載與運行

##### 下載遊戲

1. **自Releases頁下載**：
   - 訪問GitHub倉庫：[https://github.com/Hello-ABYDOS-27/EF-ADH-main](https://github.com/Hello-ABYDOS-27/EF-ADH-main)
   - 覓右侧紅框所標"Releases"之處
   - 點擊"Create a new release"（若已發布，則顯示最新版本）
   - 下載最新版本之遊戲壓縮包
   - 下載畢，解壓至所欲安裝之處

##### 運行遊戲

1. **開遊戲目錄**：
   - 解壓後，入解壓所得文件夾`EF-ADH-main`

2. **運行遊戲**：
   - 覓`game.exe`文件，雙擊之
   - 遊戲自動啟動

##### 注意事項

- 遊戲僅支持Windows系統
- 確保系統已裝DirectX或OpenGL圖形庫
- 首次運行，或需時載入資源
- 欲得最佳體驗，宜關閉其他耗費資源之程序

#### 遊戲操作

| 按鍵 | 功能 |
|------|------|
| W | 向上移動 |
| A | 向左移動 |
| S | 向下移動 |
| D | 向右移動 |
| E | 開門/互動 |
| 空格 | 暫停遊戲 |
| ESC | 關閉菜單/返回 |

#### 遊戲場景

##### 1. 廢棄醫院
- 遊戲初始之場景
- 探索醫院內部，尋覓逃脫線索
- 解破大門之謎，開啟新章

##### 2. 咖啡館
- 穿過廢醫大門後所至之場景
- 與NPC互動，獲取更多劇情信息
- 解鎖新挑戰與謎題

##### 3. 婚禮現場（待更新）
- 後續更新將開放之新場景
- 更多精彩劇情與謎題，待君探索

#### 項目結構

```
EF-ADH-main/
├── main.py                 # 遊戲主程序
├── requirements.txt         # 項目依賴
├── .gitignore              # Git忽略配置
├── README.md               # 項目說明文檔
├── audio/                  # 音頻資源
│   ├── cafe_bgm.mp3        # 咖啡館背景音樂
│   ├── hospital_bgm.mp3    # 廢棄醫院背景音樂
│   ├── menu_bgm.mp3        # 主菜單背景音樂
│   └── open_gate.WAV       # 開門音效
├── images/                 # 圖片資源
│   ├── github.webp         # GitHub圖標
│   ├── player_idle_down.png # 玩家向下站立動畫幀
│   ├── player_idle_left.png # 玩家向左站立動畫幀
│   ├── player_idle_right.png # 玩家向右站立動畫幀
│   ├── player_idle_up.png  # 玩家向上站立動畫幀
│   ├── player_walk1.png    # 玩家行走備用動畫幀1
│   ├── player_walk3.png    # 玩家行走備用動畫幀3
│   ├── player_walk_down.png # 玩家向下行走動畫幀
│   ├── player_walk_left.png # 玩家向左行走動畫幀
│   ├── player_walk_right.png # 玩家向右行走動畫幀
│   └── player_walk_up.png  # 玩家向上行走動畫幀
├── test/                   # 測試相關文件
│   └── 遊戲所有廢案/        # 遊戲開發廢案歷史
├── scenes/                 # 場景文件
│   ├── hospital.py         # 廢棄醫院場景
│   └── cafe.py            # 咖啡館場景
├── ui/                     # UI組件
│   ├── dialog.py           # 對話框系統
│   └── ui_components.py    # UI組件庫
└── utils/                  # 工具函數
    └── collision.py        # 碰撞檢測
```

#### 文件功能敘略

##### 核心文件

| 文件名 | 類型 | 功能敘略 |
|--------|------|----------|
| main.py | Python代碼 | 遊戲主程序，含初始化、主循環、事件處理與場景管理 |
| requirements.txt | 文本文件 | 項目依賴列表，含遊戲運行所需之所有Python庫 |
| README.md | Markdown文檔 | 項目說明，含概述、安裝步驟、遊戲操作等信息 |
| .gitignore | 文本文件 | Git忽略配置，指定不需跟蹤之文件與目錄 |

##### 音頻資源

| 文件名 | 類型 | 功能敘略 |
|--------|------|----------|
| audio/cafe_bgm.mp3 | 音頻 | 咖啡館場景之背景音樂 |
| audio/hospital_bgm.mp3 | 音頻 | 廢棄醫院場景之背景音樂 |
| audio/menu_bgm.mp3 | 音頻 | 主菜單與副本選擇界面之背景音樂 |
| audio/open_gate.WAV | 音頻 | 開門音效，用於玩家開門之時 |

##### 圖片資源

| 文件名 | 類型 | 功能敘略 |
|--------|------|----------|
| images/github.webp | 圖片 | GitHub圖標，用於項目相關鏈接 |
| images/player_idle_down.png | 圖片 | 玩家向下站立之idle動畫幀 |
| images/player_idle_left.png | 圖片 | 玩家向左站立之idle動畫幀 |
| images/player_idle_right.png | 圖片 | 玩家向右站立之idle動畫幀 |
| images/player_idle_up.png | 圖片 | 玩家向上站立之idle動畫幀 |
| images/player_walk1.png | 圖片 | 玩家行走之備用動畫幀1 |
| images/player_walk3.png | 圖片 | 玩家行走之備用動畫幀3 |
| images/player_walk_down.png | 圖片 | 玩家向下行走之動畫幀 |
| images/player_walk_left.png | 圖片 | 玩家向左行走之動畫幀 |
| images/player_walk_right.png | 圖片 | 玩家向右行走之動畫幀 |
| images/player_walk_up.png | 圖片 | 玩家向上行走之動畫幀 |

##### 場景文件

| 文件名 | 類型 | 功能敘略 |
|--------|------|----------|
| scenes/hospital.py | Python代碼 | 廢棄醫院場景之實現，含繪製、碰撞檢測與互動邏輯 |
| scenes/cafe.py | Python代碼 | 咖啡館場景之實現，含繪製、碰撞檢測與互動邏輯 |

##### UI組件文件

| 文件名 | 類型 | 功能敘略 |
|--------|------|----------|
| ui/dialog.py | Python代碼 | 對話框系統之實現，用於顯示遊戲劇情與角色對話 |
| ui/ui_components.py | Python代碼 | 通用UI組件庫，含按鈕、滑塊、菜單等UI元素之實現 |

##### 工具函數文件

| 文件名 | 類型 | 功能敘略 |
|--------|------|----------|
| utils/collision.py | Python代碼 | 碰撞檢測工具，用於檢測玩家與遊戲對象間之碰撞 |

##### 測試文件

| 文件名 | 類型 | 功能敘略 |
|--------|------|----------|
| test/遊戲所有廢案/ | 目錄 | 遊戲開發過程中之廢案歷史，含廢棄之設計方案與代碼 |
| test/遊戲所有廢案/介紹.md | Markdown文檔 | 廢案歷史之介紹與說明 |
| test/遊戲所有廢案/scenes/ | 目錄 | 廢棄之場景代碼 |
| test/遊戲所有廢案/ui/ | 目錄 | 廢棄之UI組件代碼 |
| test/遊戲所有廢案/utils/ | 目錄 | 廢棄之工具函數代碼 |

#### 開發團隊

| 角色 | 成員 | 職責 |
|------|------|------|
| 核心開發者 | 黄 | 代碼實現、功能開發 |
| UI設計師 | 凉乞钞_official | UI樣式、動畫編輯 |
| 主策劃 | 矢车菊 | 遊戲玩法設計、劇情架構 |
| 玩法顧問 | 坚林 | 冒險解謎玩法建議 |
| 美術負責人 | 沫沫 | 角色/場景美術風格定義 |
| 視覺設計 | 筱 | UI界面設計、顏色搭配 |
| 資源製作 | 京华 | 圖片資源繪製、素材處理 |

#### 版本歷史

- **v1.0.0** (2025-11-24)：初始版本發布，含廢棄醫院場景
- **v1.0.1** (2025-11-25)：修復角色移動bug，優化動畫效果
- **v1.0.2** (2025-11-30)：新增咖啡館場景，擴展劇情
- **v1.0.3** (2025-12-02)：優化遊戲性能，修復碰撞檢測問題
- **v1.0.4** (2025-12-03)：新增遊戲設置功能，支持調整解析度和幀率
- **v1.0.5** (2025-12-05)：修復UI顯示問題，優化遊戲體驗
- **v1.1.0** (2025-12-06)：優化資源文件結構，將音頻和圖片文件整理到專門目錄

#### 遊戲開發廢案歷史

##### 廢案一：模塊化拆分方案

**方案概述**：
將遊戲拆分為多個獨立之小模塊，每模塊負責特定功能，如場景渲染、角色控制、UI互動等。目的在提高開發效率，方便團隊成員獨立開發與測試。

**預期優勢**：
- 便於團隊協作，降低代碼衝突
- 模塊化設計便於維護與擴展
- 獨立測試，提高代碼質量
- 可據需求靈活替換模塊

**實際挑戰**：
- 模塊間接口設計複雜，集成難度大
- 跨模塊調用導致性能開銷
- 團隊溝通成本增加
- 模塊依賴關係複雜，構建時間長

**廢除原因**：
拆分後之模塊在實際運行中出現顯示問題，導致遊戲無法正常啟動。具體表現為模塊載入順序混亂，資源依賴關係錯誤，最終導致遊戲崩潰。

**廢除日期**：2025年12月3日

##### 經驗教訓

1. **模塊化設計需謹慎**：於進行模塊化拆分前，必須充分考慮模塊間之依賴關係與接口設計
2. **測試驅動開發**：每模塊在開發過程中，皆需進行充分之單元測試與集成測試
3. **漸進式拆分**：避免一次性大規模拆分，建議採用漸進式拆分策略，逐步驗證拆分效果
4. **文檔先行**：於進行模塊化設計前，必須編寫詳細之設計文檔，明確模塊間之接口與依賴關係
5. **團隊協作機制**：建立有效之團隊協作機制，確保模塊開發人員之間之良好溝通

#### 貢獻指南

1. **Fork 倉庫**：於GitHub上fork項目至自己之賬號
2. **創建分支**：自main分支創建新之功能分支
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **開發功能**：實現新功能或修復bug
4. **提交代碼**：編寫清晰之提交信息
   ```bash
   git commit -m "feat: 添加新功能描述"
   ```
5. **Push 分支**：將代碼推送到自己之fork倉庫
   ```bash
   git push origin feature/your-feature-name
   ```
6. **創建 Pull Request**：於GitHub上提交Pull Request，描述你的更改

#### 行為準則

- 尊重團隊成員，友好溝通
- 遵循PEP 8代碼風格
- 編寫清晰之代碼註釋
- 提交前確保代碼可以正常運行
- 勿提交與遊戲無關之文件

#### 許可證

本項目採用自定義許可證，詳見LICENSE文件。許可證內容包括輕度使用與重度使用之不同條款，旨在平衡開源共享與保護原創作品權益。

#### 聯繫方式

- **GitHub Issues**：[提交問題](https://github.com/Hello-ABYDOS-27/EF-ADH-main/issues)
- **開發團隊郵箱**：[efadh-team@example.com](mailto:efadh-team@example.com)（示例）

#### 鳴謝

感謝所有為項目做出貢獻之團隊成員與測試玩家！

---

**© 2025 逃離學校劇本開發團隊**

*享受遊戲，享受開發！*