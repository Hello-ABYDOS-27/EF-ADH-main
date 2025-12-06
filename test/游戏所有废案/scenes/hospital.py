import pygame
from config import (
    BG_COLOR, WALL_COLOR, GATE_COLOR, GATE_OPEN_COLOR, ROAD_COLOR, GRASS_COLOR_1,
    GRASS_COLOR_2, DIRT_COLOR_1, DIRT_COLOR_2, ROAD_EDGE_COLOR, ROAD_CENTER_COLOR,
    FLOOR_WIDTH, FLOOR_HEIGHT, FLOOR_BLOCK_SIZE, ROAD_START_Y, ROAD_X, ROAD_WIDTH, 
    DASH_LENGTH, DASH_GAP, GATE_TRIGGER_RANGE,
    GATE_X, GATE_Y, GATE_WIDTH, GATE_HEIGHT
)

# 动态创建GATE_RECT
import pygame
GATE_RECT = pygame.Rect(GATE_X, GATE_Y, GATE_WIDTH, GATE_HEIGHT)
from game_state import current_state, gate_is_open
from ui.dialog import font_manager
from audio import play_bgm
from utils.collision import is_player_near_gate

class HospitalScene:
    """废弃医院场景"""
    def __init__(self):
        self.name = "hospital"
    
    def draw(self, screen, config, player, camera_x, camera_y, is_paused):
        """绘制废弃医院场景"""
        screen.fill(BG_COLOR)
        screen.fill((30, 30, 30))

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

        # 播放医院BGM
        play_bgm("hospital")
    
    def _draw_background(self, screen, camera_x, camera_y, config):
        """绘制背景"""
        from config import WALL_LEFT_Y, WALL_THICKNESS
        wall_bottom_y = WALL_LEFT_Y + WALL_THICKNESS
        gate_bottom_y = GATE_RECT.y + GATE_RECT.height
        road_end_y = FLOOR_HEIGHT
        road_left_x = ROAD_X
        road_right_x = ROAD_X + ROAD_WIDTH

        for x in range(0, FLOOR_WIDTH, FLOOR_BLOCK_SIZE):
            for y in range(0, FLOOR_HEIGHT, FLOOR_BLOCK_SIZE):
                draw_x = x - camera_x
                draw_y = y - camera_y
                block_x_center = x + FLOOR_BLOCK_SIZE // 2
                block_y_center = y + FLOOR_BLOCK_SIZE // 2

                if y >= ROAD_START_Y:
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

        start_draw_y = max(0, ROAD_START_Y - camera_y)
        end_draw_y = min(config["resolution"][1], road_end_y - camera_y)
        center_line_x = (road_left_x + road_right_x) // 2 - camera_x

        pygame.draw.line(screen, ROAD_EDGE_COLOR, (road_left_x - camera_x, start_draw_y), (road_left_x - camera_x, end_draw_y), 2)
        pygame.draw.line(screen, ROAD_EDGE_COLOR, (road_right_x - camera_x, start_draw_y), (road_right_x - camera_x, end_draw_y), 2)

        current_y = start_draw_y
        while current_y < end_draw_y:
            line_end_y = min(current_y + DASH_LENGTH, end_draw_y)
            pygame.draw.line(screen, ROAD_CENTER_COLOR, (center_line_x, current_y), (center_line_x, line_end_y), 3)
            current_y += DASH_LENGTH + DASH_GAP
    
    def _draw_gate(self, screen, camera_x, camera_y, player, config):
        """绘制大门"""
        # 绘制墙壁
        from config import INNER_WALL_RECTS
        for wall_tuple in INNER_WALL_RECTS:
            wall_rect = pygame.Rect(wall_tuple)
            pygame.draw.rect(screen, WALL_COLOR, (
                wall_rect.x - camera_x,
                wall_rect.y - camera_y,
                wall_rect.width,
                wall_rect.height
            ))
        
        # 绘制大门
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
            divider_x = (GATE_RECT.x + i * 50) - camera_x  # GRID_SIZE
            divider_y_top = GATE_RECT.y - camera_y
            divider_y_bottom = GATE_RECT.y + GATE_RECT.height - camera_y
            pygame.draw.line(screen, border_color, (divider_x, divider_y_top), (divider_x, divider_y_bottom), 3)
        
        # 大门提示文字
        player_rect = pygame.Rect(
            player.x - player.width//2,
            player.y - player.height//2,
            player.width,
            player.height
        )
        if not is_player_near_gate(player_rect, GATE_RECT, GATE_TRIGGER_RANGE):
            gate_center_x = GATE_RECT.x + GATE_RECT.width//2 - camera_x
            gate_center_y = GATE_RECT.y + GATE_RECT.height//2 - camera_y
            hint_text = "→ 大门在前方 ←"
            hint_surf = font_manager.small_font.render(hint_text, True, (255, 150, 0))
            hint_x = gate_center_x - hint_surf.get_width()//2
            hint_y = gate_center_y - 60
            screen.blit(hint_surf, (hint_x, hint_y))
        else:
            if not gate_is_open:
                hint_text = f"按E打开大门"
            else:
                hint_text = "✅ 大门已打开，可直接穿过！"
            hint_surf = font_manager.small_font.render(hint_text, True, (0, 255, 0))
            hint_bg = pygame.Surface((hint_surf.get_width() + 20, hint_surf.get_height() + 10), pygame.SRCALPHA)
            pygame.draw.rect(hint_bg, (0, 0, 0, 200), (0, 0, hint_bg.get_width(), hint_bg.get_height()), border_radius=5)
            hint_x = (GATE_RECT.x + GATE_RECT.width//2) - camera_x - hint_surf.get_width()//2
            hint_y = GATE_RECT.y - camera_x - 50
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
