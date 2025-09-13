import turtle as t

t.speed(6)

# Квадрат стін
for _ in range(4):     # ▶
    t.forward(120)     # ▶
    t.left(90)         # ▶

# Перехід у верхній лівий кут квадрату (початок даху)
t.penup(); t.left(90); t.forward(120); t.right(90); t.pendown()   # ▶

# Дах (рівносторонній трикутник угорі)
for _ in range(3):     # ▶
    t.forward(120)     # ▶
    t.left(120)        # ▶

t.done()
