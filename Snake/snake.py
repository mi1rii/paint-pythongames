from turtle import *  # Imports all functions from the turtle module
from random import randrange, choice  # Imports functions for generating random numbers and selecting elements
from freegames import square, vector  # Imports functions from the freegames library

# Initialization of the game's initial state
food = vector(0, 0)  # Initial position of the food
snake = [vector(10, 0)]  # Initial position of the snake (list of segments)
aim = vector(0, -10)  # Initial movement direction of the snake

# List of colors for the food, excluding red (used to indicate collision)
food_colors = ['blue', 'yellow', 'purple', 'orange', 'pink']
current_food_color = choice(food_colors)  # Selects an initial color for the food

def change(x, y):
    """
    Change the snake's direction.

    Args:
        x (int): Movement along the X-axis.
        y (int): Movement along the Y-axis.

    Updates the direction in which the snake moves.
    """
    aim.x = x
    aim.y = y

def inside(head):
    """
    Check if the snake's head is inside the game boundaries.

    Args:
        head (vector): The position of the snake's head.

    Returns:
        bool: True if the head is inside the boundaries, False otherwise.
    """
    return -200 < head.x < 190 and -200 < head.y < 190

# List of colors for the snake's body, including a random selection
colors = ['black', 'blue', 'yellow', 'purple', 'orange', 'pink']
selected_color = colors[randrange(0, len(colors))]  # Randomly selects a color for the snake's body

def move():
    """
    Move the snake forward by one segment and handle game events.

    This function handles the snake's movement, food consumption, 
    and collision detection. The snake continues to move until it 
    collides with the wall or itself. If it eats the food, the food 
    is relocated to a random position, and the snake's length increases.
    """
    global current_food_color
    head = snake[-1].copy()  # Create a copy of the snake's head
    head.move(aim)  # Move the head in the direction of the current aim

    # End the game if the snake's head is outside boundaries or touches its body
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Draw the head in red to indicate collision
        update()  # Refresh the screen to show the red head
        return  # Stop further execution

    snake.append(head)  # Add the new head position to the snake

    if head == food:
        print('Snake:', len(snake))  # Print the current length of the snake
        food.x = randrange(-15, 15) * 10  # Randomly reposition the food on the x-axis
        food.y = randrange(-15, 15) * 10  # Randomly reposition the food on the y-axis
        current_food_color = choice(food_colors)  # Change the food's color randomly
    else:
        snake.pop(0)  # Remove the last segment of the snake if food not eaten

    clear()  # Clear the screen before redrawing the snake and food
    for body in snake:
        square(body.x, body.y, 9, selected_color)  # Draw each segment of the snake

    square(food.x, food.y, 9, current_food_color)  # Draw the food with its current color
    update()  # Update the screen with the new drawings
    ontimer(move, 100)  # Continue moving the snake every 100 milliseconds

# Setup the game screen and controls
setup(420, 420, 370, 0)  # Set up the game window size and position
hideturtle()  # Hide the default turtle cursor
tracer(False)  # Disable automatic animation for better control
listen()  # Start listening for user input

# Map keyboard keys to change the snake's direction
onkey(lambda: change(10, 0), 'Right')  # Move right
onkey(lambda: change(-10, 0), 'Left')  # Move left
onkey(lambda: change(0, 10), 'Up')  # Move up
onkey(lambda: change(0, -10), 'Down')  # Move down

move()  # Start the movement of the snake
done()  # End the turtle graphics loop when the game is over