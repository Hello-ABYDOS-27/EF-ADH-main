import pygame
from config import (
    TEXT_COLOR, DIALOG_BG, NPC_DEFAULT_COLOR,
    DEFAULT_WIDTH, DEFAULT_HEIGHT
)

class FontManager:
    """字体管理器，负责加载和管理游戏中的所有字体"""
    def __init__(self):
        try:
            self.menu_font = pygame.font.SysFont("SimHei", 48)
            self.option_font = pygame.font.SysFont("SimHei", 36)
            self.small_font = pygame.font.SysFont("SimHei", 28)
            self.dialog_font = pygame.font.SysFont("SimHei", 24)
            self.pause_font = pygame.font.SysFont("SimHei", 72)
        except:
            self.menu_font = pygame.font.SysFont(None, 48)
            self.option_font = pygame.font.SysFont(None, 36)
            self.small_font = pygame.font.SysFont(None, 28)
            self.dialog_font = pygame.font.SysFont(None, 24)
            self.pause_font = pygame.font.SysFont(None, 72)

# 全局字体管理器实例
font_manager = FontManager()

class DialogSystem:
    """对话框系统，负责显示和管理游戏中的对话"""
    def __init__(self):
        self.dialog_width = 800
        self.dialog_height = 200
        self.line_spacing = 30
        
    def draw_dialog(self, screen, config, dialog_content, current_dialog_index):
        """绘制对话框"""
        dialog_x = (config["resolution"][0] - self.dialog_width) // 2
        dialog_y = (config["resolution"][1] - self.dialog_height) // 2

        dialog_surface = pygame.Surface((self.dialog_width, self.dialog_height), pygame.SRCALPHA)
        pygame.draw.rect(dialog_surface, (50, 50, 60, 230), (0, 0, self.dialog_width, self.dialog_height), border_radius=8)
        pygame.draw.rect(dialog_surface, (255, 255, 255, 100), (0, 0, self.dialog_width, self.dialog_height), 2, border_radius=8)
        screen.blit(dialog_surface, (dialog_x, dialog_y))

        npc_img = self._init_npc_img()
        npc_x = dialog_x + 20
        npc_y = dialog_y + (self.dialog_height - 100) // 2
        screen.blit(pygame.transform.scale(npc_img, (100, 100)), (npc_x, npc_y))

        current_text = dialog_content[current_dialog_index]
        text_x = dialog_x + 140
        text_y = dialog_y + 40
        max_text_width = self.dialog_width - 180
        
        available_height = self.dialog_height - 80
        max_lines = available_height // self.line_spacing

        wrapped_content = self._wrap_text(current_text, max_text_width)
        text_overflows = len(wrapped_content) > max_lines
        
        for i, line in enumerate(wrapped_content[:max_lines]):
            text_surf = font_manager.dialog_font.render(line, True, TEXT_COLOR)
            screen.blit(text_surf, (text_x, text_y + i * self.line_spacing))
        
        if text_overflows:
            overflow_hint = font_manager.small_font.render("...", True, TEXT_COLOR)
            overflow_x = text_x + max_text_width - overflow_hint.get_width() - 5
            overflow_y = text_y + (max_lines - 1) * self.line_spacing
            screen.blit(overflow_hint, (overflow_x, overflow_y))

        hint_surf = font_manager.small_font.render("点击鼠标左键继续/关闭剧情", True, (150, 150, 150))
        hint_x = dialog_x + (self.dialog_width - hint_surf.get_width()) // 2
        hint_y = dialog_y + self.dialog_height - 40
        screen.blit(hint_surf, (hint_x, hint_y))
    
    def _init_npc_img(self):
        """初始化NPC图像"""
        try:
            npc_img = pygame.image.load("player_walk3.png").convert_alpha()
            return pygame.transform.scale(npc_img, (200, 200))
        except pygame.error:
            print("⚠️  缺少NPC图片，使用默认绿色方块")
            img = pygame.Surface((200, 200), pygame.SRCALPHA)
            pygame.draw.rect(img, NPC_DEFAULT_COLOR, (0, 0, 200, 200))
            return img
    
    def _wrap_text(self, text, max_width):
        """将文本按宽度换行"""
        words = []
        current_word = ""
        for char in text:
            if char.isspace():
                if current_word:
                    words.append(current_word)
                    words.append(char)
                    current_word = ""
                else:
                    words.append(char)
            else:
                current_word += char
        if current_word:
            words.append(current_word)

        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word
            if font_manager.dialog_font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                    current_line = word
                else:
                    for char in word:
                        test_line = current_line + char
                        if font_manager.dialog_font.size(test_line)[0] <= max_width:
                            current_line = test_line
                        else:
                            lines.append(current_line)
                            current_line = char
        if current_line:
            lines.append(current_line)
        return lines

# 全局对话框系统实例
dialog_system = DialogSystem()
