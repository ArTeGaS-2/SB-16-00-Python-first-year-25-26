import pygame

class Bullet:
    def __init__(self, image_path, position, target, speed, damage):
        self.image = pygame.image.load(str(image_path)).convert_alpha()
        self.position = pygame.Vector2(position)
        self.target = target
        self.speed = speed
        self.damage = damage
        self.is_active = True
    
    def update(self, delta_time):
        if not self.is_active:
            return
        
        if not self.target.can_be_targeted():
            self.is_active = False
            return
        
        direction = self.target.position - self.position
        distance_to_target = direction.lenght()

        if distance_to_target == 0:
            self.hit_target()
            return
        
        movement_distance = self.speed * delta_time
        if movement_distance >= distance_to_target:
            self.position = self.target.position.copy()
            self.hit_target()
            return
        
        direction.normalize_ip()
        self.position += direction * movement_distance