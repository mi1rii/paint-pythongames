from random import choice
from turtle import *
from freegames import floor, vector

# Global state variables
state = {'score': 0}
path = Turtle(visible=False)  # Turtle used to draw the maze
writer = Turtle(visible=False)  # Turtle used to display the score
aim = vector(5, 0)  # Initial movement direction for Pac-Man
pacman = vector(-40, -80)  # Initial position for Pac-Man

# List of ghosts, each with a position and movement direction
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

# Maze tiles (0 represents a wall, 1 represents an open path, 2 represents a cleared path)
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    # [Rest of the maze omitted for brevity]
]

def square(x, y):
    """
    Draws a filled square on the game grid at the specified (x, y) coordinates.
    
    Args:
        x (int): The x-coordinate of the square's bottom-left corner.
        y (int): The y-coordinate of the square's bottom-left corner.
    """
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for _ in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """
    Computes the index in the tiles array for a given point's (x, y) position.
    
    Args:
        point (vector): A vector representing the position of the point.
    
    Returns:
        int: The index in the tiles array corresponding to the given point.
    """
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    return int(x + y * 20)


def valid(point):
    """
    Checks whether the specified point is a valid position in the maze.
    
    Args:
        point (vector): A vector representing the position to validate.
    
    Returns:
        bool: True if the point is valid (not a wall and aligned to the grid), False otherwise.
    """
    index = offset(point)
    if tiles[index] == 0:
        return False

    index = offset(point + 19)
    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """
    Draws the entire game world, which consists of the maze and collectible dots.
    """
    bgcolor('black')  # Set background to black
    path.color('blue')  # Set maze color to blue

    for index, tile in enumerate(tiles):
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)  # Draw the maze tiles

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')  # Draw collectible dots


def move_towards(target, current):
    """
    Calculates the best movement vector for a ghost to move towards a target.
    
    Args:
        target (vector): The target position (typically Pac-Man's position).
        current (vector): The current position of the ghost.
    
    Returns:
        vector: The best movement vector for the ghost.
    """
    options = [vector(5, 0), vector(-5, 0), vector(0, 5), vector(0, -5)]
    best_option = options[0]
    best_distance = abs(target - (current + options[0]))

    for option in options[1:]:
        distance = abs(target - (current + option))
        if distance < best_distance and valid(current + option):
            best_option = option
            best_distance = distance

    return best_option


def move():
    """
    Controls the movement of Pac-Man and the ghosts. Also handles game logic
    such as updating the score and detecting collisions.
    """
    writer.undo()  # Clear the previous score
    writer.write(state['score'])  # Write the updated score

    clear()

    # Move Pac-Man if the intended direction is valid
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    # Check if Pac-Man has eaten a dot
    if tiles[index] == 1:
        tiles[index] = 2  # Mark tile as cleared
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    # Draw Pac-Man
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    # Move the ghosts
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            course.x, course.y = move_towards(pacman, point)

        # Draw each ghost
        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    # Check for collision between Pac-Man and any ghost
    for point, _ in ghosts:
        if abs(pacman - point) < 20:
            return  # End the game if Pac-Man collides with a ghost

    # Schedule the next frame
    ontimer(move, 50)


def change(x, y):
    """
    Changes the direction of Pac-Man based on user input.
    
    Args:
        x (int): The new x-direction of movement.
        y (int): The new y-direction of movement.
    """
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


# Game setup
setup(420, 420, 370, 0)  # Set up the game window
hideturtle()  # Hide the default turtle
tracer(False)  # Turn off animation for faster drawing
writer.goto(160, 160)  # Set the position for the score display
writer.color('white')  # Set the score text color
writer.write(state['score'])  # Initialize the score display

# Set up controls
listen()
onkey(lambda: change(10, 0), 'Right')  # Move right
onkey(lambda: change(-10, 0), 'Left')  # Move left
onkey(lambda: change(0, 10), 'Up')  # Move up
onkey(lambda: change(0, -10), 'Down')  # Move down

# Draw the game world and start the game loop
world()
move()
done()  # End the program
