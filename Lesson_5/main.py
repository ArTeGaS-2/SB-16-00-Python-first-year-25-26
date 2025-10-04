import random

num = random.randint(1, 100) # Контейнер для випадкового числа
counter = 0 # Лічильник

while True: # Цикл
    guess = input("Вгадайте число, від 1 до 100: ")
    
    if num == int(guess):
        print(f"Вірно. Кількість спроб {counter}")
        break
    elif num > int(guess):
        print("Більше")
    elif num < int(guess):
        print("Менше")
    counter += 1 # +1 до лічильника