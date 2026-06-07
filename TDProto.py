import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Tower Defence")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)

# -------- PATH --------

path = [
    (0, 350),
    (140, 350),
    (140, 160),
    (320, 160),
    (320, 520),
    (520, 520),
    (520, 240),
    (720, 240),
    (720, 460),
    (1000, 460)
]

PATH_WIDTH = 80

# -------- GAME STATE --------

money = 250
lives = 20
wave = 0
selected_tower = 1

enemies = []
towers = []
projectiles = []
spawn_queue = []
spawn_timer = 0

# -------- DATA --------

enemy_types = {
    "small": {
        "hp": 40,
        "speed": 1.8,
        "reward": 10,
        "color": (80, 200, 255),
        "radius": 13
    },
    "normal": {
        "hp": 80,
        "speed": 1.2,
        "reward": 18,
        "color": (255, 180, 60),
        "radius": 16
    },
    "tank": {
        "hp": 180,
        "speed": 0.7,
        "reward": 35,
        "color": (220, 80, 80),
        "radius": 20
    }
}

tower_types = {
    1: {
        "name": "Basic",
        "cost": 60,
        "range": 130,
        "damage": 20,
        "cooldown": 40,
        "color": (100, 220, 100)
    },
    2: {
        "name": "Sniper",
        "cost": 100,
        "range": 220,
        "damage": 50,
        "cooldown": 90,
        "color": (160, 120, 255)
    },
    3: {
        "name": "Rapid",
        "cost": 85,
        "range": 110,
        "damage": 10,
        "cooldown": 15,
        "color": (255, 230, 80)
    }
}

# -------- HELPERS --------

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def point_near_segment(px, py, ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay

    if dx == 0 and dy == 0:
        return distance((px, py), (ax, ay))

    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0, min(1, t))

    closest_x = ax + t * dx
    closest_y = ay + t * dy

    return distance((px, py), (closest_x, closest_y))


def is_on_path(pos):
    x, y = pos

    for i in range(len(path) - 1):
        ax, ay = path[i]
        bx, by = path[i + 1]

        if point_near_segment(x, y, ax, ay, bx, by) < PATH_WIDTH / 2:
            return True

    return False


def can_place_tower(pos):
    if is_on_path(pos):
        return False

    for tower in towers:
        if distance(pos, tower.pos) < 45:
            return False

    return True


# -------- CLASSES --------

class Enemy:
    def __init__(self, enemy_type):
        data = enemy_types[enemy_type]

        self.enemy_type = enemy_type
        self.max_hp = data["hp"]
        self.hp = data["hp"]
        self.speed = data["speed"]
        self.reward = data["reward"]
        self.color = data["color"]
        self.radius = data["radius"]

        self.path_index = 0
        self.x, self.y = path[0]

    @property
    def pos(self):
        return (self.x, self.y)

    def update(self):
        global lives

        if self.path_index >= len(path) - 1:
            lives -= 1
            enemies.remove(self)
            return

        target_x, target_y = path[self.path_index + 1]
        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy)

        if dist < self.speed:
            self.x = target_x
            self.y = target_y
            self.path_index += 1
        else:
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        hp_ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, (80, 0, 0), (self.x - 20, self.y - 28, 40, 5))
        pygame.draw.rect(screen, (0, 220, 0), (self.x - 20, self.y - 28, 40 * hp_ratio, 5))


class Tower:
    def __init__(self, pos, tower_type):
        data = tower_types[tower_type]

        self.x, self.y = pos
        self.tower_type = tower_type

        self.range = data["range"]
        self.damage = data["damage"]
        self.cooldown = data["cooldown"]
        self.color = data["color"]

        self.timer = 0

    @property
    def pos(self):
        return (self.x, self.y)

    def update(self):
        if self.timer > 0:
            self.timer -= 1
            return

        target = self.find_target()

        if target:
            projectiles.append(Projectile(self.pos, target, self.damage))
            self.timer = self.cooldown

    def find_target(self):
        enemies_in_range = []

        for enemy in enemies:
            if distance(self.pos, enemy.pos) <= self.range:
                enemies_in_range.append(enemy)

        if not enemies_in_range:
            return None

        # Стріляємо по ворогу, який далі пройшов по шляху
        return max(enemies_in_range, key=lambda e: e.path_index)

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, 22)
        pygame.draw.circle(screen, (30, 30, 30), self.pos, 22, 3)

        # Радіус показуємо тільки для вибраної/наведеної логіки можна додати пізніше
        mouse_pos = pygame.mouse.get_pos()
        if distance(mouse_pos, self.pos) < 25:
            pygame.draw.circle(screen, (120, 120, 120), self.pos, self.range, 1)


