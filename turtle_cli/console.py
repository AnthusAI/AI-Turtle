import code
import sys
import click
import turtle

class TurtleConsole(code.InteractiveConsole):
    def __init__(self):
        # Initialize with turtle commands in namespace
        namespace = {
            't': turtle.Turtle(),
            'forward': turtle.forward,
            'backward': turtle.backward,
            'right': turtle.right,
            'left': turtle.left,
            'goto': turtle.goto,
            'circle': turtle.circle,
            'color': turtle.color,
            'penup': turtle.penup,
            'pendown': turtle.pendown,
            'clear': turtle.clear,
        }
        super().__init__(namespace)

@click.command()
def console():
    """Start an interactive Turtle graphics console.
    
    Common commands:
    - forward(distance)
    - backward(distance) 
    - right(angle)
    - left(angle)
    - circle(radius)
    - color(color_name)
    - penup()
    - pendown()
    - clear()
    """
    turtle_console = TurtleConsole()
    turtle_console.interact(
        banner="Welcome to Turtle Console! Type help() for help."
    )
