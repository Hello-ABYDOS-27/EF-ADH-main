import pygame
from config import (
    BG_COLOR, MENU_BG, BUTTON_COLOR, BUTTON_HOVER, TEXT_COLOR,
    SELECTED_COLOR, RESET_BTN_COLOR, RESET_BTN_HOVER
)
from ui.dialog import font_manager
from audio import play_bgm

class MainMenu:
    """主菜单UI组件"""
    def __init__(self):
        self.menu_width = 250
        self.menu_height = 320
        self.btn_width = 230  # menu_width - 20
        self.btn_height = 45
        self.button_y_offset = 80
        self.button_spacing = 55
    
    def draw_main_menu(self, screen, config):
        """绘制主菜单"""
        screen.fill(BG_COLOR)
        menu_x = (config["resolution"][0] - self.menu_width) // 2
        menu_y = (config["resolution"][1] - self.menu_height) // 2

        pygame.draw.rect(screen, MENU_BG, (menu_x, menu_y, self.menu_width, self.menu_height))
        pygame.draw.rect(screen, BUTTON_COLOR, (menu_x, menu_y, self.menu_width, self.menu_height), 2)

        title_text = font_manager.option_font.render("逃离学校剧本", True, TEXT_COLOR)
        title_x = menu_x + (self.menu_width - title_text.get_width()) // 2
        title_y = menu_y + 35
        screen.blit(title_text, (title_x, title_y))

        # 开始游戏按钮
        start_btn = pygame.Rect(menu_x + 10, menu_y + self.button_y_offset, self.btn_width, self.btn_height)
        pygame.draw.rect(screen, BUTTON_HOVER if start_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, start_btn)
        start_text = font_manager.option_font.render("开始游戏", True, TEXT_COLOR)
        start_text_pos = start_text.get_rect(center=start_btn.center)
        screen.blit(start_text, start_text_pos)

        # 设置按钮
        setting_btn = pygame.Rect(menu_x + 10, menu_y + self.button_y_offset + self.button_spacing, self.btn_width, self.btn_height)
        pygame.draw.rect(screen, BUTTON_HOVER if setting_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, setting_btn)
        setting_text = font_manager.option_font.render("设置", True, TEXT_COLOR)
        setting_text_pos = setting_text.get_rect(center=setting_btn.center)
        screen.blit(setting_text, setting_text_pos)

        # 游戏信息按钮
        info_btn = pygame.Rect(menu_x + 10, menu_y + self.button_y_offset + self.button_spacing * 2, self.btn_width, self.btn_height)
        pygame.draw.rect(screen, BUTTON_HOVER if info_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, info_btn)
        info_text = font_manager.option_font.render("游戏信息", True, TEXT_COLOR)
        info_text_pos = info_text.get_rect(center=info_btn.center)
        screen.blit(info_text, info_text_pos)

        # 退出游戏按钮
        quit_btn = pygame.Rect(menu_x + 10, menu_y + self.button_y_offset + self.button_spacing * 3, self.btn_width, self.btn_height)
        quit_color = (220, 80, 80) if quit_btn.collidepoint(pygame.mouse.get_pos()) else (200, 60, 60)
        pygame.draw.rect(screen, quit_color, quit_btn)
        quit_text = font_manager.option_font.render("退出游戏", True, TEXT_COLOR)
        quit_text_pos = quit_text.get_rect(center=quit_btn.center)
        screen.blit(quit_text, quit_text_pos)

        # 播放菜单BGM
        play_bgm("menu")

        return start_btn, setting_btn, info_btn, quit_btn

