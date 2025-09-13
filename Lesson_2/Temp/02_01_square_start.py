import turtle as t

t.title("Заняття 2 — перший квадрат") # Текст заголовку
t.speed(6)  # Швидкість руху черепахи
t.pensize(3) # Розмір лінії
t.color("black") # Колір (Python turtle colors)

for i in range(4):        # Кількість ітерацій
    t.forward(100)        # Кількість пікселів пройденихї вперед
    t.left(90)            # Кількість градусів повороту вліво

t.done()
