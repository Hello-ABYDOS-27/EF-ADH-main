# Escape School Script

## Language Versions

This project is available in multiple languages. You can find the translated README files in the `docx` directory:

- [中文-简体](docx/README_zh-CN.md)
- [中文-繁体](docx/README_zh-TW.md)
- [English](README.md) (Current)
- [日本語](docx/README_ja.md)
- [中文-文言](docx/README_zh-Classic.md)

## Project Introduction

**Escape School Script** is a 2D adventure puzzle game developed with Pygame. The game tells the story of a middle school student who accidentally arrives at an abandoned hospital during a school-organized charity event. Players need to explore scenes, solve puzzles, and ultimately escape from the predicament.

## Game Features

- 🎮 **Simple and easy-to-use controls**：Use WASD to move characters, E to interact
- 🎨 **Beautiful 2D pixel art style**：Carefully designed game scenes and character animations
- 🎵 **Immersive sound effects**：Each scene has unique background music and sound effects
- 📖 **Rich storyline**：Contains multiple storylines and hidden content
- 🏠 **Diverse scenes**：From abandoned hospitals to cafes, each scene has unique puzzles and challenges
- ⚙️ **Configurable game settings**：Support for adjusting resolution, frame rate, and shortcuts

## Tech Stack

- **Development Language**：Python 3.11
- **Game Engine**：Pygame
- **Version Control**：Git
- **Code Style**：PEP 8

## Project Structure

```
EF-ADH-main/
├── main.py                 # Game main program
├── requirements.txt         # Project dependencies
├── github_utils.py         # GitHub utility functions
├── server.py               # Server-related functionality
├── .gitignore              # Git ignore configuration
├── README.md               # Project documentation (English)
├── .editorconfig           # Editor configuration
├── .gitattributes          # Git attributes
├── .gitmodules             # Git submodules
├── docx/                   # Translated README files
│   ├── README_zh-CN.md     # Chinese (Simplified)
│   ├── README_zh-TW.md     # Chinese (Traditional)
│   ├── README_en.md        # English
│   ├── README_ja.md        # Japanese
│   └── README_zh-Classic.md # Classical Chinese
├── APP/                    # Application executables
│   ├── game_app.exe
│   ├── game_client.exe
│   ├── game_server.exe
│   └── package.py
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
│       ├── 介绍.md
│       ├── scenes/         # Discarded scene code
│       ├── ui/             # Discarded UI component code
│       └── utils/          # Discarded utility function code
├── .venv/                  # Virtual environment
└── __pycache__/            # Compiled Python files
```

## Installation and Run

### Prerequisites

- Python 3.11 or later
- Pygame library
- Windows system (for executable files)

### Running from Source

1. **Clone the repository**：
   ```bash
   git clone https://github.com/Hello-ABYDOS-27/EF-ADH-main.git
   cd EF-ADH-main
   ```

2. **Install dependencies**：
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**：
   ```bash
   python main.py
   ```

### Running from Executable (Windows only)

1. **Download the game**：
   - Visit the GitHub repository：[https://github.com/Hello-ABYDOS-27/EF-ADH-main](https://github.com/Hello-ABYDOS-27/EF-ADH-main)
   - Download the latest release from the Releases page
   - Extract the zip package to your desired location

2. **Run the game**：
   - Navigate to the extracted folder
   - Double-click `game.exe` to start the game

### Notes

- The game supports both development mode and executable mode
- Ensure your system has DirectX or OpenGL graphics libraries installed
- The first run may take some time to load resources
- It is recommended to close other programs that consume a lot of system resources for the best gaming experience

## Game Controls

| Key | Function |
|------|------|
| W | Move up |
| A | Move left |
| S | Move down |
| D | Move right |
| E | Open door/Interact |
| Space | Pause game |
| ESC | Close menu/Return |

## Game Scenes

### 1. Abandoned Hospital
- The initial scene of the game
- Explore the hospital interior, find escape clues
- Solve the door puzzle to start a new chapter

### 2. Cafe
- The scene reached after passing through the abandoned hospital gate
- Interact with NPCs to get more plot information
- Unlock new challenges and puzzles

### 3. Wedding Scene (Coming Soon)
- A new scene to be opened in future updates
- More exciting plots and puzzles to explore

## Development Team

| Role | Member | Responsibility |
|------|------|------|
| Core Developer | 黄 | Code implementation, feature development |
| UI Designer | 凉乞钞_official | UI style, animation editing |
| Main Planner | 矢车菊 | Gameplay design, plot architecture |
| Gameplay Consultant | 坚林 | Adventure puzzle gameplay suggestions |
| Art Director | 沫沫 | Character/scene art style definition |
| Visual Design | 筱 | UI interface design, color matching |
| Resource Production | 京华 | Image resource drawing, material processing |

## Version History

- **v1.0.0** (2025-11-24)：Initial version release, including abandoned hospital scene
- **v1.0.1** (2025-11-25)：Fixed character movement bugs, optimized animation effects
- **v1.0.2** (2025-11-30)：Added cafe scene, expanded plot
- **v1.0.3** (2025-12-02)：Optimized game performance, fixed collision detection issues
- **v1.0.4** (2025-12-03)：Added game settings function, support for adjusting resolution and frame rate
- **v1.0.5** (2025-12-05)：Fixed UI display issues, optimized game experience
- **v1.1.0** (2025-12-06)：Optimized resource file structure, organized audio and image files into dedicated directories
- **v1.1.1** (2025-12-06)：Added multi-language README files
- **v1.1.2** (2025-12-06)：Added github_utils.py and server.py, updated project structure

## Contribution Guide

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

## Code of Conduct

- Respect team members, communicate friendly
- Follow PEP 8 code style
- Write clear code comments
- Ensure the code can run normally before submission
- Do not submit files unrelated to the game

## License

This project adopts a custom license, see the LICENSE file for details. The license content includes different terms for light use and heavy use, aiming to balance open source sharing and protection of original work rights.

## Contact Information

- **GitHub Issues**：[Submit Issues](https://github.com/Hello-ABYDOS-27/EF-ADH-main/issues)
- **Development Team Email**：[efadh-team@example.com](mailto:efadh-team@example.com) (Example)

---

**© 2025 Escape School Script Development Team**

*Enjoy the game, enjoy the development！*
