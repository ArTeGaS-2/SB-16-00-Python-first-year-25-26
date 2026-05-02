import pygame

from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_GAP)

from src.ui.button import Button
from src.scenes.game_scene import GameScene

class MenuScene:
    def __init__(self, game):
        self.game = game
        self.background = pygame.image.load("assets/ui/menu_background.png").convert()
        self.background = pygame.transform.scale(
            self.background, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.font = pygame.font.Font(None, 48)
        self.title_font = pygame.font.Font(None, 88)

        button_x = (WINDOW_WIDTH - BUTTON_WIDTH) // 2
        start_y = 320

        self.start_button = Button(
            button_x,
            start_y,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "assets/ui/button.png",
            "Старт",
            self.font)
        
        self.exit_button = Button(
            button_x,
            start_y + BUTTON_HEIGHT + BUTTON_GAP,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            "assets/ui/button.png",
            "Вихід",
            self.font)
        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            if self.start_button.is_clicked(mouse_pos):
                self.game.set_scene(GameScene(self.game))

            if self.exit_button.is_clicked(mouse_pos):
                self.game.is_running = False
    
    def update(self, delta_time):
        pass

    def draw(self, surface):
        surface.blit(self.background, (0,0))

        title_surface = self.title_font.render("Tower Defence",
            True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(WINDOW_WIDTH // 2, 170))
        surface.blit(title_surface, title_rect)

        self.start_button.draw(surface)
        self.exit_button.draw(surface)