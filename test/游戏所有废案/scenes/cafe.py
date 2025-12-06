import pygame
from config import (
    BG_COLOR, CAFE_FLOOR_COLOR, CAFE_STREET_COLOR, CAFE_WALL_COLOR,
    CAFE_GATE_COLOR, CAFE_GATE_OPEN_COLOR, CAFE_GATE_BORDER,
    CAFE_MAP_WIDTH, CAFE_FLOOR_HEIGHT, CAFE_WALL_THICKNESS,
    CAFE_WALL_Y, CAFE_GATE_TRIGGER_RANGE,
    CAFE_GATE_X, CAFE_GATE_Y, CAFE_GATE_WIDTH, CAFE_GATE_THICKNESS
)

# 动态创建Rect对象
import pygame
CAFE_WALL_RECT = pygame.Rect(0, CAFE_WALL_Y, CAFE_MAP_WIDTH, CAFE_WALL_THICKNESS)
CAFE_GATE_RECT = pygame.Rect(CAFE_GATE_X, CAFE_GATE_Y, CAFE_GATE_WIDTH, CAFE_GATE_THICKNESS)
from game_state import current_state, cafe_gate_is_open
from ui.dialog import font_manager
from audio import play_bgm
from utils.collision import is_player_near_gate

class CafeScene:
    """咖啡厅场景"""
    def __init__(self):
        self.name = "cafe"
    
    def draw(self, screen, config, player, camera_x, camera_y, is_paused):
        """绘制咖啡厅场景"""
        screen.fill(BG_COLOR)
        screen.fill((40, 40, 40))

        self._draw_background(screen, camera_x, camera_y, config)
        self._draw_gate(screen, camera_x, camera_y, player, config)
        self._draw_player(screen, player, camera_x, camera_y)
        
        # 绘制对话框
        if current_state == 6:  # DIALOG
            from ui.dialog import dialog_system
            from config import dialog_content
            from game_state import current_dialog_index
            dialog_system.draw_dialog(screen, config, dialog_content, current_dialog_index)
        
        # 绘制暂停界面
        if is_paused:
            self._draw_pause_screen(screen, config)

        # 播放咖啡厅BGM
        play_bgm("cafe")
    
    def _draw_background(self, screen, camera_x, camera_y, config):
        """绘制背景"""
        # 绘制地板
        floor_rect = pygame.Rect(0, 0, CAFE_MAP_WIDTH, CAFE_FLOOR_HEIGHT)
        pygame.draw.rect(screen, CAFE_FLOOR_COLOR, (
            floor_rect.x - camera_x,
            floor_rect.y - camera_y,
            floor_rect.width,
            floor_rect.height
        ))
        
        # 绘制地板网格
        grid_size = 50
        for x in range(0, CAFE_MAP_WIDTH, grid_size):
            pygame.draw.line(screen, (100, 60, 20), (x - camera_x, 0 - camera_y), (x - camera_x, CAFE_FLOOR_HEIGHT - camera_y), 1)
        for y in range(0, CAFE_FLOOR_HEIGHT, grid_size):
            pygame.draw.line(screen, (100, 60, 20), (0 - camera_x, y - camera_y), (CAFE_MAP_WIDTH - camera_x, y - camera_y), 1)
        
        # 绘制街道
        street_rect = pygame.Rect(0, CAFE_FLOOR_HEIGHT + CAFE_WALL_THICKNESS, CAFE_MAP_WIDTH, 200)  # CAFE_STREET_HEIGHT
        pygame.draw.rect(screen, CAFE_STREET_COLOR, (
            street_rect.x - camera_x,
            street_rect.y - camera_y,
            street_rect.width,
            street_rect.height
        ))
        for y in range(street_rect.y, street_rect.y + street_rect.height, 10):
            pygame.draw.line(screen, (100, 100, 100), (0 - camera_x, y - camera_y), (CAFE_MAP_WIDTH - camera_x, y - camera_y), 1)
        
        # 绘制墙壁
        wall_left_rect = pygame.Rect(
            0,
            CAFE_WALL_Y,
            CAFE_GATE_RECT.x,
            CAFE_WALL_THICKNESS
        )
        pygame.draw.rect(screen, CAFE_WALL_COLOR, (
            wall_left_rect.x - camera_x,
            wall_left_rect.y - camera_y,
            wall_left_rect.width,
            wall_left_rect.height
        ))
        
        wall_right_rect = pygame.Rect(
            CAFE_GATE_RECT.x + CAFE_GATE_RECT.width,
            CAFE_WALL_Y,
            CAFE_MAP_WIDTH - (CAFE_GATE_RECT.x + CAFE_GATE_RECT.width),
            CAFE_WALL_THICKNESS
        )
        pygame.draw.rect(screen, CAFE_WALL_COLOR, (
            wall_right_rect.x - camera_x,
            wall_right_rect.y - camera_y,
            wall_right_rect.width,
            wall_right_rect.height
        ))
    
    def _draw_gate(self, screen, camera_x, camera_y, player, config):
        """绘制咖啡厅大门"""
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
        
        # 大门提示文字
        player_rect = pygame.Rect(
            player.x - player.width//2,
            player.y - player.height//2,
            player.width,
            player.height
        )
        gate_center_x = CAFE_GATE_RECT.x + CAFE_GATE_RECT.width//2 - camera_x
        gate_center_y = CAFE_GATE_RECT.y + CAFE_GATE_RECT.height//2 - camera_y
        
        if not is_player_near_gate(player_rect, CAFE_GATE_RECT, CAFE_GATE_TRIGGER_RANGE):
            hint_text = "→ 咖啡厅大门 ←"
            hint_surf = font_manager.small_font.render(hint_text, True, (255, 150, 0))
            hint_x = gate_center_x - hint_surf.get_width()//2
            hint_y = gate_center_y - 40
            screen.blit(hint_surf, (hint_x, hint_y))
        else:
            if not cafe_gate_is_open:
                hint_text = f"按E打开大门"
            else:
                hint_text = "✅ 大门已打开，可进入咖啡厅！"
            hint_surf = font_manager.small_font.render(hint_text, True, (0, 255, 0))
            hint_bg = pygame.Surface((hint_surf.get_width() + 20, hint_surf.get_height() + 10), pygame.SRCALPHA)
            pygame.draw.rect(hint_bg, (0, 0, 0, 200), (0, 0, hint_bg.get_width(), hint_bg.get_height()), border_radius=5)
            hint_x = gate_center_x - hint_surf.get_width()//2
            hint_y = gate_center_y - 50
            screen.blit(hint_bg, (hint_x - 10, hint_y - 5))
            screen.blit(hint_surf, (hint_x, hint_y))
    
    def _draw_player(self, screen, player, camera_x, camera_y):
        """绘制玩家"""
        player.draw(screen, camera_x, camera_y)
    
    def _draw_pause_screen(self, screen, config):
        """绘制暂停界面"""
        pause_surface = pygame.Surface(config["resolution"], pygame.SRCALPHA)
        pygame.draw.rect(pause_surface, (0, 0, 0, 120), (0, 0, config["resolution"][0], config["resolution"][1]))
        screen.blit(pause_surface, (0, 0))
        
        pause_text = font_manager.pause_font.render("暂停", True, (255, 255, 255))
        pause_text_rect = pause_text.get_rect(center=(config["resolution"][0]//2, 200))
        shadow_text = font_manager.pause_font.render("暂停", True, (0, 0, 0, 100))
        screen.blit(shadow_text, (pause_text_rect.x + 5, pause_text_rect.y + 5))
        screen.blit(pause_text, pause_text_rect)

        # 存档按钮
        save_btn_width = 150
        btn_height = 50
        save_btn_y = (config["resolution"][1] // 2) - 40
        save_btn = pygame.Rect(
            config["resolution"][0]//2 - save_btn_width//2,
            save_btn_y,
            save_btn_width,
            btn_height
        )
        from config import BUTTON_HOVER, BUTTON_COLOR, TEXT_COLOR
        save_color = BUTTON_HOVER if save_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
        pygame.draw.rect(screen, save_color, save_btn, border_radius=5)
        save_text = font_manager.option_font.render("存档", True, TEXT_COLOR)
        screen.blit(save_text, save_text.get_rect(center=save_btn.center))
        
        # 返回副本选择按钮
        back_btn_width = 200  # 增加按钮宽度以容纳更长文本
        back_btn_y = save_btn_y + btn_height + 30
        back_btn = pygame.Rect(
            config["resolution"][0]//2 - back_btn_width//2,
            back_btn_y,
            back_btn_width,
            btn_height
        )
        pygame.draw.rect(screen, BUTTON_HOVER if back_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, back_btn)
        back_text = font_manager.option_font.render("返回副本选择", True, TEXT_COLOR)
        screen.blit(back_text, back_text.get_rect(center=back_btn.center))
