import turtle as t

# Функція що малює квадрат, з параметрами (Розмір, Колір="Чорний")
def draw_square(size, color="Black"):
    t.color(color) # Вибір кольору
    for i in range(4): # Цикл, повторює дії 4 рази
        t.forward(size) # Рух вперед в пікселях
        t.left(90) # Поворот вліво, в градусах

def draw_triangle(size, color="Black"):
    t.color(color) # Вибір кольору
    for i in range(3): # Цикл, повторює дії 3 рази
        t.forward(size) # Рух вперед в пікселях
        t.left(120) # Поворот вліво, в градусах

t.speed(7) # Визначає швидкість

draw_square(80, "orange")

t.penup()
t.goto(-120,-50)
t.pendown()

draw_triangle(100, "blue")

t.done()