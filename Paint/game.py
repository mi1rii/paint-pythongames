from turtle import *
import math
from freegames import vector


def line(start, end):
    """
    Draw a line from the start point to the end point.

    Parameters:
    start (vector): The starting point of the line as a vector with x, y coordinates.
    end (vector): The ending point of the line as a vector with x, y coordinates.
    """
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """
    Draw a square using the distance between start and end points.

    Parameters:
    start (vector): The starting point of the square as a vector with x, y coordinates.
    end (vector): The ending point used to calculate the side length of the square.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle_shape(start, end):
    """
    Draw a circle using the distance between the start and end points as the radius.

    Parameters:
    start (vector): The center of the circle as a vector with x, y coordinates.
    end (vector): A point on the circle's circumference used to calculate the radius.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calculate the radius of the circle as the distance between start and end points
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
    up()
    goto(start.x, start.y - radius)  # Move to the top of the circle
    down()
    circle(radius)
    
    end_fill()


def rectangle(start, end):
    """
    Draw a rectangle using the start and end points to determine width and height.

    Parameters:
    start (vector): The starting point of the rectangle as a vector with x, y coordinates.
    end (vector): The ending point used to calculate the width and height of the rectangle.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calculate width and height based on the difference in x and y coordinates
    width = end.x - start.x  
    height = end.y - start.y 

    # Draw the rectangle with two equal long sides and two equal short sides
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)

    end_fill()


def triangle(start, end):
    """
    Draw a triangle using the start and end points to determine the side length.

    The function calculates the side length based on the distance between start and end points
    and draws an equilateral triangle.

    Parameters:
    start (vector): The starting point of the triangle as a vector with x, y coordinates.
    end (vector): A point used to calculate the side length of the triangle.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calculate the side length of the triangle as the distance between start and end points
    side_length = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)

    # Draw the three sides of the triangle, turning 120 degrees after each side
    for _ in range(3):
        forward(side_length)
        left(120)

    end_fill()


def tap(x, y):
    """
    Handle mouse click events to either store the starting point or draw the selected shape.

    If no starting point is stored, the current click's coordinates are stored as the start point.
    If a starting point is already stored, the function will draw the selected shape from the 
    stored start point to the current click's coordinates and reset the start point.

    Parameters:
    x (float): The x-coordinate of the mouse click.
    y (float): The y-coordinate of the mouse click.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """
    Store a value in the global state dictionary with the given key.

    This function is used to change the shape or other parameters based on user input.

    Parameters:
    key (str): The key in the state dictionary to store the value under.
    value (function): The value to store, typically a drawing function (line, square, etc.).
    """
    state[key] = value


# Global state dictionary to store the start point and currently selected shape
state = {'start': None, 'shape': line}

# Set up the drawing canvas
setup(420, 420, 370, 0)

# Register the tap function to handle mouse clicks
onscreenclick(tap)

# Listen for keyboard input to select shapes and colors
listen()

# Register undo function for 'u' key
onkey(undo, 'u')

# Register color changes for keyboard keys
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

# Register shape changes for keyboard keys
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_shape), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# Finish the program
done()
