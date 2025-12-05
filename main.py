import pygame
import sys
import math

# 初始化Pygame与音频模块
pygame.init()
pygame.mixer.init()  # 初始化音频，必须在加载音乐前调用

# 核心配置（保留原有所有设置）
DEFAULT_WIDTH = 1366
DEFAULT_HEIGHT = 768
DEFAULT_FPS = 60
current_fps = DEFAULT_FPS
screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("逃离学校剧本")

# 颜色定义（完全保留原有，新增滑杆相关颜色）
BG_COLOR = (20, 20, 20)
MENU_BG = (40, 40, 40)
BUTTON_COLOR = (80, 80, 80)
BUTTON_HOVER = (120, 120, 120)
TEXT_COLOR = (255, 255, 255)
SELECTED_COLOR = (180, 100, 100)
RESET_BTN_COLOR = (100, 80, 180)
RESET_BTN_HOVER = (140, 120, 220)
GRASS_COLOR_1 = (34, 139, 34)
GRASS_COLOR_2 = (22, 107, 22)
DIRT_COLOR_1 = (139, 69, 19)
DIRT_COLOR_2 = (101, 67, 33)
ROAD_COLOR = (0, 0, 0)
ROAD_EDGE_COLOR = (255, 255, 0)
ROAD_CENTER_COLOR = (255, 255, 255)
DIALOG_BG = (50, 50, 60)
PAUSE_MASK_COLOR = (0, 0, 0, 120)
PLAYER_DEFAULT_COLOR = (255, 100, 100)
NPC_DEFAULT_COLOR = (100, 200, 100)
WALL_COLOR = (100, 100, 100)
GATE_COLOR = (150, 75, 0)
GATE_OPEN_COLOR = (120, 60, 0)
CAFE_FLOOR_COLOR = (139, 69, 19)
CAFE_STREET_COLOR = (128, 128, 128)
CAFE_WALL_COLOR = (160, 82, 45)
CAFE_GATE_COLOR = (210, 180, 140)
CAFE_GATE_OPEN_COLOR = (245, 222, 179)
CAFE_GATE_BORDER = (139, 69, 19)
SLIDER_BG_COLOR = (60, 60, 60)    # 新增：滑杆背景色
SLIDER_FILL_COLOR = (180, 180, 0) # 新增：滑杆填充色
SLIDER_THUMB_COLOR = (255, 255, 255) # 新增：滑杆滑块色
SLIDER_THUMB_HOVER_COLOR = (255, 100, 100) # 新增：滑块悬停色

# 字体设置（完全保留原有）
try:
    menu_font = pygame.font.SysFont("SimHei", 48)
    option_font = pygame.font.SysFont("SimHei", 36)
    small_font = pygame.font.SysFont("SimHei", 28)
    dialog_font = pygame.font.SysFont("SimHei", 24)
    pause_font = pygame.font.SysFont("SimHei", 72)
except:
    menu_font = pygame.font.SysFont(None, 48)
    option_font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 28)
    dialog_font = pygame.font.SysFont(None, 24)
    pause_font = pygame.font.SysFont(None, 72)

# 游戏状态枚举（完全保留原有）
class GameState:
    MAIN_MENU = 0
    COPY_SELECT = 1
    HOSPITAL = 2
    CAFE = 3
    SETTINGS = 4
    GAME_INFO = 5
    DIALOG = 6
    QUIT_CONFIRM = 7

# 全局状态变量（保留原有，新增滑杆交互变量，初始化settings_scroll_y和按键状态）
current_state = GameState.MAIN_MENU
is_paused = False
show_back_btn = False
gate_is_open = False
cafe_gate_is_open = False
gate_cooldown = 0
dialog_shown = False
editing_shortcut = None
info_scroll_y = 0
settings_scroll_y = 0  # 全局初始化，修复未定义问题
current_bgm = None  # 当前播放的BGM标识
bgm_volume = 0.3    # BGM音量（0.0-1.0）
sfx_volume = 0.5    # 音效音量（0.0-1.0）
dragging_bgm_slider = False  # 新增：BGM滑杆拖拽状态
dragging_sfx_slider = False  # 新增：音效滑杆拖拽状态
bgm_slider_rect_global = None  # 新增：全局存储BGM滑块位置
sfx_slider_rect_global = None  # 新增：全局存储音效滑块位置
# 新增：按键状态字典，用于跟踪按键按下状态，解决中文输入法问题
key_states = {
    'move_up': False,
    'move_down': False,
    'move_left': False,
    'move_right': False
}
# 新增：输入法提示显示状态
show_input_tip = True

# 新增：缓存变量，用于优化游戏信息和设置的绘制性能
game_info_cache = None  # 游戏信息页面的缓存表面
game_info_cache_resolution = None  # 缓存对应的分辨率
game_info_cache_scroll_y = None  # 缓存对应的滚动位置
settings_cache = None  # 设置页面的缓存表面
settings_cache_resolution = None  # 缓存对应的分辨率
settings_cache_scroll_y = None  # 缓存对应的滚动位置

# 动画相关状态变量
is_animating = False  # 动画是否正在播放
animation_progress = 0.0  # 动画进度，0.0到1.0
animation_speed = 0.03  # 动画速度，适中数值确保流畅度
prev_state = current_state  # 动画开始前的状态
next_state = current_state  # 动画结束后的状态
animation_direction = "right"  # 动画方向：right（向右滑出/滑入）

# 分辨率/帧率/快捷键配置（完全保留原有）
RESOLUTION_OPTIONS = [
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1366, 768),
    (1440, 900),
    (1600, 900),
    (1920, 1080),
    (2560, 1440),
    (3840, 2160)
]
current_res_idx = 3
FPS_OPTIONS = [30, 60, 90, 120, 144, 165, 240]
current_fps_idx = 1
GRID_SIZE = 50
FLOOR_BLOCK_SIZE = GRID_SIZE
FLOOR_WIDTH = 5000
FLOOR_HEIGHT = 5000
CAFE_MAP_WIDTH = 2000
CAFE_MAP_HEIGHT = 2000
CAFE_FLOOR_HEIGHT = 1800
CAFE_STREET_HEIGHT = 200
CAFE_WALL_THICKNESS = 10
CAFE_GATE_THICKNESS = CAFE_WALL_THICKNESS * 2

camera_x = 0
camera_y = 0

# 废弃医院/咖啡厅地图配置（完全保留原有）
GATE_WIDTH = GRID_SIZE * 3
GATE_HEIGHT = GRID_SIZE * 2
GATE_Y = FLOOR_HEIGHT * 2 // 3 - GRID_SIZE
GATE_X = (FLOOR_WIDTH - GATE_WIDTH) // 2
GATE_RECT = pygame.Rect(GATE_X, GATE_Y, GATE_WIDTH, GATE_HEIGHT)
GATE_TRIGGER_RANGE = 100
CAFE_WALL_Y = CAFE_FLOOR_HEIGHT
CAFE_WALL_RECT = pygame.Rect(
    0,
    CAFE_WALL_Y,
    CAFE_MAP_WIDTH,
    CAFE_WALL_THICKNESS
)
CAFE_GATE_WIDTH = 60
CAFE_GATE_X = (CAFE_MAP_WIDTH - CAFE_GATE_WIDTH) // 2
CAFE_GATE_Y = CAFE_WALL_Y - (CAFE_GATE_THICKNESS - CAFE_WALL_THICKNESS) // 2
CAFE_GATE_RECT = pygame.Rect(
    CAFE_GATE_X,
    CAFE_GATE_Y,
    CAFE_GATE_WIDTH,
    CAFE_GATE_THICKNESS
)
CAFE_GATE_TRIGGER_RANGE = 80
WALL_THICKNESS = 15
WALL_LEFT_RECT = pygame.Rect(
    0,
    GATE_Y + (GATE_HEIGHT - WALL_THICKNESS) // 2,
    GATE_X - 20,
    WALL_THICKNESS
)
WALL_RIGHT_RECT = pygame.Rect(
    GATE_X + GATE_WIDTH + 20,
    GATE_Y + (GATE_HEIGHT - WALL_THICKNESS) // 2,
    FLOOR_WIDTH - (GATE_X + GATE_WIDTH + 20),
    WALL_THICKNESS
)
INNER_WALL_RECTS = [WALL_LEFT_RECT, WALL_RIGHT_RECT]
ROAD_START_Y = GATE_Y + GATE_HEIGHT + GRID_SIZE * 3
ROAD_WIDTH = GRID_SIZE * 10
ROAD_X = (FLOOR_WIDTH - ROAD_WIDTH) // 2
ROAD_RECT = pygame.Rect(ROAD_X, ROAD_START_Y, ROAD_WIDTH, FLOOR_HEIGHT - ROAD_START_Y)
DASH_LENGTH = GRID_SIZE // 2
DASH_GAP = GRID_SIZE // 2

# 剧情对话内容（完全保留原有）
dialog_content = [
    "中学生：学校组织的公益活动也太奇怪了吧？",
    "中学生：明明说要去一家正规医院帮忙，结果大巴车停在了这所废弃医院门口。",
    "中学生：周围连个人影都没有，不过既然来了，不如进去看看里面到底有什么...",
    "中学生：大门好像锁着，按E试试能不能打开，进去后一定要提高警惕！"
]
current_dialog_index = 0

# 快捷键配置（完全保留原有）
DEFAULT_SHORTCUTS = {
    "move_up": pygame.K_w,
    "move_down": pygame.K_s,
    "move_left": pygame.K_a,
    "move_right": pygame.K_d,
    "open_gate": pygame.K_e
}
config = {
    "resolution": (DEFAULT_WIDTH, DEFAULT_HEIGHT),
    "shortcuts": DEFAULT_SHORTCUTS.copy()
}
shortcut_items = [("上移", "move_up"), ("下移", "move_down"), ("左移", "move_left"), ("右移", "move_right"), ("开门", "open_gate")]

# 面板位置计算的公共函数，确保draw_settings和handle_events使用相同的逻辑
def calculate_panel_position(resolution):
    """计算设置面板的位置和尺寸，确保UI元素坐标计算一致
    
    Args:
        resolution: 游戏分辨率元组 (width, height)
    
    Returns:
        tuple: (panel_x, panel_y, panel_width, panel_height)
    """
    panel_width = 850  # 增大宽度，从650变为850（增加200像素，实现往左延伸）
    panel_height = resolution[1] - 150  # 保持高度不变
    panel_x = resolution[0] - panel_width - 50  # 保持距离右边50像素不变，实现往左延伸
    panel_y = 100  # 保持Y位置不变
    return panel_x, panel_y, panel_width, panel_height

# 音频资源路径（修复咖啡厅BGM路径拼写错误：cafe_bgn.mp3 → cafe_bgm.mp3）
AUDIO_PATHS = {
    "menu": "menu_bgm.mp3",        # 主界面/副本选择共用BGM
    "hospital": "hospital_bgm.mp3",# 废弃医院BGM
    "cafe": "cafe_bgm.mp3",        # 咖啡厅BGM（已修正拼写错误）
    "open_gate": "open_gate.wav"   # 开门音效
}

# 工具函数（完全保留原有）
def create_default_image(width, height, color):
    img = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(img, color, (0, 0, width, height), border_radius=5)
    return img

def check_collision(player_rect):
    for wall_rect in INNER_WALL_RECTS:
        if player_rect.colliderect(wall_rect):
            return True
    if not gate_is_open and player_rect.colliderect(GATE_RECT):
        return True
    return False

def check_cafe_collision(player_rect):
    if player_rect.colliderect(CAFE_WALL_RECT) and not player_rect.colliderect(CAFE_GATE_RECT):
        return True
    if not cafe_gate_is_open and player_rect.colliderect(CAFE_GATE_RECT):
        return True
    return False

