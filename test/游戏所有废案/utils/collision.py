import pygame
from config import (
    INNER_WALL_RECTS
)
from game_state import gate_is_open, cafe_gate_is_open

# 从config导入必要的坐标和尺寸
from config import (
    GATE_X, GATE_Y, GATE_WIDTH, GATE_HEIGHT,
    CAFE_WALL_Y, CAFE_WALL_THICKNESS, CAFE_MAP_WIDTH,
    CAFE_GATE_X, CAFE_GATE_Y, CAFE_GATE_WIDTH, CAFE_GATE_THICKNESS
)

# 动态创建rect对象
GATE_RECT = pygame.Rect(GATE_X, GATE_Y, GATE_WIDTH, GATE_HEIGHT)
CAFE_WALL_RECT = pygame.Rect(0, CAFE_WALL_Y, CAFE_MAP_WIDTH, CAFE_WALL_THICKNESS)
CAFE_GATE_RECT = pygame.Rect(CAFE_GATE_X, CAFE_GATE_Y, CAFE_GATE_WIDTH, CAFE_GATE_THICKNESS)

def check_collision(player_rect):
    """检查玩家与废弃医院场景的碰撞"""
    for wall_tuple in INNER_WALL_RECTS:
        # 将元组转换为pygame.Rect对象
        wall_rect = pygame.Rect(wall_tuple)
        if player_rect.colliderect(wall_rect):
            return True
    if not gate_is_open and player_rect.colliderect(GATE_RECT):
        return True
    return False

def check_cafe_collision(player_rect):
    """检查玩家与咖啡厅场景的碰撞"""
    if player_rect.colliderect(CAFE_WALL_RECT) and not player_rect.colliderect(CAFE_GATE_RECT):
        return True
    if not cafe_gate_is_open and player_rect.colliderect(CAFE_GATE_RECT):
        return True
    return False

def is_player_near_gate(player_rect, gate_rect, trigger_range):
    """检查玩家是否靠近大门"""
    trigger_rect = gate_rect.inflate(trigger_range, trigger_range // 2)
    return player_rect.colliderect(trigger_rect)

def fix_gate_stuck(player_rect, player, gate_rect, gate_is_open):
    """修复玩家卡在大门的问题"""
    if gate_is_open or not player_rect.colliderect(gate_rect):
        return player_rect
    gate_mid_y = gate_rect.y + gate_rect.height // 2
    player_mid_y = player_rect.centery
    if player_mid_y < gate_mid_y:
        player.y -= 50  # GRID_SIZE
    else:
        player.y += 50  # GRID_SIZE
    return pygame.Rect(
        player.x - player.width//2,
        player.y - player.height//2,
        player.width,
        player.height
    )
