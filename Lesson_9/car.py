import pygame
import settings
import random

class Car:
    def __init__(self, lane_index, color, is_player):
        self.lane_index = lane_index # індекс (номер) лінії
        self.color = color # колір машини
        self.is_player = is_player # чи гравець ця машина

        self.symbols_done = 0.0 # скільки символів вже введено
        self.finished = False # чи на фініші

        self.width = settings.CAR_WIDTH # ширина
        self.height = settings.CAR_HEIGHT # висота

        # старт по Х
        self.x = settings.TRACK_START_X

        # позиція по Y: рівномірно розкладаємо по лініях
        lane_height = (settings.TRACK_BOTTOM - settings.TRACK_TOP
                       ) // settings.LANE_COUNT
        self.y = (
            settings.TRACK_TOP
            + lane_height * self.lane_index
            + lane_height // 2)
        
        if not self.is_player:
            self.speed_symbols_per_sec = random.uniform(0.5, 4.0)
        else:
            self.speed_symbols_per_sec = 0.0
        
        self._update_x_from_symbols()

    def _update_x_from_symbols(self):
        self.x = (settings.TRACK_START_X + self.symbols_done * 
                    settings.SYMBOL_STEP_PX)
        if self.symbols_done >= settings.SYMBOLS_TO_FINISH:
            self.symbols_done = settings.SYMBOLS_TO_FINISH
            self.finished = True
            self.x = (settings.TRACK_START_X + self.symbols_done *
                      settings.SYMBOL_STEP_PX)
    
    def move_one_symbol(self):
        if self.finished:
            return
        self.symbols_done += 1.0
        self._update_x_from_symbols()

    def update(self, dt):
        if self.finished:
            return
        
        if not self.is_player:
            self.symbols_done += self.speed_symbols_per_sec * dt
            self._update_x_from_symbols()

    def draw(self, surface):
        rect = pygame.Rect(
            int(self.x),
            int(self.y - self.height // 2),
            self.width,
            self.height)
        pygame.draw.rect(surface, self.color, rect)