def is_player_near_gate(player_rect):
    trigger_rect = GATE_RECT.inflate(GATE_TRIGGER_RANGE, GATE_TRIGGER_RANGE // 2)
    return player_rect.colliderect(trigger_rect)

def is_player_near_cafe_gate(player_rect):
    trigger_rect = CAFE_GATE_RECT.inflate(CAFE_GATE_TRIGGER_RANGE, CAFE_GATE_TRIGGER_RANGE // 2)
    return player_rect.colliderect(trigger_rect)

def fix_gate_stuck(player_rect, player):
    if gate_is_open or not player_rect.colliderect(GATE_RECT):
        return player_rect
    gate_mid_y = GATE_RECT.y + GATE_RECT.height // 2
    player_mid_y = player_rect.centery
    if player_mid_y < gate_mid_y:
        player.y -= GRID_SIZE
    else:
        player.y += GRID_SIZE
    return pygame.Rect(
        player.x - player.width//2,
        player.y - player.height//2,
        player.width,
        player.height
    )

def fix_cafe_gate_stuck(player_rect, player):
    if cafe_gate_is_open or not player_rect.collidepoint(CAFE_GATE_RECT.center):
        return player_rect
    gate_mid_y = CAFE_GATE_RECT.y + CAFE_GATE_RECT.height // 2
    player_mid_y = player_rect.centery
    if player_mid_y < gate_mid_y:
        player.y -= GRID_SIZE
    else:
        player.y += GRID_SIZE
    return pygame.Rect(
        player.x - player.width//2,
        player.y - player.height//2,
        player.width,
        player.height
    )

def update_camera():
    global camera_x, camera_y
    camera_x = player.x - config["resolution"][0] // 2
    camera_y = player.y - config["resolution"][1] // 2
    if current_state == GameState.HOSPITAL:
        camera_x = max(0, min(camera_x, FLOOR_WIDTH - config["resolution"][0]))
        camera_y = max(0, min(camera_y, FLOOR_HEIGHT - config["resolution"][1]))
    elif current_state == GameState.CAFE:
        camera_x = max(0, min(camera_x, CAFE_MAP_WIDTH - config["resolution"][0]))
        camera_y = max(0, min(camera_y, CAFE_MAP_HEIGHT - config["resolution"][1]))

def update_gate_cooldown():
    global gate_cooldown
    if gate_cooldown > 0:
        gate_cooldown -= 1

# 音频控制函数（保留原有容错逻辑）
def load_audio():
    """加载所有音频资源，添加容错处理"""
    global gate_sound
    gate_sound = None  # 初始化为None
    try:
        gate_sound = pygame.mixer.Sound(AUDIO_PATHS["open_gate"])
        gate_sound.set_volume(sfx_volume)
    except pygame.error as e:
        print(f"⚠️  加载开门音效失败: {e}（缺少open_gate.wav文件，不影响游戏运行）")

def play_bgm(bgm_name):
    """播放指定BGM，添加容错处理"""
    global current_bgm
    if current_bgm == bgm_name:
        return
    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load(AUDIO_PATHS[bgm_name])
        pygame.mixer.music.set_volume(bgm_volume)
        pygame.mixer.music.play(-1)
        current_bgm = bgm_name
    except pygame.error as e:
        print(f"⚠️  加载{bgm_name} BGM失败: {e}（缺少{AUDIO_PATHS[bgm_name]}文件，不影响游戏运行）")
        current_bgm = None

def stop_bgm():
    """停止当前BGM"""
    pygame.mixer.music.stop()
    global current_bgm
    current_bgm = None

def play_sfx(sound_obj):
    """播放音效，添加容错处理"""
    if sound_obj:
        try:
            sound_obj.set_volume(sfx_volume)
            sound_obj.play()
        except:
            pass
# 玩家类（完全保留原有，无任何修改）
class Player:
    def __init__(self):
        try:
            self.idle_up = pygame.image.load("player_idle_up.png").convert_alpha()
            self.idle_down = pygame.image.load("player_idle_down.png").convert_alpha()
            self.idle_left = pygame.image.load("player_idle_left.png").convert_alpha()
            self.idle_right = pygame.image.load("player_idle_right.png").convert_alpha()
            self.walk_up = pygame.image.load("player_walk_up.png").convert_alpha()
            self.walk_down = pygame.image.load("player_walk_down.png").convert_alpha()
            self.walk_left = pygame.image.load("player_walk_left.png").convert_alpha()
            self.walk_right = pygame.image.load("player_walk_right.png").convert_alpha()
        except pygame.error:
            print("⚠️  缺少玩家图片，使用默认红色方块")
            self.idle_up = create_default_image(100, 150, PLAYER_DEFAULT_COLOR)
            self.idle_down = create_default_image(100, 150, PLAYER_DEFAULT_COLOR)
            self.idle_left = create_default_image(100, 150, PLAYER_DEFAULT_COLOR)
            self.idle_right = create_default_image(100, 150, PLAYER_DEFAULT_COLOR)
            self.walk_up = create_default_image(100, 150, PLAYER_DEFAULT_COLOR)
            self.walk_down = create_default_image(100, 150, PLAYER_DEFAULT_COLOR)
            self.walk_left = create_default_image(100, 150, PLAYER_DEFAULT_COLOR)
            self.walk_right = create_default_image(100, 150, PLAYER_DEFAULT_COLOR)
        
        self.scale = 0.15  # 若需匹配偏好的0.05，可修改此处
        self.width = int(self.idle_down.get_width() * self.scale)
        self.height = int(self.idle_down.get_height() * self.scale)
        self._scale_all_images()
        
        self.current_img = self.idle_down
        self.start_x = GATE_X + GATE_WIDTH // 2
        self.start_y = GATE_Y + GATE_HEIGHT + GRID_SIZE
        self.x = self.start_x
        self.y = self.start_y
        self.last_direction = "down"
        self.speed = 6
        self.is_moving = False

    def _scale_all_images(self):
        self.idle_up = pygame.transform.scale(self.idle_up, (self.width, self.height))
        self.idle_down = pygame.transform.scale(self.idle_down, (self.width, self.height))
        self.idle_left = pygame.transform.scale(self.idle_left, (self.width, self.height))
        self.idle_right = pygame.transform.scale(self.idle_right, (self.width, self.height))
        self.walk_up = pygame.transform.scale(self.walk_up, (self.width, self.height))
        self.walk_down = pygame.transform.scale(self.walk_down, (self.width, self.height))
        self.walk_left = pygame.transform.scale(self.walk_left, (self.width, self.height))
        self.walk_right = pygame.transform.scale(self.walk_right, (self.width, self.height))

    def move(self, keys, delta_time):
        if is_paused or current_state == GameState.DIALOG:
            self.is_moving = False
            return
        
        self.is_moving = False
        current_direction = self.last_direction
        prev_x = self.x
        prev_y = self.y
        
        # 使用delta_time调整速度，确保移动速度不受帧率影响
        adjusted_speed = self.speed * delta_time * 60  # 以60fps为基准
        
        # 使用key_states字典检查按键状态，解决中文输入法问题
        if key_states["move_up"]:
            self.y -= adjusted_speed
            self.is_moving = True
            current_direction = "up"
        if key_states["move_down"]:
            self.y += adjusted_speed
            self.is_moving = True
            current_direction = "down"
        if key_states["move_left"]:
            self.x -= adjusted_speed
            self.is_moving = True
            current_direction = "left"
        if key_states["move_right"]:
            self.x += adjusted_speed
            self.is_moving = True
            current_direction = "right"
        
        if current_state == GameState.HOSPITAL:
            self.x = max(self.width//2, min(self.x, FLOOR_WIDTH - self.width//2))
            self.y = max(self.height//2, min(self.y, FLOOR_HEIGHT - self.height//2))
        elif current_state == GameState.CAFE:
            self.x = max(self.width//2, min(self.x, CAFE_MAP_WIDTH - self.width//2))
            self.y = max(self.height//2, min(self.y, CAFE_MAP_HEIGHT - self.height//2))
        
        player_rect = pygame.Rect(
            self.x - self.width//2,
            self.y - self.height//2,
            self.width,
            self.height
        )
        if current_state == GameState.HOSPITAL:
            collision = check_collision(player_rect)
        else:
            collision = check_cafe_collision(player_rect)
        
        if collision:
            self.x = prev_x
            self.y = prev_y
            self.is_moving = False
        
        if self.is_moving:
            self.last_direction = current_direction
        
        if self.is_moving:
            self.current_img = {
                "up": self.walk_up,
                "down": self.walk_down,
                "left": self.walk_left,
                "right": self.walk_right
            }[current_direction]
        else:
            self.current_img = {
                "up": self.idle_up,
                "down": self.idle_down,
                "left": self.idle_left,
                "right": self.idle_right
            }[self.last_direction]

    def draw(self, surface):
        draw_x = self.x - camera_x - self.width//2
        draw_y = self.y - camera_y - self.height//2
        surface.blit(self.current_img, (draw_x, draw_y))

# 界面绘制辅助函数（对话框+NPC初始化，NPC尺寸保持200×200像素）
def init_npc_img():
    try:
        npc_img = pygame.image.load("player_walk3.png").convert_alpha()
        return pygame.transform.scale(npc_img, (200, 200))  # 匹配偏好的NPC尺寸
    except pygame.error:
        print("⚠️  缺少NPC图片，使用默认绿色方块")
        return create_default_image(200, 200, NPC_DEFAULT_COLOR)  # 默认尺寸200×200

def draw_dialog():
    dialog_width = 800
    dialog_height = 200
    dialog_x = (config["resolution"][0] - dialog_width) // 2
    dialog_y = (config["resolution"][1] - dialog_height) // 2

    dialog_surface = pygame.Surface((dialog_width, dialog_height), pygame.SRCALPHA)
    pygame.draw.rect(dialog_surface, (50, 50, 60, 230), (0, 0, dialog_width, dialog_height), border_radius=8)
    pygame.draw.rect(dialog_surface, (255, 255, 255, 100), (0, 0, dialog_width, dialog_height), 2, border_radius=8)
    screen.blit(dialog_surface, (dialog_x, dialog_y))

    npc_img = init_npc_img()
    npc_x = dialog_x + 20
    npc_y = dialog_y + (dialog_height - 100) // 2
    screen.blit(pygame.transform.scale(npc_img, (100, 100)), (npc_x, npc_y))

    current_text = dialog_content[current_dialog_index]
    text_x = dialog_x + 140
    text_y = dialog_y + 40
    line_spacing = 30
    max_text_width = dialog_width - 180
    
    # 计算对话框中可显示的最大行数（考虑顶部间距和底部提示文本的空间）
    available_height = dialog_height - 80  # 顶部40px + 底部40px用于提示文本
    max_lines = available_height // line_spacing

    # 优化的文本换行算法：尽量按单词分割
    words = []
    current_word = ""
    for char in current_text:
        if char.isspace():
            if current_word:
                words.append(current_word)
                words.append(char)  # 保留空格
                current_word = ""
            else:
                words.append(char)  # 连续空格
        else:
            current_word += char
    if current_word:
        words.append(current_word)

    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word
        if dialog_font.size(test_line)[0] <= max_text_width:
            current_line = test_line
        else:
            # 如果当前行不为空，添加到行列表
            if current_line:
                lines.append(current_line)
                current_line = word
            else:  # 单个单词太长，需要强制拆分
                for char in word:
                    test_line = current_line + char
                    if dialog_font.size(test_line)[0] <= max_text_width:
                        current_line = test_line
                    else:
                        lines.append(current_line)
                        current_line = char
    if current_line:
        lines.append(current_line)

    # 检查是否有文本溢出
    text_overflows = len(lines) > max_lines
    
    # 只渲染不超出最大行数的文本
    for i, line in enumerate(lines[:max_lines]):
        text_surf = dialog_font.render(line, True, TEXT_COLOR)
        screen.blit(text_surf, (text_x, text_y + i * line_spacing))
    
    # 如果有文本溢出，显示提示
    if text_overflows:
        overflow_hint = small_font.render("...", True, TEXT_COLOR)
        overflow_x = text_x + max_text_width - overflow_hint.get_width() - 5
        overflow_y = text_y + (max_lines - 1) * line_spacing
        screen.blit(overflow_hint, (overflow_x, overflow_y))

    hint_surf = small_font.render("点击鼠标左键继续/关闭剧情", True, (150, 150, 150))
    hint_x = dialog_x + (dialog_width - hint_surf.get_width()) // 2
    hint_y = dialog_y + dialog_height - 40
    screen.blit(hint_surf, (hint_x, hint_y))

# 废弃医院地图绘制（含BGM播放）
def draw_hospital():
    screen.fill(BG_COLOR)
    screen.fill((30, 30, 30))

    wall_bottom_y = WALL_LEFT_RECT.y + WALL_THICKNESS
    gate_bottom_y = GATE_RECT.y + GATE_RECT.height
    road_start_y = ROAD_START_Y
    road_end_y = FLOOR_HEIGHT
    road_left_x = ROAD_X
    road_right_x = ROAD_X + ROAD_WIDTH

    for x in range(0, FLOOR_WIDTH, FLOOR_BLOCK_SIZE):
        for y in range(0, FLOOR_HEIGHT, FLOOR_BLOCK_SIZE):
            draw_x = x - camera_x
            draw_y = y - camera_y
            block_x_center = x + FLOOR_BLOCK_SIZE // 2
            block_y_center = y + FLOOR_BLOCK_SIZE // 2

            if y >= road_start_y:
                if road_left_x <= block_x_center <= road_right_x:
                    color = ROAD_COLOR
                else:
                    color = GRASS_COLOR_1 if (x//FLOOR_BLOCK_SIZE + y//FLOOR_BLOCK_SIZE) % 2 == 0 else GRASS_COLOR_2
            elif y > gate_bottom_y:
                color = DIRT_COLOR_1 if (x//FLOOR_BLOCK_SIZE + y//FLOOR_BLOCK_SIZE) % 2 == 0 else DIRT_COLOR_2
            elif y > wall_bottom_y:
                color = GRASS_COLOR_1 if (x//FLOOR_BLOCK_SIZE + y//FLOOR_BLOCK_SIZE) % 2 == 0 else GRASS_COLOR_2
            else:
                color = (180, 180, 180) if (x//FLOOR_BLOCK_SIZE + y//FLOOR_BLOCK_SIZE) % 2 == 0 else (160, 160, 160)
            
            if 0 <= draw_x < config["resolution"][0] and 0 <= draw_y < config["resolution"][1]:
                pygame.draw.rect(screen, color, (draw_x, draw_y, FLOOR_BLOCK_SIZE, FLOOR_BLOCK_SIZE))
                pygame.draw.rect(screen, (20, 20, 20), (draw_x, draw_y, FLOOR_BLOCK_SIZE, FLOOR_BLOCK_SIZE), 1)

    start_draw_y = max(0, road_start_y - camera_y)
    end_draw_y = min(config["resolution"][1], road_end_y - camera_y)
    center_line_x = (road_left_x + road_right_x) // 2 - camera_x

    pygame.draw.line(screen, ROAD_EDGE_COLOR, (road_left_x - camera_x, start_draw_y), (road_left_x - camera_x, end_draw_y), 2)
    pygame.draw.line(screen, ROAD_EDGE_COLOR, (road_right_x - camera_x, start_draw_y), (road_right_x - camera_x, end_draw_y), 2)

    current_y = start_draw_y
    while current_y < end_draw_y:
        line_end_y = min(current_y + DASH_LENGTH, end_draw_y)
        pygame.draw.line(screen, ROAD_CENTER_COLOR, (center_line_x, current_y), (center_line_x, line_end_y), 3)
        current_y += DASH_LENGTH + DASH_GAP

    # 绘制墙壁和大门
    pygame.draw.rect(screen, WALL_COLOR, (
        WALL_LEFT_RECT.x - camera_x,
        WALL_LEFT_RECT.y - camera_y,
        WALL_LEFT_RECT.width,
        WALL_LEFT_RECT.height
    ))
    pygame.draw.rect(screen, WALL_COLOR, (
        WALL_RIGHT_RECT.x - camera_x,
        WALL_RIGHT_RECT.y - camera_y,
        WALL_RIGHT_RECT.width,
        WALL_RIGHT_RECT.height
    ))
    
    gate_color = GATE_OPEN_COLOR if gate_is_open else GATE_COLOR
    pygame.draw.rect(screen, gate_color, (
        GATE_RECT.x - camera_x,
        GATE_RECT.y - camera_y,
        GATE_RECT.width,
        GATE_RECT.height
    ))
    border_color = (80, 40, 0) if gate_is_open else (120, 60, 0)
    pygame.draw.rect(screen, border_color, (
        GATE_RECT.x - camera_x,
        GATE_RECT.y - camera_y,
        GATE_RECT.width,
        GATE_RECT.height
    ), 4)
    for i in range(1, 3):
        divider_x = (GATE_RECT.x + i * GRID_SIZE) - camera_x
        divider_y_top = GATE_RECT.y - camera_y
        divider_y_bottom = GATE_RECT.y + GATE_RECT.height - camera_y
        pygame.draw.line(screen, border_color, (divider_x, divider_y_top), (divider_x, divider_y_bottom), 3)

    # 显示输入法切换提示（仅当未按下移动键时）
    if show_input_tip:
        input_tip_text = "切换为英文输入法才能正常游戏哦"
        input_tip_surf = small_font.render(input_tip_text, True, (255, 255, 255))
        input_tip_bg = pygame.Surface((input_tip_surf.get_width() + 10, input_tip_surf.get_height() + 5), pygame.SRCALPHA)
        pygame.draw.rect(input_tip_bg, (0, 0, 0, 150), (0, 0, input_tip_bg.get_width(), input_tip_bg.get_height()), border_radius=3)
        input_tip_x = config["resolution"][0] - input_tip_surf.get_width() - 20
        input_tip_y = 20
        screen.blit(input_tip_bg, (input_tip_x - 5, input_tip_y - 2))
        screen.blit(input_tip_surf, (input_tip_x, input_tip_y))

    # 大门提示文字
    player_rect = pygame.Rect(
        player.x - player.width//2,
        player.y - player.height//2,
        player.width,
        player.height
    )
    if not is_player_near_gate(player_rect):
        gate_center_x = GATE_RECT.x + GATE_RECT.width//2 - camera_x
        gate_center_y = GATE_RECT.y + GATE_RECT.height//2 - camera_y
        hint_text = "→ 大门在前方 ←"
        hint_surf = small_font.render(hint_text, True, (255, 150, 0))
        hint_x = gate_center_x - hint_surf.get_width()//2
        hint_y = gate_center_y - 60
        screen.blit(hint_surf, (hint_x, hint_y))
    else:
        if not gate_is_open:
            hint_text = f"按{pygame.key.name(config['shortcuts']['open_gate'])}打开大门"
        else:
            hint_text = "✅ 大门已打开，可直接穿过！"
        hint_surf = small_font.render(hint_text, True, (0, 255, 0))
        hint_bg = pygame.Surface((hint_surf.get_width() + 20, hint_surf.get_height() + 10), pygame.SRCALPHA)
        pygame.draw.rect(hint_bg, (0, 0, 0, 200), (0, 0, hint_bg.get_width(), hint_bg.get_height()), border_radius=5)
        hint_x = (GATE_RECT.x + GATE_RECT.width//2) - camera_x - hint_surf.get_width()//2
        hint_y = GATE_RECT.y - camera_x - 50
        screen.blit(hint_bg, (hint_x - 10, hint_y - 5))
        screen.blit(hint_surf, (hint_x, hint_y))

    player.draw(screen)

    if current_state == GameState.DIALOG:
        draw_dialog()

    if is_paused:
        pause_surface = pygame.Surface(config["resolution"], pygame.SRCALPHA)
        pygame.draw.rect(pause_surface, PAUSE_MASK_COLOR, (0, 0, config["resolution"][0], config["resolution"][1]))
        screen.blit(pause_surface, (0, 0))
        
        pause_text = pause_font.render("暂停", True, (255, 255, 255))
        pause_text_rect = pause_text.get_rect(center=(config["resolution"][0]//2, 200))
        shadow_text = pause_font.render("暂停", True, (0, 0, 0, 100))
        screen.blit(shadow_text, (pause_text_rect.x + 5, pause_text_rect.y + 5))
        screen.blit(pause_text, pause_text_rect)

        btn_height = 50
        btn_spacing = 30
        
        # 存档按钮
        save_btn_width = 150
        save_btn_y = (config["resolution"][1] // 2) - 100
        save_btn = pygame.Rect(
            config["resolution"][0]//2 - save_btn_width//2,
            save_btn_y,
            save_btn_width,
            btn_height
        )
        save_is_hovered = save_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), save_btn)
        pygame.draw.rect(screen, (100, 180, 255) if save_is_hovered else (0, 0, 0), save_btn, 2)
        save_text_color = (255, 255, 255) if save_is_hovered else (200, 200, 200)
        save_text = option_font.render("存档", True, save_text_color)
        screen.blit(save_text, save_text.get_rect(center=save_btn.center))
        
        # 设置按钮
        settings_btn_width = 150
        settings_btn_y = save_btn_y + btn_height + btn_spacing
        settings_btn = pygame.Rect(
            config["resolution"][0]//2 - settings_btn_width//2,
            settings_btn_y,
            settings_btn_width,
            btn_height
        )
        settings_is_hovered = settings_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), settings_btn)
        pygame.draw.rect(screen, (100, 180, 255) if settings_is_hovered else (0, 0, 0), settings_btn, 2)
        settings_text_color = (255, 255, 255) if settings_is_hovered else (200, 200, 200)
        settings_text = option_font.render("设置", True, settings_text_color)
        screen.blit(settings_text, settings_text.get_rect(center=settings_btn.center))
        
        # 返回副本选择按钮
        back_btn_width = 200  # 增加按钮宽度以容纳更长文本
        back_btn_y = settings_btn_y + btn_height + btn_spacing
        back_btn = pygame.Rect(
            config["resolution"][0]//2 - back_btn_width//2,
            back_btn_y,
            back_btn_width,
            btn_height
        )
        back_is_hovered = back_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), back_btn)
        pygame.draw.rect(screen, (100, 180, 255) if back_is_hovered else (0, 0, 0), back_btn, 2)
        back_text_color = (255, 255, 255) if back_is_hovered else (200, 200, 200)
        back_text = option_font.render("返回副本选择", True, back_text_color)
        screen.blit(back_text, back_text.get_rect(center=back_btn.center))

    # 播放医院BGM
    if current_bgm != "hospital":
        play_bgm("hospital")

# 咖啡厅地图绘制（含BGM播放，路径已修复）
def draw_cafe():
    screen.fill(BG_COLOR)
    screen.fill((40, 40, 40))

    # 绘制地板
    floor_rect = pygame.Rect(0, 0, CAFE_MAP_WIDTH, CAFE_FLOOR_HEIGHT)
    pygame.draw.rect(screen, CAFE_FLOOR_COLOR, (
        floor_rect.x - camera_x,
        floor_rect.y - camera_y,
        floor_rect.width,
        floor_rect.height
    ))
    grid_size = 50
    for x in range(0, CAFE_MAP_WIDTH, grid_size):
        pygame.draw.line(screen, (100, 60, 20), (x - camera_x, 0 - camera_y), (x - camera_x, CAFE_FLOOR_HEIGHT - camera_y), 1)
    for y in range(0, CAFE_FLOOR_HEIGHT, grid_size):
        pygame.draw.line(screen, (100, 60, 20), (0 - camera_x, y - camera_y), (CAFE_MAP_WIDTH - camera_x, y - camera_y), 1)

    # 绘制街道
    street_rect = pygame.Rect(0, CAFE_FLOOR_HEIGHT + CAFE_WALL_THICKNESS, CAFE_MAP_WIDTH, CAFE_STREET_HEIGHT)
    pygame.draw.rect(screen, CAFE_STREET_COLOR, (
        street_rect.x - camera_x,
        street_rect.y - camera_y,
        street_rect.width,
        street_rect.height
    ))
    for y in range(street_rect.y, street_rect.y + street_rect.height, 10):
        pygame.draw.line(screen, (100, 100, 100), (0 - camera_x, y - camera_y), (CAFE_MAP_WIDTH - camera_x, y - camera_y), 1)

    # 绘制墙壁和大门
    wall_left_rect = pygame.Rect(
        0,
        CAFE_WALL_Y,
        CAFE_GATE_X,
        CAFE_WALL_THICKNESS
    )
    pygame.draw.rect(screen, CAFE_WALL_COLOR, (
        wall_left_rect.x - camera_x,
        wall_left_rect.y - camera_y,
        wall_left_rect.width,
        wall_left_rect.height
    ))
    wall_right_rect = pygame.Rect(
        CAFE_GATE_X + CAFE_GATE_WIDTH,
        CAFE_WALL_Y,
        CAFE_MAP_WIDTH - (CAFE_GATE_X + CAFE_GATE_WIDTH),
        CAFE_WALL_THICKNESS
    )
    pygame.draw.rect(screen, CAFE_WALL_COLOR, (
        wall_right_rect.x - camera_x,
        wall_right_rect.y - camera_y,
        wall_right_rect.width,
        wall_right_rect.height
    ))
    
    gate_color = CAFE_GATE_OPEN_COLOR if cafe_gate_is_open else CAFE_GATE_COLOR
    pygame.draw.rect(screen, gate_color, (
        CAFE_GATE_RECT.x - camera_x,
        CAFE_GATE_RECT.y - camera_y,
        CAFE_GATE_RECT.width,
        CAFE_GATE_RECT.height
    ))
    border_color = CAFE_GATE_BORDER
    pygame.draw.rect(screen, border_color, (
        CAFE_GATE_RECT.x - camera_x,
        CAFE_GATE_RECT.y - camera_y,
        CAFE_GATE_RECT.width,
        CAFE_GATE_RECT.height
    ), 2)
    if not cafe_gate_is_open:
        divider_x = CAFE_GATE_RECT.x + CAFE_GATE_RECT.width//2 - camera_x
        divider_y_top = CAFE_GATE_RECT.y - camera_y
        divider_y_bottom = CAFE_GATE_RECT.y + CAFE_GATE_RECT.height - camera_y
        pygame.draw.line(screen, border_color, (divider_x, divider_y_top), (divider_x, divider_y_bottom), 2)

    # 显示输入法切换提示（仅当未按下移动键时）
    if show_input_tip:
        input_tip_text = "切换为英文输入法才能正常游戏哦"
        input_tip_surf = small_font.render(input_tip_text, True, (255, 255, 255))
        input_tip_bg = pygame.Surface((input_tip_surf.get_width() + 10, input_tip_surf.get_height() + 5), pygame.SRCALPHA)
        pygame.draw.rect(input_tip_bg, (0, 0, 0, 150), (0, 0, input_tip_bg.get_width(), input_tip_bg.get_height()), border_radius=3)
        input_tip_x = config["resolution"][0] - input_tip_surf.get_width() - 20
        input_tip_y = 20
        screen.blit(input_tip_bg, (input_tip_x - 5, input_tip_y - 2))
        screen.blit(input_tip_surf, (input_tip_x, input_tip_y))

    # 大门提示文字
    player_rect = pygame.Rect(
        player.x - player.width//2,
        player.y - player.height//2,
        player.width,
        player.height
    )
    gate_center_x = CAFE_GATE_RECT.x + CAFE_GATE_RECT.width//2 - camera_x
    gate_center_y = CAFE_GATE_RECT.y + CAFE_GATE_RECT.height//2 - camera_y
    if not is_player_near_cafe_gate(player_rect):
        hint_text = "→ 咖啡厅大门 ←"
        hint_surf = small_font.render(hint_text, True, (255, 150, 0))
        hint_x = gate_center_x - hint_surf.get_width()//2
        hint_y = gate_center_y - 40
        screen.blit(hint_surf, (hint_x, hint_y))
    else:
        if not cafe_gate_is_open:
            hint_text = f"按{pygame.key.name(config['shortcuts']['open_gate'])}打开大门"
        else:
            hint_text = "✅ 大门已打开，可进入咖啡厅！"
        hint_surf = small_font.render(hint_text, True, (0, 255, 0))
        hint_bg = pygame.Surface((hint_surf.get_width() + 20, hint_surf.get_height() + 10), pygame.SRCALPHA)
        pygame.draw.rect(hint_bg, (0, 0, 0, 200), (0, 0, hint_bg.get_width(), hint_bg.get_height()), border_radius=5)
        hint_x = gate_center_x - hint_surf.get_width()//2
        hint_y = gate_center_y - 50
        screen.blit(hint_bg, (hint_x - 10, hint_y - 5))
        screen.blit(hint_surf, (hint_x, hint_y))

    player.draw(screen)

    if current_state == GameState.DIALOG:
        draw_dialog()

    if is_paused:
        pause_surface = pygame.Surface(config["resolution"], pygame.SRCALPHA)
        pygame.draw.rect(pause_surface, PAUSE_MASK_COLOR, (0, 0, config["resolution"][0], config["resolution"][1]))
        screen.blit(pause_surface, (0, 0))
        
        pause_text = pause_font.render("暂停", True, (255, 255, 255))
        pause_text_rect = pause_text.get_rect(center=(config["resolution"][0]//2, 200))
        shadow_text = pause_font.render("暂停", True, (0, 0, 0, 100))
        screen.blit(shadow_text, (pause_text_rect.x + 5, pause_text_rect.y + 5))
        screen.blit(pause_text, pause_text_rect)

        btn_height = 50
        btn_spacing = 30
        
        # 存档按钮
        save_btn_width = 150
        save_btn_y = (config["resolution"][1] // 2) - 100
        save_btn = pygame.Rect(
            config["resolution"][0]//2 - save_btn_width//2,
            save_btn_y,
            save_btn_width,
            btn_height
        )
        save_is_hovered = save_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), save_btn)
        pygame.draw.rect(screen, (100, 180, 255) if save_is_hovered else (0, 0, 0), save_btn, 2)
        save_text_color = (255, 255, 255) if save_is_hovered else (200, 200, 200)
        save_text = option_font.render("存档", True, save_text_color)
        screen.blit(save_text, save_text.get_rect(center=save_btn.center))
        
        # 设置按钮
        settings_btn_width = 150
        settings_btn_y = save_btn_y + btn_height + btn_spacing
        settings_btn = pygame.Rect(
            config["resolution"][0]//2 - settings_btn_width//2,
            settings_btn_y,
            settings_btn_width,
            btn_height
        )
        settings_is_hovered = settings_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), settings_btn)
        pygame.draw.rect(screen, (100, 180, 255) if settings_is_hovered else (0, 0, 0), settings_btn, 2)
        settings_text_color = (255, 255, 255) if settings_is_hovered else (200, 200, 200)
        settings_text = option_font.render("设置", True, settings_text_color)
        screen.blit(settings_text, settings_text.get_rect(center=settings_btn.center))
        
        # 返回副本选择按钮
        back_btn_width = 200  # 增加按钮宽度以容纳更长文本
        back_btn_y = settings_btn_y + btn_height + btn_spacing
        back_btn = pygame.Rect(
            config["resolution"][0]//2 - back_btn_width//2,
            back_btn_y,
            back_btn_width,
            btn_height
        )
        back_is_hovered = back_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), back_btn)
        pygame.draw.rect(screen, (100, 180, 255) if back_is_hovered else (0, 0, 0), back_btn, 2)
        back_text_color = (255, 255, 255) if back_is_hovered else (200, 200, 200)
        back_text = option_font.render("返回副本选择", True, back_text_color)
        screen.blit(back_text, back_text.get_rect(center=back_btn.center))

    # 播放咖啡厅BGM（路径已修复）
    if current_bgm != "cafe":
        play_bgm("cafe")
# 主菜单绘制（含BGM播放）
def draw_main_menu():
    screen.fill(BG_COLOR)
    menu_width = 250
    menu_height = 320
    menu_x = 150
    menu_y = (config["resolution"][1] - menu_height) // 2

    pygame.draw.rect(screen, MENU_BG, (menu_x, menu_y, menu_width, menu_height))
    pygame.draw.rect(screen, BUTTON_COLOR, (menu_x, menu_y, menu_width, menu_height), 2)

    # 绘制标题，确保不超出菜单宽度
    # 使用更小的字体渲染标题，避免超出菜单宽度
    title_text = option_font.render("逃离学校剧本", True, TEXT_COLOR)
    # 计算标题位置，确保居中且不超出菜单
    title_x = menu_x + (menu_width - title_text.get_width()) // 2
    title_y = menu_y + 35
    screen.blit(title_text, (title_x, title_y))

    btn_width = menu_width - 20
    btn_height = 45
    button_y_offset = 80
    button_spacing = 55

    # 开始游戏按钮
    start_btn = pygame.Rect(menu_x + 10, menu_y + button_y_offset, btn_width, btn_height)
    start_is_hovered = start_btn.collidepoint(pygame.mouse.get_pos())
    # 设置按钮背景为浅蓝色，边框为黑色实线
    pygame.draw.rect(screen, (60, 120, 200), start_btn)
    pygame.draw.rect(screen, (100, 180, 255) if start_is_hovered else (0, 0, 0), start_btn, 2)
    # 鼠标悬停时文本颜色变为高亮
    start_text_color = (255, 255, 255) if start_is_hovered else (200, 200, 200)
    start_text = option_font.render("开始游戏", True, start_text_color)
    start_text_pos = start_text.get_rect(center=start_btn.center)
    screen.blit(start_text, start_text_pos)

    # 设置按钮
    setting_btn = pygame.Rect(menu_x + 10, menu_y + button_y_offset + button_spacing, btn_width, btn_height)
    setting_is_hovered = setting_btn.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, (60, 120, 200), setting_btn)
    pygame.draw.rect(screen, (100, 180, 255) if setting_is_hovered else (0, 0, 0), setting_btn, 2)
    setting_text_color = (255, 255, 255) if setting_is_hovered else (200, 200, 200)
    setting_text = option_font.render("设置", True, setting_text_color)
    setting_text_pos = setting_text.get_rect(center=setting_btn.center)
    screen.blit(setting_text, setting_text_pos)

    # 游戏信息按钮
    info_btn = pygame.Rect(menu_x + 10, menu_y + button_y_offset + button_spacing * 2, btn_width, btn_height)
    info_is_hovered = info_btn.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, (60, 120, 200), info_btn)
    pygame.draw.rect(screen, (100, 180, 255) if info_is_hovered else (0, 0, 0), info_btn, 2)
    info_text_color = (255, 255, 255) if info_is_hovered else (200, 200, 200)
    info_text = option_font.render("游戏信息", True, info_text_color)
    info_text_pos = info_text.get_rect(center=info_btn.center)
    screen.blit(info_text, info_text_pos)

    # 退出游戏按钮 - 保持红色不变
    quit_btn = pygame.Rect(menu_x + 10, menu_y + button_y_offset + button_spacing * 3, btn_width, btn_height)
    quit_is_hovered = quit_btn.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, (200, 60, 60), quit_btn)
    pygame.draw.rect(screen, (255, 0, 0) if quit_is_hovered else (0, 0, 0), quit_btn, 2)
    quit_text_color = (255, 255, 255) if quit_is_hovered else (200, 200, 200)
    quit_text = option_font.render("退出游戏", True, quit_text_color)
    quit_text_pos = quit_text.get_rect(center=quit_btn.center)
    screen.blit(quit_text, quit_text_pos)

    # 播放菜单BGM
    if current_bgm != "menu":
        play_bgm("menu")

    return start_btn, setting_btn, info_btn, quit_btn

# 设置图标绘制函数
def draw_settings_icon():
    """绘制左下角的设置图标
    
    Returns:
        pygame.Rect: 设置图标的碰撞矩形
    """
    icon_size = 50
    icon_margin = 20
    
    # 图标位置：左下角
    icon_x = icon_margin
    icon_y = config["resolution"][1] - icon_size - icon_margin
    
    # 创建图标矩形
    icon_rect = pygame.Rect(icon_x, icon_y, icon_size, icon_size)
    
    # 检查鼠标是否悬停
    mouse_pos = pygame.mouse.get_pos()
    is_hovered = icon_rect.collidepoint(mouse_pos)
    
    # 绘制图标背景
    if is_hovered:
        pygame.draw.rect(screen, BUTTON_HOVER, icon_rect, border_radius=10)
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, icon_rect, border_radius=10)
    
    # 绘制设置图标（齿轮形状）
    gear_color = TEXT_COLOR
    gear_radius = icon_size // 4
    gear_center = (icon_x + icon_size // 2, icon_y + icon_size // 2)
    
    # 绘制齿轮中心
    pygame.draw.circle(screen, gear_color, gear_center, gear_radius, 2)
    
    # 绘制齿轮齿
    for i in range(8):
        angle = i * (360 / 8)
        radians = math.radians(angle)
        
        # 外点
        outer_x = gear_center[0] + int(gear_radius * 2 * math.cos(radians))
        outer_y = gear_center[1] + int(gear_radius * 2 * math.sin(radians))
        
        # 内点
        inner_x = gear_center[0] + int(gear_radius * 1.2 * math.cos(radians))
        inner_y = gear_center[1] + int(gear_radius * 1.2 * math.sin(radians))
        
        # 绘制齿轮齿
        pygame.draw.line(screen, gear_color, (inner_x, inner_y), (outer_x, outer_y), 3)
    
    # 绘制设置文字
    settings_text = small_font.render("设置", True, TEXT_COLOR)
    text_x = icon_x + (icon_size - settings_text.get_width()) // 2
    text_y = icon_y + icon_size + 5
    screen.blit(settings_text, (text_x, text_y))
    
    return icon_rect

# 副本选择界面绘制（含BGM播放）
def draw_copy_select():
    # 只绘制内容区域，不绘制主菜单（主菜单由draw_animation或main函数单独绘制）
    
    title_text = menu_font.render("选择副本场景", True, TEXT_COLOR)
    title_rect = title_text.get_rect(center=(config["resolution"][0]//2, 80))
    # 绘制半透明背景，增强标题可读性
    title_bg = pygame.Surface((title_rect.width + 40, title_rect.height + 20), pygame.SRCALPHA)
    pygame.draw.rect(title_bg, (0, 0, 0, 150), (0, 0, title_rect.width + 40, title_rect.height + 20), border_radius=5)
    screen.blit(title_bg, (title_rect.x - 20, title_rect.y - 10))
    screen.blit(title_text, title_rect)

    option_width = 220
    option_height = 120
    spacing = 60
    # 右侧计算，将副本选择按钮放在右侧，增加边距
    start_x = config["resolution"][0] - (3 * option_width + 2 * spacing) - 100
    start_y = (config["resolution"][1] - option_height) // 2 + 20

    hospital_btn = pygame.Rect(start_x, start_y, option_width, option_height)
    hospital_is_hovered = hospital_btn.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, (60, 120, 200), hospital_btn)
    pygame.draw.rect(screen, (100, 180, 255) if hospital_is_hovered else (0, 0, 0), hospital_btn, 2)
    hospital_text_color = (255, 255, 255) if hospital_is_hovered else (200, 200, 200)
    hospital_text = option_font.render("废弃医院", True, hospital_text_color)
    screen.blit(hospital_text, hospital_text.get_rect(center=hospital_btn.center))

    cafe_btn = pygame.Rect(start_x + option_width + spacing, start_y, option_width, option_height)
    cafe_is_hovered = cafe_btn.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, (60, 120, 200), cafe_btn)
    pygame.draw.rect(screen, (100, 180, 255) if cafe_is_hovered else (0, 0, 0), cafe_btn, 2)
    cafe_text_color = (255, 255, 255) if cafe_is_hovered else (200, 200, 200)
    cafe_text = option_font.render("咖啡厅", True, cafe_text_color)
    screen.blit(cafe_text, cafe_text.get_rect(center=cafe_btn.center))

    wedding_btn = pygame.Rect(start_x + 2*(option_width + spacing), start_y, option_width, option_height)
    wedding_is_hovered = wedding_btn.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, (60, 120, 200), wedding_btn)
    pygame.draw.rect(screen, (100, 180, 255) if wedding_is_hovered else (0, 0, 0), wedding_btn, 2)
    wedding_text_color = (255, 255, 255) if wedding_is_hovered else (200, 200, 200)
    wedding_text = option_font.render("结婚现场", True, wedding_text_color)
    screen.blit(wedding_text, wedding_text.get_rect(center=wedding_btn.center))



    # 播放菜单BGM
    if current_bgm != "menu":
        play_bgm("menu")

    return hospital_btn, cafe_btn, wedding_btn

# 游戏信息界面绘制（修复返回值错误，只返回back_btn）
def draw_game_info():
    global screen, info_scroll_y  # 声明使用全局变量
    # 只绘制内容区域，不绘制主菜单（主菜单由draw_animation或main函数单独绘制）
    # 使用公共函数计算面板位置，确保与设置面板一致
    info_x, info_y, info_width, info_height = calculate_panel_position(config["resolution"])
    
    title_text = menu_font.render("游戏信息", True, TEXT_COLOR)
    # 标题显示在面板上方，与面板左对齐
    # 绘制半透明背景，增强标题可读性
    title_bg = pygame.Surface((title_text.get_width() + 20, title_text.get_height() + 10), pygame.SRCALPHA)
    pygame.draw.rect(title_bg, (0, 0, 0, 150), (0, 0, title_text.get_width() + 20, title_text.get_height() + 10), border_radius=3)
    screen.blit(title_bg, (info_x - 10, 50 - 5))
    screen.blit(title_text, (info_x, 50))
    info_bottom_y = info_y + info_height

    # 创建信息面板背景和边框
    pygame.draw.rect(screen, MENU_BG, (info_x, info_y, info_width, info_height))
    pygame.draw.rect(screen, BUTTON_COLOR, (info_x, info_y, info_width, info_height), 2)

    # 定义游戏信息内容
    info_content = [
        "游戏名称：逃离学校剧本",
        "",
        "开发团队信息",
        "",
        "【开发者】",
        "  黄（核心代码实现、功能开发）",
        "  凉乞钞_official(UI样式、动画编辑)"
        "",
        "【策划团队】",
        "  主策划：矢车菊（游戏玩法设计、剧情架构）",
        "",
        "【特邀嘉宾】",
        "  玩法顾问：坚林（提供冒险解谜玩法建议）",
        "",
        "【美术组】",
        "  美术负责人：沫沫（角色/场景美术风格定义）",
        "  视觉设计：筱（UI界面设计、颜色搭配）",
        "  资源制作：京华（图片资源绘制、素材处理）",
        "",
        "【特别鸣谢】",
        "  凉乞钞_official:(一个学C++和.VB语言的小子。在内测时找到了一堆没人能想到的诡异BUG并修复了它,有非同寻常的BUG体质.)",
        "",
        "游戏基础信息",
        "",
        "游戏类型：2D冒险解谜",
        "",
        "操作说明：",
        "  - W/A/S/D：控制角色上下左右移动",
        "  - E：打开大门（靠近大门时使用）",
        "  - 空格：暂停/继续游戏",
        "  - ESC：暂停游戏/关闭菜单",
        "  - 鼠标左键：点击按钮/继续剧情",
        "",
        "副本场景：",
        "  1. 废弃医院（初始场景）：探索医院内部，寻找逃离线索",
        "  2. 咖啡厅（新增场景）：穿过大门进入，解锁更多剧情",
        "  3. 结婚现场（待更新）：后续更新开放",
        "",
        "注意事项：",
        "  - 部分场景存在隐藏线索，仔细探索每个区域",
        "  - 遇到困难时可查看游戏信息获取帮助",
        "  - 建议在高FPS环境下运行，获得最佳体验",
        "",
        "版本信息",
        "  当前版本：v1.0.5",
        "  更新日期：2025年12月",
        "  版权所有：©逃离学校剧本开发团队"
    ]

    line_height = small_font.get_linesize()
    max_line_width = info_width - 40  # 左右各留20像素边距
    
    # 辅助函数：处理单个过长的单词
    def split_long_word(word, max_width):
        if small_font.size(word)[0] <= max_width:
            return [word]
        
        # 在字符级别拆分过长单词
        result = []
        current_part = ''
        for char in word:
            test_part = current_part + char
            if small_font.size(test_part)[0] > max_width:
                result.append(current_part)
                current_part = char
            else:
                current_part = test_part
        if current_part:
            result.append(current_part)
        return result
    
    # 处理文本自动换行
    wrapped_content = []
    for line in info_content:
        if not line.strip():
            wrapped_content.append('')
            continue
            
        # 尝试按单词分割，优先在空格处换行
        words = []
        current_word = ''
        for char in line:
            if char.isspace():
                if current_word:
                    words.append(current_word)
                    current_word = ''
                words.append(' ')
            else:
                current_word += char
        if current_word:
            words.append(current_word)
            
        # 构建换行后的行，包含处理过长单词
        current_line = ''
        for word in words:
            # 如果是空格，直接添加（保持原有的空格处理）
            if word.isspace():
                # 测试添加空格后的行宽
                test_line = current_line + word
                line_width = small_font.size(test_line)[0]
                
                if line_width > max_line_width and current_line:
                    wrapped_content.append(current_line.rstrip())
                    current_line = ''
                else:
                    current_line = test_line
                continue
            
            # 处理非空单词，检查是否需要拆分
            word_parts = split_long_word(word, max_line_width)
            
            for i, part in enumerate(word_parts):
                # 测试添加当前部分后的行宽
                test_line = current_line + (' ' if current_line and i > 0 else '') + part
                line_width = small_font.size(test_line)[0]
                
                # 如果添加后超出宽度且当前行不为空，则换行
                if line_width > max_line_width and current_line:
                    wrapped_content.append(current_line.rstrip())
                    current_line = part
                else:
                    current_line = test_line
                    
        # 添加剩余的文本
        if current_line:
            wrapped_content.append(current_line)
    
    # 计算总高度和滚动区域
    total_height = len(wrapped_content) * line_height
    scrollable_area = max(0, total_height - info_height)

    # 确保滚动位置在有效范围内
    info_scroll_y = max(-scrollable_area, min(0, info_scroll_y))

    # 创建一个裁剪区域，确保文本不会超出容器边界
    clip_rect = pygame.Rect(info_x + 20, info_y, info_width - 40, info_height)
    original_clip = screen.get_clip()  # 保存原始裁剪区域
    screen.set_clip(clip_rect)  # 设置裁剪区域

    # 渲染换行后的文本
    for i, line in enumerate(wrapped_content):
        line_top_y = info_y + i * line_height + info_scroll_y
        line_bottom_y = line_top_y + line_height
        
        # 只有当行与可见区域相交时才渲染
        if line_bottom_y > info_y and line_top_y < info_bottom_y:
            # 渲染文本
            text_surf = small_font.render(line, True, TEXT_COLOR)
            
            # 确保文本不会超出左右边界
            max_text_width = info_width - 40
            text_width = text_surf.get_width()
            
            if text_width > max_text_width:
                # 创建一个与可见区域等宽的临时表面
                clipped_surf = pygame.Surface((max_text_width, line_height), pygame.SRCALPHA)
                clipped_surf.blit(text_surf, (0, 0))
                screen.blit(clipped_surf, (info_x + 20, line_top_y))
            else:
                # 文本宽度正常，直接渲染
                screen.blit(text_surf, (info_x + 20, line_top_y))

    # 恢复原始裁剪区域
    screen.set_clip(original_clip)

    # 绘制滚动条
    if scrollable_area > 0:
        scrollbar_width = 8
        scrollbar_height = max(20, (info_height / total_height) * info_height)  # 确保滚动条有最小高度
        scrollbar_y = info_y + (-info_scroll_y / scrollable_area) * (info_height - scrollbar_height)
        pygame.draw.rect(screen, BUTTON_HOVER, (info_x + info_width - 15, scrollbar_y, scrollbar_width, scrollbar_height), border_radius=3)

    # 播放菜单BGM
    if current_bgm != "menu":
        play_bgm("menu")

    return None

# 绘制指定状态的内容区域到表面上（不包括主菜单）
def draw_content_to_surface(state, surface):
    """将指定状态的内容区域绘制到给定的表面上（不包括主菜单）
    
    Args:
        state: 游戏状态
        surface: 目标表面
    """
    # 保存当前屏幕，然后将绘制目标切换到surface
    global screen, settings_scroll_y, info_scroll_y
    original_screen = screen
    screen = surface
    
    # 清除表面
    screen.fill((0, 0, 0, 0), rect=pygame.Rect(0, 0, config["resolution"][0], config["resolution"][1]))
    
    # 绘制指定状态的内容区域
    if state == GameState.COPY_SELECT:
        title_text = menu_font.render("选择副本场景", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(config["resolution"][0]//2, 80))
        # 绘制半透明背景，增强标题可读性
        title_bg = pygame.Surface((title_rect.width + 40, title_rect.height + 20), pygame.SRCALPHA)
        pygame.draw.rect(title_bg, (0, 0, 0, 150), (0, 0, title_rect.width + 40, title_rect.height + 20), border_radius=5)
        screen.blit(title_bg, (title_rect.x - 20, title_rect.y - 10))
        screen.blit(title_text, title_rect)
        
        option_width = 220
        option_height = 120
        spacing = 60
        # 右侧计算，将副本选择按钮放在右侧，增加边距
        start_x = config["resolution"][0] - (3 * option_width + 2 * spacing) - 100
        start_y = (config["resolution"][1] - option_height) // 2 + 20
        
        hospital_btn = pygame.Rect(start_x, start_y, option_width, option_height)
        hospital_is_hovered = hospital_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), hospital_btn)
        pygame.draw.rect(screen, (100, 180, 255) if hospital_is_hovered else (0, 0, 0), hospital_btn, 2)
        hospital_text_color = (255, 255, 255) if hospital_is_hovered else (200, 200, 200)
        hospital_text = option_font.render("废弃医院", True, hospital_text_color)
        screen.blit(hospital_text, hospital_text.get_rect(center=hospital_btn.center))
        
        cafe_btn = pygame.Rect(start_x + option_width + spacing, start_y, option_width, option_height)
        cafe_is_hovered = cafe_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), cafe_btn)
        pygame.draw.rect(screen, (100, 180, 255) if cafe_is_hovered else (0, 0, 0), cafe_btn, 2)
        cafe_text_color = (255, 255, 255) if cafe_is_hovered else (200, 200, 200)
        cafe_text = option_font.render("咖啡厅", True, cafe_text_color)
        screen.blit(cafe_text, cafe_text.get_rect(center=cafe_btn.center))
        
        wedding_btn = pygame.Rect(start_x + 2*(option_width + spacing), start_y, option_width, option_height)
        wedding_is_hovered = wedding_btn.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(screen, (60, 120, 200), wedding_btn)
        pygame.draw.rect(screen, (100, 180, 255) if wedding_is_hovered else (0, 0, 0), wedding_btn, 2)
        wedding_text_color = (255, 255, 255) if wedding_is_hovered else (200, 200, 200)
        wedding_text = option_font.render("结婚现场", True, wedding_text_color)
        screen.blit(wedding_text, wedding_text.get_rect(center=wedding_btn.center))
        
    elif state == GameState.SETTINGS:
        # 使用公共函数计算面板位置，确保与handle_events一致
        panel_x, panel_y, panel_width, panel_height = calculate_panel_position(config["resolution"])
        
        title_text = menu_font.render("游戏设置", True, TEXT_COLOR)
        # 标题显示在面板上方，与面板左对齐
        # 绘制半透明背景，增强标题可读性
        title_bg = pygame.Surface((title_text.get_width() + 20, title_text.get_height() + 10), pygame.SRCALPHA)
        pygame.draw.rect(title_bg, (0, 0, 0, 150), (0, 0, title_text.get_width() + 20, title_text.get_height() + 10), border_radius=3)
        screen.blit(title_bg, (panel_x - 10, 50 - 5))
        screen.blit(title_text, (panel_x, 50))
        panel_bottom_y = panel_y + panel_height
        
        pygame.draw.rect(screen, MENU_BG, (panel_x, panel_y, panel_width, panel_height))
        pygame.draw.rect(screen, BUTTON_COLOR, (panel_x, panel_y, panel_width, panel_height), 2)
        
        # 滚动容器（所有设置项绘制在滚动表面上）
        scroll_surface = pygame.Surface((panel_width - 40, 1000), pygame.SRCALPHA)
        base_y = 0 + settings_scroll_y  # 已在函数开头声明global，可正常使用
        
        # 分辨率设置
        res_title = option_font.render("分辨率设置", True, TEXT_COLOR)
        scroll_surface.blit(res_title, (0, base_y))
        res_y = base_y + 40
        res_spacing = 30
        for i, (w, h) in enumerate(RESOLUTION_OPTIONS):
            res_text = f"{w} × {h}"
            res_rect = pygame.Rect(0, res_y + i * res_spacing, 200, 30)
            if i == current_res_idx:
                pygame.draw.rect(scroll_surface, SELECTED_COLOR, res_rect, border_radius=3)
            else:
                pygame.draw.rect(scroll_surface, BUTTON_COLOR, res_rect, border_radius=3)
            res_surf = small_font.render(res_text, True, TEXT_COLOR)
            scroll_surface.blit(res_surf, res_surf.get_rect(center=res_rect.center))
        
        # 帧率设置
        fps_title = option_font.render("帧率设置", True, TEXT_COLOR)
        fps_y = res_y + len(RESOLUTION_OPTIONS) * res_spacing + 60
        scroll_surface.blit(fps_title, (0, fps_y))
        # 添加刷新率提示文字
        fps_hint = small_font.render("(刷新率最高以显示器为准)", True, (150, 150, 150))
        scroll_surface.blit(fps_hint, (0, fps_y + 30))
        fps_option_y = fps_y + 60
        for i, fps in enumerate(FPS_OPTIONS):
            fps_rect = pygame.Rect(0, fps_option_y + i * res_spacing, 100, 30)
            if i == current_fps_idx:
                pygame.draw.rect(scroll_surface, SELECTED_COLOR, fps_rect, border_radius=3)
            else:
                pygame.draw.rect(scroll_surface, BUTTON_COLOR, fps_rect, border_radius=3)
            fps_surf = small_font.render(f"{fps} FPS", True, TEXT_COLOR)
            scroll_surface.blit(fps_surf, fps_surf.get_rect(center=fps_rect.center))
        
        # 快捷键设置
        shortcut_title = option_font.render("快捷键设置（点击修改）", True, TEXT_COLOR)
        shortcut_y = fps_option_y + len(FPS_OPTIONS) * res_spacing + 60
        scroll_surface.blit(shortcut_title, (0, shortcut_y))
        shortcut_option_y = shortcut_y + 40
        for i, (name, key) in enumerate(shortcut_items):
            # 快捷键标签
            label_rect = pygame.Rect(0, shortcut_option_y + i * 50, 100, 35)
            pygame.draw.rect(scroll_surface, BUTTON_COLOR, label_rect, border_radius=3)
            label_surf = small_font.render(name, True, TEXT_COLOR)
            scroll_surface.blit(label_surf, label_surf.get_rect(center=label_rect.center))
            
            # 快捷键显示框
            key_rect = pygame.Rect(120, shortcut_option_y + i * 50, 200, 35)
            if editing_shortcut == key:
                pygame.draw.rect(scroll_surface, SELECTED_COLOR, key_rect, border_radius=3)
                key_text = "按任意键修改..."
            else:
                pygame.draw.rect(scroll_surface, BUTTON_COLOR, key_rect, border_radius=3)
                key_text = pygame.key.name(config["shortcuts"][key])
            key_surf = small_font.render(key_text, True, TEXT_COLOR)
            scroll_surface.blit(key_surf, key_surf.get_rect(center=key_rect.center))
            
            # 重置按钮
            reset_rect = pygame.Rect(340, shortcut_option_y + i * 50, 80, 35)
            # 简化悬停检测：直接使用屏幕坐标计算
            # 创建屏幕坐标的矩形用于悬停检测
            screen_reset_rect = pygame.Rect(panel_x + 20 + 340, panel_y + 20 + shortcut_option_y + i * 50 + settings_scroll_y, 80, 35)
            pygame.draw.rect(scroll_surface, RESET_BTN_HOVER if screen_reset_rect.collidepoint(pygame.mouse.get_pos()) else RESET_BTN_COLOR, reset_rect, border_radius=3)
            reset_surf = small_font.render("重置", True, TEXT_COLOR)
            scroll_surface.blit(reset_surf, reset_surf.get_rect(center=reset_rect.center))
        
        # 音量设置（新增滑杆）
        volume_title = option_font.render("音量设置", True, TEXT_COLOR)
        volume_y = shortcut_option_y + len(shortcut_items) * 50 + 60
        scroll_surface.blit(volume_title, (0, volume_y))
        
        # BGM音量滑杆
        bgm_label_y = volume_y + 40
        bgm_label = small_font.render(f"BGM音量: {int(bgm_volume * 100)}%", True, TEXT_COLOR)
        scroll_surface.blit(bgm_label, (0, bgm_label_y))
        bgm_slider_y = bgm_label_y + 30
        bgm_slider_width = 300
        bgm_slider_height = 8
        bgm_slider_rect = pygame.Rect(0, bgm_slider_y, bgm_slider_width, bgm_slider_height)
        pygame.draw.rect(scroll_surface, SLIDER_BG_COLOR, bgm_slider_rect, border_radius=4)
        bgm_fill_width = bgm_slider_width * bgm_volume
        pygame.draw.rect(scroll_surface, SLIDER_FILL_COLOR, (0, bgm_slider_y, bgm_fill_width, bgm_slider_height), border_radius=4)
        bgm_thumb_radius = 12
        bgm_thumb_x = bgm_fill_width - bgm_thumb_radius
        bgm_thumb_y = bgm_slider_y + bgm_slider_height//2 - bgm_thumb_radius
        bgm_thumb_rect = pygame.Rect(bgm_thumb_x, bgm_thumb_y, bgm_thumb_radius*2, bgm_thumb_radius*2)
        # 简化悬停检测：直接使用屏幕坐标计算
        # 创建屏幕坐标的矩形用于悬停检测
        screen_thumb_rect = pygame.Rect(panel_x + 20 + bgm_thumb_x, panel_y + 20 + bgm_thumb_y + settings_scroll_y, bgm_thumb_radius * 2, bgm_thumb_radius * 2)
        thumb_color = SLIDER_THUMB_HOVER_COLOR if screen_thumb_rect.collidepoint(pygame.mouse.get_pos()) else SLIDER_THUMB_COLOR
        pygame.draw.circle(scroll_surface, thumb_color, (bgm_thumb_x + bgm_thumb_radius, bgm_thumb_y + bgm_thumb_radius), bgm_thumb_radius)
        
        # 音效音量滑杆
        sfx_label_y = bgm_slider_y + 50
        sfx_label = small_font.render(f"音效音量: {int(sfx_volume * 100)}%", True, TEXT_COLOR)
        scroll_surface.blit(sfx_label, (0, sfx_label_y))
        sfx_slider_y = sfx_label_y + 30
        sfx_slider_rect = pygame.Rect(0, sfx_slider_y, bgm_slider_width, bgm_slider_height)
        pygame.draw.rect(scroll_surface, SLIDER_BG_COLOR, sfx_slider_rect, border_radius=4)
        sfx_fill_width = bgm_slider_width * sfx_volume
        pygame.draw.rect(scroll_surface, SLIDER_FILL_COLOR, (0, sfx_slider_y, sfx_fill_width, bgm_slider_height), border_radius=4)
        sfx_thumb_x = sfx_fill_width - bgm_thumb_radius
        sfx_thumb_y = sfx_slider_y + bgm_slider_height//2 - bgm_thumb_radius
        sfx_thumb_rect = pygame.Rect(sfx_thumb_x, sfx_thumb_y, bgm_thumb_radius*2, bgm_thumb_radius*2)
        # 简化悬停检测：直接使用屏幕坐标计算
        # 创建屏幕坐标的矩形用于悬停检测
        screen_sfx_thumb_rect = pygame.Rect(panel_x + 20 + sfx_thumb_x, panel_y + 20 + sfx_thumb_y + settings_scroll_y, bgm_thumb_radius * 2, bgm_thumb_radius * 2)
        sfx_thumb_color = SLIDER_THUMB_HOVER_COLOR if screen_sfx_thumb_rect.collidepoint(pygame.mouse.get_pos()) else SLIDER_THUMB_COLOR
        pygame.draw.circle(scroll_surface, sfx_thumb_color, (sfx_thumb_x + bgm_thumb_radius, sfx_thumb_y + bgm_thumb_radius), bgm_thumb_radius)
        
        # 计算滚动范围
        total_content_height = sfx_slider_y + 50
        max_scroll_y = max(0, total_content_height - (panel_height - 40))
        settings_scroll_y = max(-max_scroll_y, min(0, settings_scroll_y))
        
        # 绘制滚动内容（裁剪到面板范围内）
        screen.blit(scroll_surface, (panel_x + 20, panel_y + 20), area=(0, -settings_scroll_y, panel_width - 40, panel_height - 40))
        
        # 滚动条
        if max_scroll_y > 0:
            scrollbar_width = 6
            scrollbar_height = (panel_height - 40) / total_content_height * (panel_height - 40)
            scrollbar_y = panel_y + 20 + (-settings_scroll_y / max_scroll_y) * (panel_height - 40 - scrollbar_height)
            pygame.draw.rect(screen, BUTTON_HOVER, (panel_x + panel_width - 30, scrollbar_y, scrollbar_width, scrollbar_height), border_radius=3)
        
    elif state == GameState.GAME_INFO:
        # 定义信息面板的尺寸和位置
        info_width = 500  # 固定宽度，与设置面板一致
        info_height = config["resolution"][1] - 200
        info_x = config["resolution"][0] - info_width - 100  # 右侧计算，距离右边100像素，增加边距
        info_y = 120
        info_bottom_y = info_y + info_height
        
        title_text = menu_font.render("游戏信息", True, TEXT_COLOR)
        # 标题显示在面板上方，与面板左对齐
        # 绘制半透明背景，增强标题可读性
        title_bg = pygame.Surface((title_text.get_width() + 20, title_text.get_height() + 10), pygame.SRCALPHA)
        pygame.draw.rect(title_bg, (0, 0, 0, 150), (0, 0, title_text.get_width() + 20, title_text.get_height() + 10), border_radius=3)
        screen.blit(title_bg, (info_x - 10, 50 - 5))
        screen.blit(title_text, (info_x, 50))
        
        # 创建信息面板背景和边框
        pygame.draw.rect(screen, MENU_BG, (info_x, info_y, info_width, info_height))
        pygame.draw.rect(screen, BUTTON_COLOR, (info_x, info_y, info_width, info_height), 2)
        
        # 定义游戏信息内容
        info_content = [
            "游戏名称：逃离学校剧本",
            "",
            "📌 开发团队信息",
            "",
            "【开发者】",
            "  主开发者：黄（核心代码实现、功能开发）",
            "",
            "【策划团队】",
            "  主策划：矢车菊（游戏玩法设计、剧情架构）",
            "",
            "【特邀嘉宾】",
            "  玩法顾问：坚林（提供冒险解谜玩法建议）",
            "",
            "【美术组】",
            "  美术负责人：沫沫（角色/场景美术风格定义）",
            "  视觉设计：筱（UI界面设计、颜色搭配）",
            "  资源制作：京华（图片资源绘制、素材处理）",
            "",
            "【特别鸣谢】",
            "  凉乞钞_official:(一个学C++和.VB语言的小子。在内测时找到了一堆没人能想到的诡异BUG并修复了它,有非同寻常的BUG体质.)",
            "",
            "🎮 游戏基础信息",
            "",
            "游戏类型：2D冒险解谜",
            "",
            "操作说明：",
            "  - W/A/S/D：控制角色上下左右移动",
            "  - E：打开大门（靠近大门时使用）",
            "  - 空格：暂停/继续游戏",
            "  - ESC：暂停游戏/关闭菜单",
            "  - 鼠标左键：点击按钮/继续剧情",
            "",
            "副本场景：",
            "  1. 废弃医院（初始场景）：探索医院内部，寻找逃离线索",
            "  2. 咖啡厅（新增场景）：穿过大门进入，解锁更多剧情",
            "  3. 结婚现场（待更新）：后续更新开放",
            "",
            "注意事项：",
            "  - 部分场景存在隐藏线索，仔细探索每个区域",
            "  - 遇到困难时可查看游戏信息获取帮助",
            "  - 建议在60FPS下运行，获得最佳体验",
            "",
            "📅 版本信息",
            "  当前版本：v1.0.1",
            "  更新日期：2025年11月",
            "  版权所有：逃离学校剧本开发团队"
        ]
        
        line_height = small_font.get_linesize()
        max_line_width = info_width - 40  # 左右各留20像素边距
        
        # 辅助函数：处理单个过长的单词
        def split_long_word(word, max_width):
            if small_font.size(word)[0] <= max_width:
                return [word]
            
            # 在字符级别拆分过长单词
            result = []
            current_part = ''
            for char in word:
                test_part = current_part + char
                if small_font.size(test_part)[0] > max_width:
                    result.append(current_part)
                    current_part = char
                else:
                    current_part = test_part
            if current_part:
                result.append(current_part)
            return result
        
        # 处理文本自动换行
        wrapped_content = []
        for line in info_content:
            if not line.strip():
                wrapped_content.append('')
                continue
                
            # 尝试按单词分割，优先在空格处换行
            words = []
            current_word = ''
            for char in line:
                if char.isspace():
                    if current_word:
                        words.append(current_word)
                        current_word = ''
                    words.append(' ')
                else:
                    current_word += char
            if current_word:
                words.append(current_word)
                
            # 构建换行后的行，包含处理过长单词
            current_line = ''
            for word in words:
                # 如果是空格，直接添加（保持原有的空格处理）
                if word.isspace():
                    # 测试添加空格后的行宽
                    test_line = current_line + word
                    line_width = small_font.size(test_line)[0]
                    
                    if line_width > max_line_width and current_line:
                        wrapped_content.append(current_line.rstrip())
                        current_line = ''
                    else:
                        current_line = test_line
                    continue
                
                # 处理非空单词，检查是否需要拆分
                word_parts = split_long_word(word, max_line_width)
                
                for i, part in enumerate(word_parts):
                    # 测试添加当前部分后的行宽
                    test_line = current_line + (' ' if current_line and i > 0 else '') + part
                    line_width = small_font.size(test_line)[0]
                    
                    # 如果添加后超出宽度且当前行不为空，则换行
                    if line_width > max_line_width and current_line:
                        wrapped_content.append(current_line.rstrip())
                        current_line = part
                    else:
                        current_line = test_line
                        
            # 添加剩余的文本
            if current_line:
                wrapped_content.append(current_line)
        
        # 计算总高度和滚动区域
        total_height = len(wrapped_content) * line_height
        scrollable_area = max(0, total_height - info_height)
        
        # 确保滚动位置在有效范围内
        info_scroll_y = max(-scrollable_area, min(0, info_scroll_y))
        
        # 创建一个裁剪区域，确保文本不会超出容器边界
        clip_rect = pygame.Rect(info_x + 20, info_y, info_width - 40, info_height)
        original_clip = screen.get_clip()  # 保存原始裁剪区域
        screen.set_clip(clip_rect)  # 设置裁剪区域
        
        # 渲染换行后的文本
        for i, line in enumerate(wrapped_content):
            line_top_y = info_y + i * line_height + info_scroll_y
            line_bottom_y = line_top_y + line_height
            
            # 只有当行与可见区域相交时才渲染
            if line_bottom_y > info_y and line_top_y < info_bottom_y:
                # 渲染文本
                text_surf = small_font.render(line, True, TEXT_COLOR)
                
                # 确保文本不会超出左右边界
                max_text_width = info_width - 40
                text_width = text_surf.get_width()
                
                if text_width > max_text_width:
                    # 创建一个与可见区域等宽的临时表面
                    clipped_surf = pygame.Surface((max_text_width, line_height), pygame.SRCALPHA)
                    clipped_surf.blit(text_surf, (0, 0))
                    screen.blit(clipped_surf, (info_x + 20, line_top_y))
                else:
                    # 文本宽度正常，直接渲染
                    screen.blit(text_surf, (info_x + 20, line_top_y))
        
        # 恢复原始裁剪区域
        screen.set_clip(original_clip)
        
        # 绘制滚动条
        if scrollable_area > 0:
            scrollbar_width = 8
            scrollbar_height = max(20, (info_height / total_height) * info_height)  # 确保滚动条有最小高度
            scrollbar_y = info_y + (-info_scroll_y / scrollable_area) * (info_height - scrollbar_height)
            pygame.draw.rect(screen, BUTTON_HOVER, (info_x + info_width - 15, scrollbar_y, scrollbar_width, scrollbar_height), border_radius=3)
    
    # 恢复原来的屏幕
    screen = original_screen

