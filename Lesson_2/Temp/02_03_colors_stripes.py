import turtle as t

t.title("Кольорові смужки")
t.speed(0)
t.penup() # Піднімає черепашку
t.goto(-280, 120) # Переміщує черепашку на координати в дужках
t.pendown() # Опускає черепашку

# colors = [0,1,2,3,4,5]
colors = ["red", "orange", "yellow", "green", "blue", "purple"] # Список

for c in colors:              
    t.color(c); t.pensize(6)
    t.forward(80)                 # ▶
    t.penup(); t.forward(10); t.pendown()  # ▶
    
t.done()
