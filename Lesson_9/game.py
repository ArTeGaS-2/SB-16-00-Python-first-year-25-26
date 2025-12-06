# pip install pygame
import sys
import pygame
import settings

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Гра")

        self.screen = pygame.display.set_mode(
            (settings.BASE_WIDTH, settings.BASE_HEIGHT),
            pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            dt_ms = self.clock.tick(settings.FPS)
            dt = dt_ms / 1000.0 

            self._handle_events()
            self._draw()
        
        pygame.quit()
        sys.exit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def _draw(self):
        self.screen.fill(settings.BG_COLOR)
        pygame.display.flip()