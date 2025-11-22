import pygame
import sys

# Налаштування вікна
width, height = 800, 600
FPS = 60
bg_color = (30,30,40)

def main():
    pygame.init() # ініціалізація
    pygame.display.set_caption("Бачимо і пишимо")
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    # Шрифт і текст
    font = pygame.font.SysFont("consolas", 32)

    current_pharse = "small car-race, go."
    remaining_text = current_pharse

    distance = 0 # скільки "умовних одиниць" траси машина вже проїхала

    car_y = height // 2 # Машина по середині екрану за висотою
    car_base_x = 100 # стартова позиція машини по ширині
    car_width, car_height = 80, 40

    running = True
    while running:
        # 1) Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    distance += 10
        
        # 2) Логіка гри (пуста)
        car_x = car_base_x + distance

        # 3) Малюванню
        screen.fill(bg_color)

        pygame.draw.rect(screen,
            (200,50,50),                     # Червоний колір
            (car_x, car_y - car_height // 2, # x,y центр по вертикалі
            car_width, car_height))         # ширина і висота

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()