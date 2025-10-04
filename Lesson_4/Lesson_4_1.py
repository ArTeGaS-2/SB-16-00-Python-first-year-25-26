import turtle as t # Імпорт бібліотеки/модуля "Черепашка"

t.title("Мозаїка") # Заголовок
t.speed(0) # Швидкість
t.bgcolor("white") 
t.tracer(0)

def draw_cell(x, y, size, fill):
    """ Малює зафарбований квадрат з верхнього-лівого кута"""
    t.penup(); t.goto(x, y); t.setheading(0); t.pendown()
    t.color("Black", fill)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

# Параметри сітки
n = 8
cell = 40

# Верхній лівий кут сітки
start_x = -(n * cell) // 2
start_y = (n * cell) // 2

# Вкладені цикли
for i in range(n): # Рядки
    for j in range(n): # Стовбці
        if (i + j) % 2 == 0:
            fill = "white"
        else:
            fill = "gray"
        x = start_x + j * cell
        y = start_y - i * cell
        draw_cell(x, y, cell, fill)

t.hideturtle(); t.done()