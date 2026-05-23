from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
UI_ASSETS_DIR = ASSETS_DIR / "ui"
TILES_ASSETS_DIR = ASSETS_DIR / "tiles"
DATA_DIR = BASE_DIR / "data"

MENU_BACKGROUND_PATH = UI_ASSETS_DIR / "menu_background.png"
BUTTON_IMAGE_PATH = UI_ASSETS_DIR / "button.png"

SIDEBAR_PANEL_PATH = UI_ASSETS_DIR / "sidebar_panel.png"

GRASS_TILE_PATH = TILES_ASSETS_DIR / "grass.png"
ROAD_TILE_PATH = TILES_ASSETS_DIR / "road.png"
SPAWN_TILE_PATH = TILES_ASSETS_DIR / "spawn.png"
GOAL_TILE_PATH = TILES_ASSETS_DIR / "goal.png"
BUILD_SPOT_TILE_PATH = TILES_ASSETS_DIR / "build_spot.png"

MAP_DATA_PATH = DATA_DIR / "map_01.json"

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Tower Defence"
FPS = 60

SIDEBAR_WIDTH = 320
GAME_AREA_WIDTH = WINDOW_WIDTH - SIDEBAR_WIDTH
GAME_AREA_HEIGHT = WINDOW_HEIGHT

SIDEBAR_X = GAME_AREA_WIDTH

TILE_SIZE = 48
MAP_COLS = GAME_AREA_WIDTH // TILE_SIZE
MAP_ROWS = GAME_AREA_HEIGHT // TILE_SIZE

BUTTON_WIDTH = 260
BUTTON_HEIGHT = 90
BUTTON_GAP = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ворог
ENEMIES_ASSETS_DIR = ASSETS_DIR / "enemies"
BASIC_ENEMY_PATH = ENEMIES_ASSETS_DIR / "basic_enemy.png"

BASIC_ENEMY_SPEED = 120 

# Вежа і куля

TOWER_ASSETS_DIR = ASSETS_DIR / "tower"
PROJECTILE_ASSETS_DIR = ASSETS_DIR / "projectiles"

BASIC_TOWER_PATH = TOWER_ASSETS_DIR / "basic_tower.png"
BASIC_BULLET_PATH = PROJECTILE_ASSETS_DIR / "basic_bullet.png"

BASIC_ENEMY_HP = 3 # кількість ударів, які ворог може витримати

BASIC_TOWER_RANGE = 260 # радіус атаки вежі
BASIC_TOWER_FIRE_INTERVAL = 0.5 # час між пострілами в секундах (0.5 означає, що вежа стріляє двічі на секунду)
BASIC_TOWER_DAMAGE = 1 # кількість HP, які знімаються з ворога при попаданні кулі
BASIC_BULLET_SPEED = 340 # швидкість руху кулі в пікселях за секунду (чим більше, тим швидше куля летить до ворога)
BASIC_TOWER_CAN_ROTATE = True # якщо True, то вежа буде повертатися в напрямку ворога при стрільбі;