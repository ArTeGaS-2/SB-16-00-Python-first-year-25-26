import pygame
import sys

# вікно
WIDTH, HEIGHT = 800, 600
BG_COLOR = (125,125,125)
TEXT_COLOR = (255,255,255)
FPS = 60

BUTTON_IMAGE_PATH = "button.png"
TEXT_TEMPLATE = "Кліків: {}"

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Клікер - базова версія")
    clock = pygame.time.Clock()

    # Шрифт
    font = pygame.font.SysFont("arial", 36)

    button_img = pygame.image.load(BUTTON_IMAGE_PATH).convert_alpha()
    button_img = pygame.transform.scale(button_img, (200, 200))

    # Головний цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((125,125,125))
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

