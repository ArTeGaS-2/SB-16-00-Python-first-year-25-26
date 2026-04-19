import pygame

from settings import(
    MAP_DATA_PATH,
    SIDEBAR_PANEL_PATH,
    SIDEBAR_WIDTH,
    SIDEBAR_X,
    WHITE,
    WINDOW_HEIGHT)

from src.map.tile_map import TileMap

class GameScene:
    def __init__(self, game):
        self.game = game
        self.tile_map = TileMap(MAP_DATA_PATH)
        self.sidebar_panel = pygame.image.load(str(SIDEBAR_PANEL_PATH)).convert()
        self.sidebar_panel = pygame.transform.scale(
            self.sidebar_panel, (SIDEBAR_WIDTH, WINDOW_HEIGHT))
        self.title_font = pygame.font.SysFont("arial", 34, bold=True)
        self.section_font = pygame.font.SysFont("arial", 26, bold=True)
        self.text_font = pygame.font.SysFont("arial", 24)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.game.is_running = False
    
    def update(self, delta_time):
        pass

    def draw(self, surface):
        self.tile_map.draw(surface)
        # surface.