# 动画绘制逻辑 - 实现绿框和红框都参与动画
def draw_animation():
    """绘制滑入滑出动画，主界面旧窗口退出动画为后退慢慢消失
    实现效果：
    1. 主菜单（红圈内容）保持固定位置
    2. 旧窗口（当前状态）后退并慢慢消失
    3. 新窗口（下一状态）从右侧滑入
    4. 动画流畅自然
    
    Returns:
        bool: 动画是否完成
    """
    global animation_progress, screen
    
    # 1. 清除整个屏幕，确保没有任何残留内容
    screen.fill(BG_COLOR)
    
    # 2. 动画参数
    content_width = 500
    content_x = config["resolution"][0] - content_width - 100
    
    # 3. 计算动画进度
    progress = animation_progress
    
    # 4. 绘制主菜单（红圈内容），保持固定位置，不参与动画
    draw_main_menu()
    
    # 5. 绘制旧窗口（当前状态）的退出动画：后退慢慢消失
    if prev_state != GameState.MAIN_MENU:
        # 保存原始屏幕
        original_screen = screen
        
        # 创建旧窗口的临时表面
        old_surface = pygame.Surface(config["resolution"], pygame.SRCALPHA)
        screen = old_surface
        
        # 绘制旧窗口内容
        if prev_state == GameState.COPY_SELECT:
            draw_copy_select()
        elif prev_state == GameState.SETTINGS:
            draw_settings()
        elif prev_state == GameState.GAME_INFO:
            draw_game_info()
        
        # 恢复屏幕
        screen = original_screen
        
        # 旧窗口使用自己状态对应的slide_distance
        if prev_state == GameState.COPY_SELECT:
            old_slide_distance = 400  # 开始游戏的动画范围更大
        else:
            old_slide_distance = 200  # 其他状态的正常动画范围
        
        # 旧窗口退出动画：向后退并慢慢消失
        old_window_offset = int(old_slide_distance * progress)  # 向后退的距离，使用旧窗口自己的slide_distance
        old_window_alpha = int(255 * (1 - progress))  # 透明度从255到0
        
        # 应用透明度
        old_surface.set_alpha(old_window_alpha)
        
        # 绘制旧窗口，向后退
        screen.blit(old_surface, (old_window_offset, 0))
    
    # 6. 绘制新窗口（下一状态）的进入动画：从右侧滑入
    if next_state != GameState.MAIN_MENU:
        # 保存原始屏幕
        original_screen = screen
        
        # 创建新窗口的临时表面
        new_surface = pygame.Surface(config["resolution"], pygame.SRCALPHA)
        screen = new_surface
        
        # 绘制新窗口内容
        if next_state == GameState.COPY_SELECT:
            draw_copy_select()
        elif next_state == GameState.SETTINGS:
            draw_settings()
        elif next_state == GameState.GAME_INFO:
            draw_game_info()
        
        # 恢复屏幕
        screen = original_screen
        
        # 新窗口使用自己状态对应的slide_distance
        if next_state == GameState.COPY_SELECT:
            new_slide_distance = 400  # 开始游戏的动画范围更大
        else:
            new_slide_distance = 200  # 其他状态的正常动画范围
        
        # 新窗口进入动画：从右侧滑入
        new_window_offset = int(new_slide_distance * (1 - progress))  # 从右侧滑入的距离，使用新窗口自己的slide_distance
        new_window_x = content_x + new_window_offset
        
        # 绘制新窗口，从右侧滑入
        screen.blit(new_surface, (new_window_x - content_x, 0))
    
    # 7. 更新动画进度 - 调整不同状态的动画速度
    if next_state in [GameState.SETTINGS, GameState.GAME_INFO]:
        animation_progress += 0.12  # 设置和游戏信息的动画速度更快，60FPS下约0.15秒完成
    elif next_state == GameState.COPY_SELECT:
        animation_progress += 0.08  # 开始游戏的动画速度适中，60FPS下约0.2秒完成
    else:
        animation_progress += 0.06  # 其他状态的默认速度
    
    # 8. 检查动画是否完成
    if animation_progress >= 1.0:
        animation_progress = 0.0
        return True
    return False

