from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de colores para la comida, excluyendo el rojo
food_colors = ['blue', 'yellow', 'purple', 'orange', 'pink']
current_food_color = choice(food_colors)  # Selecciona un color inicial para la comida

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    global current_food_color
    head = snake[-1].copy()
    head.move(aim)

    # Si la cabeza sale de los límites o toca el cuerpo, el juego termina
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        current_food_color = choice(food_colors)  # Cambia el color de la comida al azar
    else:
        snake.pop(0)  

    clear()
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, current_food_color)  # Dibuja la comida con el color actual
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()