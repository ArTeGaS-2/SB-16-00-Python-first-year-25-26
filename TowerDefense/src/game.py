import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, FPS
from src.scenes.menu_scene import MenuScene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.current_scene = MenuScene(self)