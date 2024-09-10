"""
Memory Game

This script implements a simple memory game using the Turtle graphics library. The game involves a ball and targets that move across the screen. The player can interact with the game by tapping on the screen, which affects the ball's movement.

Dependencies:
- random: for generating random positions for targets.
- turtle: for drawing and handling user interactions.
- freegames.vector: for vector operations used in ball and target movements.

The main components of the game include:
- Ball: The player's object that moves according to user input.
- Targets: Moving objects that the player should avoid or interact with.
"""

from random import randrange
from turtle import *
from freegames import vector

# Initialize ball and target variables
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """
    Respond to screen tap by adjusting the ball's speed and position.

    Parameters:
    x (float): The x-coordinate of the screen tap.
    y (float): The y-coordinate of the screen tap.
    """
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10

def inside(xy):
    """
    Check if a given point is within the screen bounds.

    Parameters:
    xy (vector): The vector representing the point to check.

    Returns:
    bool: True if the point is within screen bounds, otherwise False.
    """
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """
    Draw the ball and targets on the screen. Clears the previous drawings 
    and updates the screen with the current state of the game.
    """
    clear()

    for target in targets:
        goto(target.x, target.y)
        begin_fill()
        color('purple')
        for _ in range(4): 
            forward(20)
            left(90)
        end_fill()

    if inside(ball):
        goto(ball.x, ball.y)
        begin_fill()
        color('turquoise')
        for _ in range(3): 
            forward(10)
            left(120)
        end_fill()

    update()

def move():
    """
    Move the ball and targets across the screen. Introduces new targets 
    randomly and updates their positions. Adjusts the ball's speed based 
    on gravity and user interaction. Also manages the ball's collision 
    with targets and screen edges.
    """
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            if not inside(target):
                target.x = 200
                target.y = randrange(-150, 150)
            targets.append(target)

    draw()

    ontimer(move, 50)

# Setup the screen and initial conditions
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()