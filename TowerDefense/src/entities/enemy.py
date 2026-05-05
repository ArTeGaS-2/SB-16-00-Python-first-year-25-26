import pygame

class Enemy:
    def __init__(self, image_path, path_points, speed):
        self.image = pygame.image.load(str(image_path)).convert_alpha()
        self.path_points = [pygame.Vector2(point) for point in path_points]
        self.speed = speed