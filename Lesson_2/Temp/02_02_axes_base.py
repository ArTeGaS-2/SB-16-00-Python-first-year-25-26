import turtle as t

t.title("Координати і осі")
t.speed(0)

# Готова функція осей
def draw_axes():
    t.color("gray"); t.pensize(1)
    t.penup(); t.goto(-300, 0); t.pendown(); t.goto(300, 0); t.penup()   # X
    t.goto(0, -200); t.pendown(); t.goto(0, 200); t.penup()             # Y

# ▶ 
points = [(-150, 80), (120, 120), (200, -60), (-100, -120)]  # ▶

draw_axes()

for (x, y) in points:       # ▶
    t.goto(x, y); t.pendown(); t.dot(8); t.penup()   # ▶

# Підпис однієї точки
t.goto(120, 130); t.write("(120,120)")  # ▶

t.done()
