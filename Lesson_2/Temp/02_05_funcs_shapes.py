import turtle as t

def draw_square(size, color="black"):
    t.color(color)
    for _ in range(4):      # ▶
        t.forward(size)     # ▶
        t.left(90)          # ▶

def draw_triangle(size, color="black"):
    t.color(color)
    for _ in range(3):      # ▶
        t.forward(size)     # ▶
        t.left(120)         # ▶

t.speed(7)
draw_square(80, "orange")     # ▶
t.penup(); t.goto(-120, -50); t.pendown()  # ▶
draw_triangle(100, "blue")    # ▶

t.done()