# 退出确认弹窗绘制
def draw_quit_confirm():
    screen.fill(BG_COLOR)
    
    # 绘制半透明遮罩
    mask = pygame.Surface(config["resolution"], pygame.SRCALPHA)
    pygame.draw.rect(mask, (0, 0, 0, 150), mask.get_rect())
    screen.blit(mask, (0, 0))
    
    # 绘制确认窗口
    confirm_width = 400
    confirm_height = 200
    confirm_x = (config["resolution"][0] - confirm_width) // 2
    confirm_y = (config["resolution"][1] - confirm_height) // 2
    
    pygame.draw.rect(screen, MENU_BG, (confirm_x, confirm_y, confirm_width, confirm_height))
    pygame.draw.rect(screen, BUTTON_COLOR, (confirm_x, confirm_y, confirm_width, confirm_height), 2)
    
    # 标题
    title_text = menu_font.render("是否退出游戏？", True, TEXT_COLOR)
    title_rect = title_text.get_rect(center=(confirm_x + confirm_width//2, confirm_y + 40))
    screen.blit(title_text, title_rect)
    
    # 按钮配置
    btn_width = 120
    btn_height = 45
    btn_spacing = 40
    btn_start_x = confirm_x + (confirm_width - (2 * btn_width + btn_spacing)) // 2
    btn_y = confirm_y + confirm_height - 80
    
    # 确认按钮
    confirm_btn = pygame.Rect(btn_start_x, btn_y, btn_width, btn_height)
    confirm_is_hovered = confirm_btn.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, (200, 60, 60), confirm_btn)
    pygame.draw.rect(screen, (255, 0, 0) if confirm_is_hovered else (0, 0, 0), confirm_btn, 2)
    confirm_text_color = (255, 255, 255) if confirm_is_hovered else (200, 200, 200)
    confirm_text = option_font.render("确认", True, confirm_text_color)
    confirm_text_rect = confirm_text.get_rect(center=confirm_btn.center)
    screen.blit(confirm_text, confirm_text_rect)
    
    # 取消按钮
    cancel_btn = pygame.Rect(btn_start_x + btn_width + btn_spacing, btn_y, btn_width, btn_height)
    cancel_is_hovered = cancel_btn.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, (60, 120, 200), cancel_btn)
    pygame.draw.rect(screen, (100, 180, 255) if cancel_is_hovered else (0, 0, 0), cancel_btn, 2)
    cancel_text_color = (255, 255, 255) if cancel_is_hovered else (200, 200, 200)
    cancel_text = option_font.render("取消", True, cancel_text_color)
    cancel_text_rect = cancel_text.get_rect(center=cancel_btn.center)
    screen.blit(cancel_text, cancel_text_rect)
    
    return confirm_btn, cancel_btn