class CopySelect:
    """副本选择UI组件"""
    def __init__(self):
        self.option_width = 220
        self.option_height = 120
        self.spacing = 60
        self.back_btn_width = 100
        self.back_btn_height = 40
    
    def draw_copy_select(self, screen, config):
        """绘制副本选择界面"""
        screen.fill(BG_COLOR)

        title_text = font_manager.menu_font.render("选择副本场景", True, TEXT_COLOR)
        screen.blit(title_text, title_text.get_rect(center=(config["resolution"][0]//2, 80)))

        start_x = (config["resolution"][0] - (3 * self.option_width + 2 * self.spacing)) // 2
        start_y = (config["resolution"][1] - self.option_height) // 2 + 20

        # 废弃医院按钮
        hospital_btn = pygame.Rect(start_x, start_y, self.option_width, self.option_height)
        pygame.draw.rect(screen, BUTTON_HOVER if hospital_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, hospital_btn)
        hospital_text = font_manager.option_font.render("废弃医院", True, TEXT_COLOR)
        screen.blit(hospital_text, hospital_text.get_rect(center=hospital_btn.center))

        # 咖啡厅按钮
        cafe_btn = pygame.Rect(start_x + self.option_width + self.spacing, start_y, self.option_width, self.option_height)
        pygame.draw.rect(screen, BUTTON_HOVER if cafe_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, cafe_btn)
        cafe_text = font_manager.option_font.render("咖啡厅", True, TEXT_COLOR)
        screen.blit(cafe_text, cafe_text.get_rect(center=cafe_btn.center))

        # 结婚现场按钮
        wedding_btn = pygame.Rect(start_x + 2*(self.option_width + self.spacing), start_y, self.option_width, self.option_height)
        pygame.draw.rect(screen, BUTTON_HOVER if wedding_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, wedding_btn)
        wedding_text = font_manager.option_font.render("结婚现场", True, TEXT_COLOR)
        screen.blit(wedding_text, wedding_text.get_rect(center=wedding_btn.center))

        # 返回按钮
        back_btn = pygame.Rect(30, config["resolution"][1] - 60, self.back_btn_width, self.back_btn_height)
        pygame.draw.rect(screen, BUTTON_HOVER if back_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, back_btn)
        back_text = font_manager.small_font.render("返回", True, TEXT_COLOR)
        screen.blit(back_text, back_text.get_rect(center=back_btn.center))

        # 播放菜单BGM
        play_bgm("menu")

        return hospital_btn, cafe_btn, wedding_btn, back_btn

class GameInfo:
    """游戏信息UI组件"""
    def __init__(self):
        self.info_width = 0
        self.info_height = 0
    
    def draw_game_info(self, screen, config, info_scroll_y):
        """绘制游戏信息界面"""
        screen.fill(BG_COLOR)
        title_text = font_manager.menu_font.render("游戏信息", True, TEXT_COLOR)
        screen.blit(title_text, title_text.get_rect(center=(config["resolution"][0]//2, 80)))

        self.info_width = config["resolution"][0] - 100
        self.info_height = config["resolution"][1] - 200
        info_x = 50
        info_y = 120
        info_bottom_y = info_y + self.info_height

        pygame.draw.rect(screen, MENU_BG, (info_x, info_y, self.info_width, self.info_height))
        pygame.draw.rect(screen, BUTTON_COLOR, (info_x, info_y, self.info_width, self.info_height), 2)

        info_content = self._get_game_info_content()
        self._draw_scrollable_text(screen, info_x, info_y, info_content, info_scroll_y)

        # 绘制返回按钮
        back_btn = pygame.Rect(30, config["resolution"][1] - 60, 100, 40)
        pygame.draw.rect(screen, BUTTON_HOVER if back_btn.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR, back_btn)
        back_text = font_manager.small_font.render("返回", True, TEXT_COLOR)
        screen.blit(back_text, back_text.get_rect(center=back_btn.center))

        # 播放菜单BGM
        play_bgm("menu")

        return back_btn
    
    def _get_game_info_content(self):
        """获取游戏信息内容"""
        return [
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
    
    def _draw_scrollable_text(self, screen, info_x, info_y, info_content, info_scroll_y):
        """绘制可滚动文本"""
        line_height = font_manager.small_font.get_linesize()
        max_line_width = self.info_width - 40  # 左右各留20像素边距
        
        # 处理文本自动换行
        wrapped_content = []
        for line in info_content:
            if not line.strip():
                wrapped_content.append('')
                continue
            
            # 简单的换行处理
            if font_manager.small_font.size(line)[0] <= max_line_width:
                wrapped_content.append(line)
            else:
                # 按字符拆分长文本
                current_line = ''
                for char in line:
                    test_line = current_line + char
                    if font_manager.small_font.size(test_line)[0] > max_line_width:
                        wrapped_content.append(current_line)
                        current_line = char
                    else:
                        current_line = test_line
                if current_line:
                    wrapped_content.append(current_line)
        
        # 计算总高度和滚动区域
        total_height = len(wrapped_content) * line_height
        scrollable_area = max(0, total_height - self.info_height)

        # 确保滚动位置在有效范围内
        info_scroll_y = max(-scrollable_area, min(0, info_scroll_y))

        # 创建一个裁剪区域，确保文本不会超出容器边界
        clip_rect = pygame.Rect(info_x + 20, info_y, self.info_width - 40, self.info_height)
        original_clip = screen.get_clip()  # 保存原始裁剪区域
        screen.set_clip(clip_rect)  # 设置裁剪区域

        # 渲染换行后的文本
        for i, line in enumerate(wrapped_content):
            line_top_y = info_y + i * line_height + info_scroll_y
            line_bottom_y = line_top_y + line_height
            
            # 只有当行与可见区域相交时才渲染
            if line_bottom_y > info_y and line_top_y < info_y + self.info_height:
                # 渲染文本
                text_surf = font_manager.small_font.render(line, True, TEXT_COLOR)
                screen.blit(text_surf, (info_x + 20, line_top_y))

        # 恢复原始裁剪区域
        screen.set_clip(original_clip)

        # 绘制滚动条
        if scrollable_area > 0:
            scrollbar_width = 8
            scrollbar_height = max(20, (self.info_height / total_height) * self.info_height)
            scrollbar_y = info_y + (-info_scroll_y / scrollable_area) * (self.info_height - scrollbar_height)
            pygame.draw.rect(screen, BUTTON_HOVER, (info_x + self.info_width - 15, scrollbar_y, scrollbar_width, scrollbar_height), border_radius=3)

class Settings:
    """设置界面UI组件"""
    def __init__(self):
        self.panel_width = 500
        self.panel_height = 0
        self.base_y = 0
    
    def calculate_panel_position(self, resolution):
        """计算设置面板的位置和尺寸"""
        panel_width = 500  # 固定宽度以确保一致性
        panel_height = resolution[1] - 200
        panel_x = (resolution[0] - panel_width) // 2  # 居中计算
        panel_y = 120
        return panel_x, panel_y, panel_width, panel_height
    
    def draw_settings(self, screen, config, current_res_idx, current_fps_idx, editing_shortcut, settings_scroll_y, RESOLUTION_OPTIONS, FPS_OPTIONS, shortcut_items):
        """绘制设置界面"""
        screen.fill(BG_COLOR)
        title_text = font_manager.menu_font.render("游戏设置", True, TEXT_COLOR)
        screen.blit(title_text, title_text.get_rect(center=(config["resolution"][0]//2, 80)))

        panel_x, panel_y, panel_width, panel_height = self.calculate_panel_position(config["resolution"])
        panel_bottom_y = panel_y + panel_height

        pygame.draw.rect(screen, MENU_BG, (panel_x, panel_y, panel_width, panel_height))
        pygame.draw.rect(screen, BUTTON_COLOR, (panel_x, panel_y, panel_width, panel_height), 2)

        # 滚动容器（所有设置项绘制在滚动表面上）
        scroll_surface = pygame.Surface((panel_width - 40, 1200), pygame.SRCALPHA)
        self.base_y = 0 + settings_scroll_y

        # 分辨率设置
        res_y = self._draw_resolution_settings(scroll_surface, current_res_idx, RESOLUTION_OPTIONS)
        
        # 帧率设置
        fps_y = self._draw_fps_settings(scroll_surface, current_fps_idx, FPS_OPTIONS, res_y)
        
        # 音量设置
        vol_y = self._draw_volume_settings(scroll_surface, fps_y)
        
        # 快捷键设置
        self._draw_shortcut_settings(scroll_surface, editing_shortcut, shortcut_items, config, panel_x, panel_y, settings_scroll_y, vol_y)

        # 绘制滚动表面
        screen.blit(scroll_surface, (panel_x + 20, panel_y + 20))

        # 播放菜单BGM
        play_bgm("menu")
    
    def _draw_resolution_settings(self, scroll_surface, current_res_idx, RESOLUTION_OPTIONS):
        """绘制分辨率设置"""
        res_title = font_manager.option_font.render("分辨率设置", True, TEXT_COLOR)
        scroll_surface.blit(res_title, (0, self.base_y))
        res_y = self.base_y + 40
        res_spacing = 30
        for i, (w, h) in enumerate(RESOLUTION_OPTIONS):
            res_text = f"{w} × {h}"
            res_rect = pygame.Rect(0, res_y + i * res_spacing, 200, 30)
            if i == current_res_idx:
                pygame.draw.rect(scroll_surface, SELECTED_COLOR, res_rect, border_radius=3)
            else:
                pygame.draw.rect(scroll_surface, BUTTON_COLOR, res_rect, border_radius=3)
            res_surf = font_manager.small_font.render(res_text, True, TEXT_COLOR)
            scroll_surface.blit(res_surf, res_surf.get_rect(center=res_rect.center))
        return res_y + len(RESOLUTION_OPTIONS) * res_spacing
    
    def _draw_fps_settings(self, scroll_surface, current_fps_idx, FPS_OPTIONS, start_y):
        """绘制帧率设置"""
        fps_title = font_manager.option_font.render("帧率设置", True, TEXT_COLOR)
        fps_y = start_y + 60
        scroll_surface.blit(fps_title, (0, fps_y))
        fps_option_y = fps_y + 40
        res_spacing = 30
        for i, fps in enumerate(FPS_OPTIONS):
            fps_rect = pygame.Rect(0, fps_option_y + i * res_spacing, 100, 30)
            if i == current_fps_idx:
                pygame.draw.rect(scroll_surface, SELECTED_COLOR, fps_rect, border_radius=3)
            else:
                pygame.draw.rect(scroll_surface, BUTTON_COLOR, fps_rect, border_radius=3)
            fps_surf = font_manager.small_font.render(f"{fps} FPS", True, TEXT_COLOR)
            scroll_surface.blit(fps_surf, fps_surf.get_rect(center=fps_rect.center))
        return fps_option_y + len(FPS_OPTIONS) * res_spacing
    
    def _draw_volume_settings(self, scroll_surface, start_y):
        """绘制音量设置"""
        from config import SLIDER_BG_COLOR, SLIDER_FILL_COLOR, SLIDER_THUMB_COLOR, SLIDER_THUMB_HOVER_COLOR
        from game_state import bgm_volume, sfx_volume
        
        vol_title = font_manager.option_font.render("音量设置", True, TEXT_COLOR)
        vol_y = start_y + 60
        scroll_surface.blit(vol_title, (0, vol_y))
        
        # BGM音量
        bgm_label = font_manager.small_font.render("BGM音量", True, TEXT_COLOR)
        scroll_surface.blit(bgm_label, (0, vol_y + 40))
        
        # BGM音量滑块
        slider_width = 300
        slider_height = 10
        slider_x = 120
        slider_y = vol_y + 45
        
        # 绘制滑块背景
        pygame.draw.rect(scroll_surface, SLIDER_BG_COLOR, (slider_x, slider_y, slider_width, slider_height), border_radius=5)
        
        # 绘制填充部分
        fill_width = int(slider_width * bgm_volume)
        pygame.draw.rect(scroll_surface, SLIDER_FILL_COLOR, (slider_x, slider_y, fill_width, slider_height), border_radius=5)
        
        # 绘制滑块
        thumb_x = slider_x + fill_width - 7
        thumb_y = slider_y - 7
        thumb_color = SLIDER_THUMB_HOVER_COLOR if pygame.Rect(thumb_x-5, thumb_y-5, 20, 20).collidepoint(pygame.mouse.get_pos()) else SLIDER_THUMB_COLOR
        pygame.draw.circle(scroll_surface, thumb_color, (thumb_x, thumb_y + 5), 10)
        
        # SFX音量
        sfx_label = font_manager.small_font.render("音效音量", True, TEXT_COLOR)
        scroll_surface.blit(sfx_label, (0, vol_y + 80))
        
        # SFX音量滑块
        sfx_slider_y = vol_y + 85
        
        # 绘制滑块背景
        pygame.draw.rect(scroll_surface, SLIDER_BG_COLOR, (slider_x, sfx_slider_y, slider_width, slider_height), border_radius=5)
        
        # 绘制填充部分
        fill_width = int(slider_width * sfx_volume)
        pygame.draw.rect(scroll_surface, SLIDER_FILL_COLOR, (slider_x, sfx_slider_y, fill_width, slider_height), border_radius=5)
        
        # 绘制滑块
        thumb_x = slider_x + fill_width - 7
        thumb_y = sfx_slider_y - 7
        thumb_color = SLIDER_THUMB_HOVER_COLOR if pygame.Rect(thumb_x-5, thumb_y-5, 20, 20).collidepoint(pygame.mouse.get_pos()) else SLIDER_THUMB_COLOR
        pygame.draw.circle(scroll_surface, thumb_color, (thumb_x, thumb_y + 5), 10)
        
        return vol_y + 120
    
    def _draw_shortcut_settings(self, scroll_surface, editing_shortcut, shortcut_items, config, panel_x, panel_y, settings_scroll_y, start_y):
        """绘制快捷键设置"""
        shortcut_title = font_manager.option_font.render("快捷键设置（点击修改）", True, TEXT_COLOR)
        shortcut_y = start_y + 60
        scroll_surface.blit(shortcut_title, (0, shortcut_y))
        shortcut_option_y = shortcut_y + 40
        
        for i, (name, key) in enumerate(shortcut_items):
            # 快捷键标签
            label_rect = pygame.Rect(0, shortcut_option_y + i * 50, 100, 35)
            pygame.draw.rect(scroll_surface, BUTTON_COLOR, label_rect, border_radius=3)
            label_surf = font_manager.small_font.render(name, True, TEXT_COLOR)
            scroll_surface.blit(label_surf, label_surf.get_rect(center=label_rect.center))

            # 快捷键显示框
            key_rect = pygame.Rect(120, shortcut_option_y + i * 50, 200, 35)
            if editing_shortcut == key:
                pygame.draw.rect(scroll_surface, SELECTED_COLOR, key_rect, border_radius=3)
                key_text = "按任意键修改..."
            else:
                pygame.draw.rect(scroll_surface, BUTTON_COLOR, key_rect, border_radius=3)
                key_text = pygame.key.name(config["shortcuts"][key])
            key_surf = font_manager.small_font.render(key_text, True, TEXT_COLOR)
            scroll_surface.blit(key_surf, key_surf.get_rect(center=key_rect.center))

            # 重置按钮
            reset_rect = pygame.Rect(340, shortcut_option_y + i * 50, 80, 35)
            # 简化悬停检测：直接使用屏幕坐标计算
            # 创建屏幕坐标的矩形用于悬停检测
            screen_reset_rect = pygame.Rect(panel_x + 20 + 340, panel_y + 20 + shortcut_option_y + i * 50 + settings_scroll_y, 80, 35)
            pygame.draw.rect(scroll_surface, RESET_BTN_HOVER if screen_reset_rect.collidepoint(pygame.mouse.get_pos()) else RESET_BTN_COLOR, reset_rect, border_radius=3)
            reset_surf = font_manager.small_font.render("重置", True, TEXT_COLOR)
            scroll_surface.blit(reset_surf, reset_surf.get_rect(center=reset_rect.center))
