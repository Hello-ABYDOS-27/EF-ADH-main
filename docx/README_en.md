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

**© 2025 Escape School Script Development Team**

*Enjoy the game, enjoy the development！*
