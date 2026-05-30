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

    def draw(self, surface):
        # якщо куля вже влучила в ціль або ціль стала недоступною, не малюємо її
        if not self.is_active:
            return
        
        # розраховуємо координати для малювання кулі, щоб вона була центрована на позиції
        draw_x = self.position.x - self.image.get_width() / 2
        draw_y = self.position.y - self.image.get_height() / 2
        # малюємо кулю на екрані
        surface.blit(self.image, (draw_x, draw_y))

    def hit_target(self):
        # якщо ціль все ще може бути атакована (не мертва і не досягла мети), наносимо їй шкоду
        if self.target.can_be_targeted():
            self.target.take_damage(self.damage)
        # після влучання в ціль або якщо ціль стала недоступною, деактивуємо кулю
        self.is_active = False