import turtle as t

# Готові допоміжні функції

def draw_string(x1, y, x2):
    t.pensize(2); t.color("black")
    t.penup(); t.goto(x1, y); t.pendown(); t.goto(x2, y)

def draw_pennant(x, y, w, h, color):
    t.color(color)
    t.penup(); t.goto(x, y); t.setheading(0); t.pendown()
    t.begin_fill()
    t.forward(w)
    t.goto(x + w/2, y - h)
    t.goto(x, y)
    t.end_fill()

# Сцена

t.speed(0)
start_x, end_x = -280, 280
y = 150

draw_string(start_x, y, end_x)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
w, h = 40, 50
space = 10

x = start_x + 10      # ▶
color_i = 0           # ▶

while x + w <= end_x - 10:               # ▶
    draw_pennant(x, y, w, h, colors[color_i % len(colors)])  # ▶
    x += w + space                         # ▶
    color_i += 1                           # ▶

# Підпис

t.penup(); t.goto(-50, -180); t.pendown(); t.write("Моя гірлянда!", font=("Arial", 14))

t.done()