# 设置界面绘制（修复settings_scroll_y未定义：显式声明全局变量在函数开头）
def draw_settings():
    global screen, settings_scroll_y  # 关键修复：在函数开头声明global，避免UnboundLocalError
    # 只绘制内容区域，不绘制主菜单（主菜单由draw_animation或main函数单独绘制）
    # 使用公共函数计算面板位置，确保与handle_events一致
    panel_x, panel_y, panel_width, panel_height = calculate_panel_position(config["resolution"])
    
    title_text = menu_font.render("游戏设置", True, TEXT_COLOR)
    # 标题显示在面板上方，与面板左对齐
    # 绘制半透明背景，增强标题可读性
    title_bg = pygame.Surface((title_text.get_width() + 20, title_text.get_height() + 10), pygame.SRCALPHA)
    pygame.draw.rect(title_bg, (0, 0, 0, 150), (0, 0, title_text.get_width() + 20, title_text.get_height() + 10), border_radius=3)
    screen.blit(title_bg, (panel_x - 10, 50 - 5))
    screen.blit(title_text, (panel_x, 50))
    panel_bottom_y = panel_y + panel_height

    pygame.draw.rect(screen, MENU_BG, (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, BUTTON_COLOR, (panel_x, panel_y, panel_width, panel_height), 2)

    # 滚动容器（所有设置项绘制在滚动表面上）
    scroll_surface = pygame.Surface((panel_width - 40, 1000), pygame.SRCALPHA)
    base_y = 0 + settings_scroll_y  # 已在函数开头声明global，可正常使用

    # 分辨率设置
    res_title = option_font.render("分辨率设置", True, TEXT_COLOR)
    scroll_surface.blit(res_title, (0, base_y))
    res_y = base_y + 40
    res_spacing = 30
    for i, (w, h) in enumerate(RESOLUTION_OPTIONS):
        res_text = f"{w} × {h}"
        res_rect = pygame.Rect(0, res_y + i * res_spacing, 200, 30)
        if i == current_res_idx:
            pygame.draw.rect(scroll_surface, SELECTED_COLOR, res_rect, border_radius=3)
        else:
            pygame.draw.rect(scroll_surface, BUTTON_COLOR, res_rect, border_radius=3)
        res_surf = small_font.render(res_text, True, TEXT_COLOR)
        scroll_surface.blit(res_surf, res_surf.get_rect(center=res_rect.center))

    # 帧率设置
    fps_title = option_font.render("帧率设置", True, TEXT_COLOR)
    fps_y = res_y + len(RESOLUTION_OPTIONS) * res_spacing + 60
    scroll_surface.blit(fps_title, (0, fps_y))
    # 添加刷新率提示文字
    fps_hint = small_font.render("(刷新率最高以显示器为准)", True, (150, 150, 150))
    scroll_surface.blit(fps_hint, (0, fps_y + 30))
    fps_option_y = fps_y + 60
    for i, fps in enumerate(FPS_OPTIONS):
        fps_rect = pygame.Rect(0, fps_option_y + i * res_spacing, 100, 30)
        if i == current_fps_idx:
            pygame.draw.rect(scroll_surface, SELECTED_COLOR, fps_rect, border_radius=3)
        else:
            pygame.draw.rect(scroll_surface, BUTTON_COLOR, fps_rect, border_radius=3)
        fps_surf = small_font.render(f"{fps} FPS", True, TEXT_COLOR)
        scroll_surface.blit(fps_surf, fps_surf.get_rect(center=fps_rect.center))

    # 快捷键设置
    shortcut_title = option_font.render("快捷键设置（点击修改）", True, TEXT_COLOR)
    shortcut_y = fps_option_y + len(FPS_OPTIONS) * res_spacing + 60
    scroll_surface.blit(shortcut_title, (0, shortcut_y))
    shortcut_option_y = shortcut_y + 40
    for i, (name, key) in enumerate(shortcut_items):
        # 快捷键标签
        label_rect = pygame.Rect(0, shortcut_option_y + i * 50, 100, 35)
        pygame.draw.rect(scroll_surface, BUTTON_COLOR, label_rect, border_radius=3)
        label_surf = small_font.render(name, True, TEXT_COLOR)
        scroll_surface.blit(label_surf, label_surf.get_rect(center=label_rect.center))

        # 快捷键显示框
        key_rect = pygame.Rect(120, shortcut_option_y + i * 50, 200, 35)
        if editing_shortcut == key:
            pygame.draw.rect(scroll_surface, SELECTED_COLOR, key_rect, border_radius=3)
            key_text = "按任意键修改..."
        else:
            pygame.draw.rect(scroll_surface, BUTTON_COLOR, key_rect, border_radius=3)
            key_text = pygame.key.name(config["shortcuts"][key])
        key_surf = small_font.render(key_text, True, TEXT_COLOR)
        scroll_surface.blit(key_surf, key_surf.get_rect(center=key_rect.center))

        # 重置按钮
        reset_rect = pygame.Rect(340, shortcut_option_y + i * 50, 80, 35)
        # 简化悬停检测：直接使用屏幕坐标计算
        # 创建屏幕坐标的矩形用于悬停检测
        screen_reset_rect = pygame.Rect(panel_x + 20 + 340, panel_y + 20 + shortcut_option_y + i * 50 + settings_scroll_y, 80, 35)
        pygame.draw.rect(scroll_surface, RESET_BTN_HOVER if screen_reset_rect.collidepoint(pygame.mouse.get_pos()) else RESET_BTN_COLOR, reset_rect, border_radius=3)
        reset_surf = small_font.render("重置", True, TEXT_COLOR)
        scroll_surface.blit(reset_surf, reset_surf.get_rect(center=reset_rect.center))

    # 音量设置（新增滑杆）
    volume_title = option_font.render("音量设置", True, TEXT_COLOR)
    volume_y = shortcut_option_y + len(shortcut_items) * 50 + 60
    scroll_surface.blit(volume_title, (0, volume_y))

    # BGM音量滑杆
    bgm_label_y = volume_y + 40
    bgm_label = small_font.render(f"BGM音量: {int(bgm_volume * 100)}%", True, TEXT_COLOR)
    scroll_surface.blit(bgm_label, (0, bgm_label_y))
    bgm_slider_y = bgm_label_y + 30
    bgm_slider_width = 300
    bgm_slider_height = 8
    bgm_slider_rect = pygame.Rect(0, bgm_slider_y, bgm_slider_width, bgm_slider_height)
    pygame.draw.rect(scroll_surface, SLIDER_BG_COLOR, bgm_slider_rect, border_radius=4)
    bgm_fill_width = bgm_slider_width * bgm_volume
    pygame.draw.rect(scroll_surface, SLIDER_FILL_COLOR, (0, bgm_slider_y, bgm_fill_width, bgm_slider_height), border_radius=4)
    bgm_thumb_radius = 12
    bgm_thumb_x = bgm_fill_width - bgm_thumb_radius
    bgm_thumb_y = bgm_slider_y + bgm_slider_height//2 - bgm_thumb_radius
    bgm_thumb_rect = pygame.Rect(bgm_thumb_x, bgm_thumb_y, bgm_thumb_radius*2, bgm_thumb_radius*2)
    # 简化悬停检测：直接使用屏幕坐标计算
    # 创建屏幕坐标的矩形用于悬停检测
    screen_thumb_rect = pygame.Rect(panel_x + 20 + bgm_thumb_x, panel_y + 20 + bgm_thumb_y + settings_scroll_y, bgm_thumb_radius * 2, bgm_thumb_radius * 2)
    thumb_color = SLIDER_THUMB_HOVER_COLOR if screen_thumb_rect.collidepoint(pygame.mouse.get_pos()) else SLIDER_THUMB_COLOR
    pygame.draw.circle(scroll_surface, thumb_color, (bgm_thumb_x + bgm_thumb_radius, bgm_thumb_y + bgm_thumb_radius), bgm_thumb_radius)

    # 音效音量滑杆
    sfx_label_y = bgm_slider_y + 50
    sfx_label = small_font.render(f"音效音量: {int(sfx_volume * 100)}%", True, TEXT_COLOR)
    scroll_surface.blit(sfx_label, (0, sfx_label_y))
    sfx_slider_y = sfx_label_y + 30
    sfx_slider_rect = pygame.Rect(0, sfx_slider_y, bgm_slider_width, bgm_slider_height)
    pygame.draw.rect(scroll_surface, SLIDER_BG_COLOR, sfx_slider_rect, border_radius=4)
    sfx_fill_width = bgm_slider_width * sfx_volume
    pygame.draw.rect(scroll_surface, SLIDER_FILL_COLOR, (0, sfx_slider_y, sfx_fill_width, bgm_slider_height), border_radius=4)
    sfx_thumb_x = sfx_fill_width - bgm_thumb_radius
    sfx_thumb_y = sfx_slider_y + bgm_slider_height//2 - bgm_thumb_radius
    sfx_thumb_rect = pygame.Rect(sfx_thumb_x, sfx_thumb_y, bgm_thumb_radius*2, bgm_thumb_radius*2)
    # 简化悬停检测：直接使用屏幕坐标计算
    # 创建屏幕坐标的矩形用于悬停检测
    screen_sfx_thumb_rect = pygame.Rect(panel_x + 20 + sfx_thumb_x, panel_y + 20 + sfx_thumb_y + settings_scroll_y, bgm_thumb_radius * 2, bgm_thumb_radius * 2)
    sfx_thumb_color = SLIDER_THUMB_HOVER_COLOR if screen_sfx_thumb_rect.collidepoint(pygame.mouse.get_pos()) else SLIDER_THUMB_COLOR
    pygame.draw.circle(scroll_surface, sfx_thumb_color, (sfx_thumb_x + bgm_thumb_radius, sfx_thumb_y + bgm_thumb_radius), bgm_thumb_radius)

    # 计算滚动范围
    total_content_height = sfx_slider_y + 50
    max_scroll_y = max(0, total_content_height - (panel_height - 40))
    settings_scroll_y = max(-max_scroll_y, min(0, settings_scroll_y))

    # 绘制滚动内容（裁剪到面板范围内）
    screen.blit(scroll_surface, (panel_x + 20, panel_y + 20), area=(0, -settings_scroll_y, panel_width - 40, panel_height - 40))

    # 滚动条
    if max_scroll_y > 0:
        scrollbar_width = 6
        scrollbar_height = (panel_height - 40) / total_content_height * (panel_height - 40)
        scrollbar_y = panel_y + 20 + (-settings_scroll_y / max_scroll_y) * (panel_height - 40 - scrollbar_height)
        pygame.draw.rect(screen, BUTTON_HOVER, (panel_x + panel_width - 30, scrollbar_y, scrollbar_width, scrollbar_height), border_radius=3)

    # 播放菜单BGM
    if current_bgm != "menu":
        play_bgm("menu")

    # 返回所有可交互元素的Rect（用于事件处理）
    # 重建设置项的屏幕坐标Rect（用于事件判断）
    res_rects = []
    for i, (w, h) in enumerate(RESOLUTION_OPTIONS):
        res_rect = pygame.Rect(panel_x + 20, panel_y + 20 + res_y + i * res_spacing + settings_scroll_y, 200, 30)
        res_rects.append((res_rect, i))

    fps_rects = []
    for i, fps in enumerate(FPS_OPTIONS):
        fps_rect = pygame.Rect(panel_x + 20, panel_y + 20 + fps_option_y + i * res_spacing + settings_scroll_y, 100, 30)
        fps_rects.append((fps_rect, i))

    shortcut_rects = []
    reset_rects = []
    for i, (name, key) in enumerate(shortcut_items):
        shortcut_rect = pygame.Rect(panel_x + 20 + 120, panel_y + 20 + shortcut_option_y + i * 50 + settings_scroll_y, 200, 35)
        shortcut_rects.append((shortcut_rect, key))
        reset_rect = pygame.Rect(panel_x + 20 + 340, panel_y + 20 + shortcut_option_y + i * 50 + settings_scroll_y, 80, 35)
        reset_rects.append((reset_rect, key))

    # 音量滑杆的屏幕坐标Rect
    bgm_slider_screen_rect = pygame.Rect(panel_x + 20, panel_y + 20 + bgm_slider_y + settings_scroll_y, bgm_slider_width, bgm_slider_height)
    bgm_thumb_screen_rect = pygame.Rect(
        panel_x + 20 + bgm_thumb_x,
        panel_y + 20 + bgm_thumb_y + settings_scroll_y,
        bgm_thumb_radius * 2,
        bgm_thumb_radius * 2
    )
    sfx_slider_screen_rect = pygame.Rect(panel_x + 20, panel_y + 20 + sfx_slider_y + settings_scroll_y, bgm_slider_width, bgm_slider_height)
    sfx_thumb_screen_rect = pygame.Rect(
        panel_x + 20 + sfx_thumb_x,
        panel_y + 20 + sfx_thumb_y + settings_scroll_y,
        bgm_thumb_radius * 2,
        bgm_thumb_radius * 2
    )

    # 返回所有可交互元素的Rect（用于事件处理），不包括返回按钮
    return None, shortcut_rects, reset_rects, res_rects, fps_rects, bgm_slider_screen_rect, sfx_slider_screen_rect, bgm_thumb_screen_rect, sfx_thumb_screen_rect
# 事件处理函数（修复global声明位置错误）

# 事件处理函数
def handle_events():
    # 所有需要修改的全局变量，统一在函数开头声明
    global is_paused, gate_is_open, cafe_gate_is_open, gate_cooldown
    global dialog_shown, current_dialog_index, current_state, editing_shortcut
    global info_scroll_y, settings_scroll_y, current_res_idx, current_fps_idx, current_fps, camera_x, camera_y, config
    global bgm_volume, sfx_volume, dragging_bgm_slider, dragging_sfx_slider
    global bgm_slider_rect_global, sfx_slider_rect_global, screen, key_states, show_input_tip
    # 动画相关全局变量
    global is_animating, prev_state, next_state
    
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 键盘按键事件 - 按下
        if event.type == pygame.KEYDOWN:
            # 暂停/继续游戏（空格或ESC）
            if event.key in [pygame.K_SPACE, pygame.K_ESCAPE]:
                if current_state in [GameState.HOSPITAL, GameState.CAFE] and current_state != GameState.DIALOG:
                    is_paused = not is_paused
                    if is_paused:
                        pygame.mixer.music.pause()  # 暂停BGM
                    else:
                        pygame.mixer.music.unpause()  # 恢复BGM

            # 更新按键状态字典，解决中文输入法问题
            for action, key_code in config["shortcuts"].items():
                if event.key == key_code:
                    key_states[action] = True
                    # 当玩家按下移动键时，隐藏输入法提示
                    if action in ['move_up', 'move_down', 'move_left', 'move_right']:
                        show_input_tip = False

            # 快捷键编辑确认
            if editing_shortcut:
                if event.key != pygame.K_ESCAPE:  # 按ESC取消编辑
                    config["shortcuts"][editing_shortcut] = event.key
                editing_shortcut = None

            # 开门功能（E键，含冷却机制）
            if event.key == config["shortcuts"]["open_gate"] and not is_paused and current_state != GameState.DIALOG:
                player_rect = pygame.Rect(
                    player.x - player.width//2,
                    player.y - player.height//2,
                    player.width,
                    player.height
                )
                if current_state == GameState.HOSPITAL:
                    if is_player_near_gate(player_rect) and gate_cooldown == 0:
                        if not gate_is_open:
                            gate_is_open = True
                            play_sfx(gate_sound)
                        else:
                            gate_is_open = False
                        gate_cooldown = 60  # 1秒冷却（避免重复触发）
                elif current_state == GameState.CAFE:
                    if is_player_near_cafe_gate(player_rect):
                        if not cafe_gate_is_open:
                            cafe_gate_is_open = True
                        else:
                            cafe_gate_is_open = False
                        play_sfx(gate_sound)

            # M键静音（BGM+音效同时静音/恢复）
            if event.key == pygame.K_m:
                current_bgm_vol = pygame.mixer.music.get_volume()
                if current_bgm_vol > 0 or sfx_volume > 0:
                    # 静音：保存当前音量并设置为0
                    bgm_volume = current_bgm_vol
                    sfx_volume = 0.0  # 确保设置为完全静音（0%）
                    pygame.mixer.music.set_volume(0.0)
                    if gate_sound:
                        gate_sound.set_volume(0.0)
                    print("🔇 已静音（BGM+音效）")
                else:
                    # 恢复音量 - 确保恢复的音量在有效范围内
                    restored_bgm_volume = max(0.0, min(1.0, bgm_volume))
                    restored_sfx_volume = 0.5  # 默认恢复到50%
                    pygame.mixer.music.set_volume(restored_bgm_volume)
                    sfx_volume = restored_sfx_volume
                    if gate_sound:
                        gate_sound.set_volume(restored_sfx_volume)
                    print("🔊 已恢复音量")

        # 键盘按键事件 - 释放
        if event.type == pygame.KEYUP:
            # 更新按键状态字典，解决中文输入法问题
            for action, key_code in config["shortcuts"].items():
                if event.key == key_code:
                    key_states[action] = False

        # 鼠标滚轮事件（游戏信息/设置界面滚动）
        if event.type == pygame.MOUSEWHEEL:
            if not is_paused:  # 暂停时不响应滚动（优化体验）
                if current_state == GameState.GAME_INFO:
                    # 滚动速度设置为20像素
                    scroll_speed = 20
                    info_scroll_y += event.y * scroll_speed
                elif current_state == GameState.SETTINGS:
                    settings_scroll_y += event.y * 20

        # 鼠标点击事件（所有界面按钮交互）
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                # 主菜单界面 - 无论当前状态是什么，都检查主菜单按钮，因为我们保留了主菜单
                start_btn, setting_btn, info_btn, quit_btn = draw_main_menu()
                
                # 动画正在运行时，忽略所有按钮点击（除了退出确认）
                if not is_animating:
                    if start_btn.collidepoint(mouse_pos):
                        # 只有当前状态不是副本选择时，才触发动画
                        if current_state != GameState.COPY_SELECT:
                            # 触发动画，从当前状态切换到副本选择
                            is_animating = True
                            prev_state = current_state
                            next_state = GameState.COPY_SELECT
                            animation_progress = 0.0  # 重置动画进度，确保每次动画都从头开始
                    elif setting_btn.collidepoint(mouse_pos):
                        # 只有当前状态不是设置时，才触发动画
                        if current_state != GameState.SETTINGS:
                            # 触发动画，从当前状态切换到设置
                            is_animating = True
                            prev_state = current_state
                            next_state = GameState.SETTINGS
                            animation_progress = 0.0  # 重置动画进度，确保每次动画都从头开始
                    elif info_btn.collidepoint(mouse_pos):
                        # 只有当前状态不是游戏信息时，才触发动画
                        if current_state != GameState.GAME_INFO:
                            # 触发动画，从当前状态切换到游戏信息
                            is_animating = True
                            prev_state = current_state
                            next_state = GameState.GAME_INFO
                            animation_progress = 0.0  # 重置动画进度，确保每次动画都从头开始
                    elif quit_btn.collidepoint(mouse_pos):
                        # 显示退出确认弹窗，不使用动画
                        current_state = GameState.QUIT_CONFIRM

                # 处理当前状态的按钮点击，无论动画是否正在播放
                # 退出确认弹窗
                if current_state == GameState.QUIT_CONFIRM:
                    confirm_btn, cancel_btn = draw_quit_confirm()
                    if confirm_btn.collidepoint(mouse_pos):
                        # 确认退出
                        pygame.quit()
                        sys.exit()
                    elif cancel_btn.collidepoint(mouse_pos):
                        # 取消退出，返回主菜单
                        current_state = GameState.MAIN_MENU

                # 副本选择界面
                elif current_state == GameState.COPY_SELECT:
                    hospital_btn, cafe_btn, wedding_btn = draw_copy_select()
                    if hospital_btn.collidepoint(mouse_pos):
                        # 进入废弃医院场景
                        current_state = GameState.HOSPITAL
                        # 重置玩家位置和大门状态
                        player.x = player.start_x
                        player.y = player.start_y
                        gate_is_open = False
                        gate_cooldown = 0
                        dialog_shown = False
                        current_dialog_index = 0
                        # 重置输入法提示状态
                        show_input_tip = True
                    elif cafe_btn.collidepoint(mouse_pos):
                        # 进入咖啡厅场景
                        current_state = GameState.CAFE
                        # 重置玩家位置和咖啡厅大门状态
                        player.x = CAFE_MAP_WIDTH // 2
                        player.y = CAFE_FLOOR_HEIGHT // 2
                        cafe_gate_is_open = False
                        # 重置输入法提示状态
                        show_input_tip = True
                    elif wedding_btn.collidepoint(mouse_pos):
                        # 结婚现场暂未开放，显示提示
                        print("💍 结婚现场副本暂未开放，敬请期待后续更新！")

                # 游戏信息界面
                elif current_state == GameState.GAME_INFO:
                    draw_game_info()  # 修复返回值解包错误

                # 设置界面（处理分辨率、帧率、快捷键、音量滑杆）
                elif current_state == GameState.SETTINGS:
                    back_btn, shortcut_rects, reset_rects, res_rects, fps_rects, bgm_slider_rect, sfx_slider_rect, bgm_thumb_rect, sfx_thumb_rect = draw_settings()
                    # 不再处理返回按钮，因为已经删除了
                    # 分辨率选择
                    for res_rect, idx in res_rects:
                        if res_rect.collidepoint(mouse_pos):
                            current_res_idx = idx
                            config["resolution"] = RESOLUTION_OPTIONS[idx]
                            global screen
                            screen = pygame.display.set_mode(config["resolution"], pygame.RESIZABLE)
                    # 帧率选择
                    for fps_rect, idx in fps_rects:
                        if fps_rect.collidepoint(mouse_pos):
                            current_fps_idx = idx
                            current_fps = FPS_OPTIONS[idx]
                    # 快捷键编辑
                    for shortcut_rect, key in shortcut_rects:
                        if shortcut_rect.collidepoint(mouse_pos):
                            editing_shortcut = key
                    # 快捷键重置
                    for reset_rect, key in reset_rects:
                        if reset_rect.collidepoint(mouse_pos):
                            config["shortcuts"][key] = DEFAULT_SHORTCUTS[key]
                    # BGM滑杆拖拽启动（点击滑杆或滑块）
                    if bgm_thumb_rect.collidepoint(mouse_pos) or bgm_slider_rect.collidepoint(mouse_pos):
                        dragging_bgm_slider = True
                        # 保存滑块rect到全局变量，用于鼠标移动事件处理
                        bgm_slider_rect_global = bgm_slider_rect
                        # 使用正确的坐标调整方式计算鼠标在滑杆上的位置
                        # 与draw_settings函数中相同的坐标调整逻辑
                        mouse_x, mouse_y = mouse_pos
                        # 使用calculate_panel_position函数获取面板位置
                        panel_x, panel_y, panel_width, panel_height = calculate_panel_position(config["resolution"])
                        offset_x = panel_x + 20
                        adjusted_mouse_pos_x = mouse_x - offset_x
                        
                        # 点击滑杆直接定位到点击位置 - 添加边界检查确保音量值在0-100%范围
                        slider_x = adjusted_mouse_pos_x
                        raw_volume = slider_x / bgm_slider_rect.width
                        # 严格边界检查，确保音量在0.0-1.0范围内
                        bgm_volume = max(0.0, min(1.0, raw_volume))
                        pygame.mixer.music.set_volume(bgm_volume)
                        print(f"BGM滑块点击: 位置={slider_x}, 音量={bgm_volume*100:.0f}%")
                    # 音效滑杆拖拽启动（点击滑杆或滑块）
                    if sfx_thumb_rect.collidepoint(mouse_pos) or sfx_slider_rect.collidepoint(mouse_pos):
                        dragging_sfx_slider = True
                        # 保存滑块rect到全局变量，用于鼠标移动事件处理
                        sfx_slider_rect_global = sfx_slider_rect
                        # 使用正确的坐标调整方式计算鼠标在滑杆上的位置
                        # 与draw_settings函数中相同的坐标调整逻辑
                        mouse_x, mouse_y = mouse_pos
                        # 使用calculate_panel_position函数获取面板位置
                        panel_x, panel_y, panel_width, panel_height = calculate_panel_position(config["resolution"])
                        offset_x = panel_x + 20
                        adjusted_mouse_pos_x = mouse_x - offset_x
                        
                        # 点击滑杆直接定位到点击位置 - 添加边界检查确保音量值在0-100%范围
                        slider_x = adjusted_mouse_pos_x
                        raw_volume = slider_x / sfx_slider_rect.width
                        # 严格边界检查，确保音量在0.0-1.0范围内
                        sfx_volume = max(0.0, min(1.0, raw_volume))
                        if gate_sound:
                            gate_sound.set_volume(sfx_volume)
                        print(f"SFX滑块点击: 位置={slider_x}, 音量={sfx_volume*100:.0f}%")

                # 剧情对话框（点击继续/关闭）
                elif current_state == GameState.DIALOG:
                    current_dialog_index += 1
                    if current_dialog_index >= len(dialog_content):
                        dialog_shown = False
                        current_state = GameState.HOSPITAL  # 返回游戏场景

                # 暂停界面按钮（存档/设置/返回副本选择）
        if is_paused and current_state in [GameState.HOSPITAL, GameState.CAFE]:
            # 存档按钮
            btn_height = 50
            btn_spacing = 30
            
            save_btn_width = 150
            save_btn_y = (config["resolution"][1] // 2) - 100
            save_btn = pygame.Rect(
                config["resolution"][0]//2 - save_btn_width//2,
                save_btn_y,
                save_btn_width,
                btn_height
            )
            
            # 设置按钮
            settings_btn_width = 150
            settings_btn_y = save_btn_y + btn_height + btn_spacing
            settings_btn = pygame.Rect(
                config["resolution"][0]//2 - settings_btn_width//2,
                settings_btn_y,
                settings_btn_width,
                btn_height
            )
            
            # 返回副本选择按钮
            back_btn_width = 200
            back_btn_y = settings_btn_y + btn_height + btn_spacing
            back_btn = pygame.Rect(
                config["resolution"][0]//2 - back_btn_width//2,
                back_btn_y,
                back_btn_width,
                btn_height
            )
            
            if save_btn.collidepoint(mouse_pos):
                print("💾 存档成功！（实际项目中需添加文件存储逻辑）")
            elif settings_btn.collidepoint(mouse_pos):
                # 进入设置界面
                is_paused = False
                pygame.mixer.music.unpause()
                # 触发动画，从当前状态切换到设置
                is_animating = True
                prev_state = current_state
                next_state = GameState.SETTINGS
                animation_progress = 0.0  # 重置动画进度，确保每次动画都从头开始
            elif back_btn.collidepoint(mouse_pos):
                current_state = GameState.COPY_SELECT
                is_paused = False
                pygame.mixer.music.unpause()
                stop_bgm()

        # 鼠标松开事件（结束滑杆拖拽）
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging_bgm_slider = False
                dragging_sfx_slider = False

        # 滑杆拖拽中更新（实时调整音量）
        if event.type == pygame.MOUSEMOTION:
            # 重新获取鼠标位置，确保是最新的
            mouse_pos = pygame.mouse.get_pos()
            
            if dragging_bgm_slider and bgm_slider_rect_global is not None:
                # 使用与draw_settings中相同的面板位置计算函数
                mouse_x, mouse_y = mouse_pos
                panel_x, _, _, _ = calculate_panel_position(config["resolution"])
                offset_x = panel_x + 20
                adjusted_mouse_pos_x = mouse_x - offset_x
                
                slider_x = adjusted_mouse_pos_x
                raw_volume = slider_x / bgm_slider_rect_global.width
                # 严格边界检查，确保音量在0.0-1.0范围内
                bgm_volume = max(0.0, min(1.0, raw_volume))
                pygame.mixer.music.set_volume(bgm_volume)
                print(f"BGM滑块拖拽: 位置={slider_x}, 音量={bgm_volume*100:.0f}%")
            
            if dragging_sfx_slider and sfx_slider_rect_global is not None:
                # 使用与draw_settings中相同的面板位置计算函数
                mouse_x, mouse_y = mouse_pos
                panel_x, _, _, _ = calculate_panel_position(config["resolution"])
                offset_x = panel_x + 20
                adjusted_mouse_pos_x = mouse_x - offset_x
                
                slider_x = adjusted_mouse_pos_x
                raw_volume = slider_x / sfx_slider_rect_global.width
                # 严格边界检查，确保音量在0.0-1.0范围内
                sfx_volume = max(0.0, min(1.0, raw_volume))
                if 'gate_sound' in globals() and gate_sound:
                    gate_sound.set_volume(sfx_volume)
                print(f"SFX滑块拖拽: 位置={slider_x}, 音量={sfx_volume*100:.0f}%")

# 主游戏循环（修复current_state未声明：显式在函数开头声明全局变量）
def main():
    # 声明所有需要使用的全局变量
    global dialog_shown, current_state, current_dialog_index, is_paused
    global player, dragging_bgm_slider, dragging_sfx_slider
    global bgm_slider_rect_global, sfx_slider_rect_global
    # 动画相关全局变量
    global is_animating, prev_state, next_state, animation_progress
    
    # 重置滑块状态变量
    dragging_bgm_slider = False
    dragging_sfx_slider = False
    bgm_slider_rect_global = None
    sfx_slider_rect_global = None
    
    # 初始状态设置
    current_state = GameState.MAIN_MENU
    is_paused = False
    
    # 创建玩家对象（避免未初始化错误）
    player = Player()
    
    # 加载音频
    try:
        load_audio()
    except Exception as e:
        print(f"音频加载出错: {e}")
    
    clock = pygame.time.Clock()

    while True:
        # 获取delta_time（秒）
        delta_time = clock.tick(current_fps) / 1000.0

        # 事件处理
        handle_events()

        # 状态更新（非暂停、非剧情时）
        if not is_paused and current_state != GameState.DIALOG:
            keys = pygame.key.get_pressed()
            player.move(keys, delta_time)
            update_camera()
            update_gate_cooldown()

            # 进入废弃医院后自动显示剧情对话框
            if current_state == GameState.HOSPITAL and not dialog_shown and current_dialog_index == 0:
                dialog_shown = True
                current_state = GameState.DIALOG

        # 场景绘制（根据当前状态绘制对应界面）
        if is_animating:
            # 绘制动画
            animation_complete = draw_animation()
            if animation_complete:
                # 动画完成，更新当前状态
                current_state = next_state
                is_animating = False
        else:
            # 正常绘制当前状态
            screen.fill(BG_COLOR)  # 先清除屏幕
            
            # 无论当前状态是什么，都先绘制主菜单（固定不动）
            draw_main_menu()
            
            # 然后根据当前状态绘制对应内容
            if current_state == GameState.COPY_SELECT:
                draw_copy_select()
            elif current_state == GameState.HOSPITAL:
                draw_hospital()
            elif current_state == GameState.CAFE:
                draw_cafe()
            elif current_state == GameState.GAME_INFO:
                draw_game_info()
            elif current_state == GameState.SETTINGS:
                draw_settings()
            elif current_state == GameState.DIALOG:
                # 剧情对话框在医院场景上叠加绘制
                if current_dialog_index < len(dialog_content):
                    draw_hospital()  # 绘制医院背景
                    draw_dialog()    # 叠加对话框
                else:
                    dialog_shown = False
                    current_state = GameState.HOSPITAL
            elif current_state == GameState.QUIT_CONFIRM:
                draw_quit_confirm()

        # 刷新屏幕
        pygame.display.flip()

# 程序入口（直接运行时启动游戏）
if __name__ == "__main__":
    main()
