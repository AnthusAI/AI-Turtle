import click
import os
import turtle
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def execute_turtle_command(t, command_str):
    """Execute a turtle command and log it."""
    try:
        click.echo(f"\nExecuting: {command_str}")
        # Create a namespace with turtle commands
        namespace = {
            't': t,
            'forward': t.forward,
            'backward': t.backward,
            'right': t.right,
            'left': t.left,
            'goto': t.goto,
            'circle': t.circle,
            'color': t.color,
            'penup': t.penup,
            'pendown': t.pendown,
            'clear': t.clear,
        }
        exec(command_str, namespace)
        click.echo("Command executed successfully")
        return True
    except Exception as e:
        click.echo(f"Error executing command: {e}")
        return False

@click.command()
def chat():
    """Start an AI chat session to control Turtle graphics."""
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        click.echo("OPENAI_API_KEY is not set in the .env file.")
        return

    # Initialize turtle
    t = turtle.Turtle()
    screen = turtle.Screen()
    click.echo("Turtle graphics window initialized")

    # Initialize the AI model
    llm = ChatOpenAI(
        api_key=openai_api_key,
        model="gpt-4o-mini",
        temperature=0
    )
    click.echo("AI model initialized")

    # Define prompt template with user input variable
    prompt = ChatPromptTemplate.from_template(
        """You are a Turtle graphics assistant. You control a turtle object 't'.
        Available commands:
        - t.forward(distance)
        - t.backward(distance)
        - t.right(angle)
        - t.left(angle)
        - t.circle(radius)
        - t.color(color_name)
        - t.penup()
        - t.pendown()
        - t.clear()
        
        User request: {user_input}
        
        Respond ONLY with the exact Python command to execute. 
        For example: t.forward(100) or t.right(90)
        Do not include any other text or explanation."""
    )

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Format prompt with user input
        click.echo("\nSending request to AI...")
        formatted_prompt = prompt.format_messages(user_input=user_input)
        
        # Send to AI model
        response = llm.invoke(formatted_prompt)
        command = response.content.strip()
        click.echo(f"AI response: {command}")

        # Execute the turtle command
        execute_turtle_command(t, command)

    screen.bye()
