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

        self.cars = []
        self._create_cars()

    def run(self):
        while self.running:
            dt_ms = self.clock.tick(settings.FPS)
            dt = dt_ms / 1000.0 

            self._handle_events()
            self._draw()
            self._update(dt)
        
        pygame.quit()
        sys.exit()

    def _draw_track(self):
        # фон траси
        track_rect = pygame.Rect(
            0,
            settings.TRACK_TOP,
            settings.BASE_WIDTH,
            settings.TRACK_HEIGHT)
        pygame.draw.rect(self.screen, settings.TRACK_COLOR, track_rect)

        # лінії між полосами
        lane_height = (settings.TRACK_BOTTOM - settings.TRACK_TOP
                       ) // settings.LANE_COUNT
        for lane in range(1, settings.LANE_COUNT):
            y = settings.TRACK_TOP
            pygame.draw.line(
                self.screen,
                settings.LANE_LINE_COLOR,
                (settings.TRACK_START_X, y),
                (settings.TRACK_FINISH_X, y),
                2)
        # стартова лінія
        pygame.draw.line(
            self.screen,
            settings.LINE_COLOR,
            (settings.TRACK_START_X, settings.TRACK_TOP),
            (settings.TRACK_START_X, settings.TRACK_BOTTOM),
            4)
        # Фінішна лінія
        pygame.draw.line(
            self.screen,
            settings.LINE_COLOR,
            (settings.TRACK_FINISH_X, settings.TRACK_TOP),
            (settings.TRACK_FINISH_X, settings.TRACK_BOTTOM),
            4)
        

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    player_car = self.cars[0]
                    player_car.move_one_symbol()

    def _draw(self):
        self.screen.fill(settings.BG_COLOR)
        self._draw_track()

        for car in self.cars:
            car.draw(self.screen)

        pygame.display.flip()

    def _create_cars(self):
        from car import Car

        self.cars = []

        for lane_index in range(settings.LANE_COUNT):
            is_player = (lane_index == 0)  # верхня полоса — гравець
            color = settings.CAR_COLORS[lane_index]
            car = Car(lane_index=lane_index, color=color, is_player=is_player)
            self.cars.append(car)

    def _update(self, dt):
        for car in self.cars:
            car.update(dt)

    def _load_phrases(self):
        lines = []

        try:
            with open(settings.PHRASES_FILE,"r", encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines()]
        except (OSError, UnicodeDecodeError):
            try:
                with open(settings.PHRASES_FILE,"r", encoding="cp1251") as f:
                    lines = [line.strip() for line in f.readlines()]
            except (OSError, UnicodeDecodeError):
                lines = []