class Projectile:
    def __init__(self, pos, target, damage):
        self.x, self.y = pos
        self.target = target
        self.damage = damage
        self.speed = 7
        self.radius = 5

    def update(self):
        global money

        if self.target not in enemies:
            projectiles.remove(self)
            return

        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = math.hypot(dx, dy)

        if dist < self.speed:
            self.target.hp -= self.damage

            if self.target.hp <= 0:
                money += self.target.reward
                enemies.remove(self.target)

            projectiles.remove(self)
        else:
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)


# -------- WAVE --------

def start_wave():
    global wave, spawn_queue

    if spawn_queue or enemies:
        return

    wave += 1
    spawn_queue = []

    for i in range(6 + wave * 2):
        spawn_queue.append("small")

    for i in range(3 + wave):
        spawn_queue.append("normal")

    if wave >= 3:
        for i in range(wave - 2):
            spawn_queue.append("tank")

    random.shuffle(spawn_queue)


def spawn_enemies():
    global spawn_timer

    if not spawn_queue:
        return

    spawn_timer -= 1

    if spawn_timer <= 0:
        enemy_type = spawn_queue.pop(0)
        enemies.append(Enemy(enemy_type))
        spawn_timer = 35


# -------- DRAW --------

def draw_path():
    for i in range(len(path) - 1):
        pygame.draw.line(screen, (130, 100, 65), path[i], path[i + 1], PATH_WIDTH)

    for point in path:
        pygame.draw.circle(screen, (130, 100, 65), point, PATH_WIDTH // 2)

    pygame.draw.circle(screen, (60, 220, 60), path[0], 35)
    pygame.draw.circle(screen, (220, 60, 60), path[-1], 35)

    start_text = font.render("START", True, (0, 0, 0))
    finish_text = font.render("FINISH", True, (0, 0, 0))

    screen.blit(start_text, (20, 305))
    screen.blit(finish_text, (900, 415))


def draw_ui():
    selected = tower_types[selected_tower]

    text = f"Money: {money}   Lives: {lives}   Wave: {wave}   Selected: {selected['name']} (${selected['cost']})"
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (20, 15))

    hint = "1 Basic | 2 Sniper | 3 Rapid | LMB place tower | SPACE start wave"
    hint_img = font.render(hint, True, (210, 210, 210))
    screen.blit(hint_img, (20, 45))

    mouse_pos = pygame.mouse.get_pos()

    if can_place_tower(mouse_pos) and money >= selected["cost"]:
        color = (80, 255, 80)
    else:
        color = (255, 80, 80)

    pygame.draw.circle(screen, color, mouse_pos, selected["range"], 1)
    pygame.draw.circle(screen, selected["color"], mouse_pos, 18)


def draw_game_over():
    text = font.render("GAME OVER", True, (255, 80, 80))
    screen.blit(text, (WIDTH // 2 - 70, HEIGHT // 2))


# -------- MAIN LOOP --------

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_tower = 1
            elif event.key == pygame.K_2:
                selected_tower = 2
            elif event.key == pygame.K_3:
                selected_tower = 3
            elif event.key == pygame.K_SPACE:
                start_wave()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                tower_data = tower_types[selected_tower]

                if money >= tower_data["cost"] and can_place_tower(pos):
                    towers.append(Tower(pos, selected_tower))
                    money -= tower_data["cost"]

    if lives > 0:
        spawn_enemies()

        for enemy in enemies[:]:
            enemy.update()

        for tower in towers:
            tower.update()

        for projectile in projectiles[:]:
            projectile.update()

    screen.fill((35, 45, 55))

    draw_path()

    for tower in towers:
        tower.draw()

    for enemy in enemies:
        enemy.draw()

    for projectile in projectiles:
        projectile.draw()

    draw_ui()

    if lives <= 0:
        draw_game_over()

    pygame.display.flip()

pygame.quit()