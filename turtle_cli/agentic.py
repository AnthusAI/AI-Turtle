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
        namespace = {
            't': t,
            'forward': t.forward,
            'backward': t.backward,
            'right': t.right,
            'left': t.left,
            'circle': t.circle,
            'color': t.color,
        }
        exec(command_str, namespace)
        return True
    except Exception as e:
        click.echo(f"Error executing command: {e}")
        return False

@click.command()
def agentic():
    """Start an AI agent session to control Turtle graphics."""
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        click.echo("OPENAI_API_KEY is not set in the .env file.")
        return

    t = turtle.Turtle()
    screen = turtle.Screen()
    click.echo("Turtle graphics window initialized")

    llm = ChatOpenAI(
        api_key=openai_api_key,
        model="gpt-4",
        temperature=0
    )
    click.echo("AI agent initialized")

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a Turtle graphics assistant that thinks step by step.
        Available commands:
        - t.forward(distance)
        - t.backward(distance)
        - t.right(angle)
        - t.left(angle)
        - t.circle(radius)
        - t.color(color_name)
        
        For each action:
        1. Think: Explain what you plan to do and why
        2. Action: Write the exact Python command
        3. Observe: Describe what that command will do
        
        After all commands, write "DONE" on a new line.
        
        Example:
        Think: I'll start by making the line red
        Action: t.color('red')
        Observe: The turtle will now draw in red
        
        Think: Now I'll move forward to start the line
        Action: t.forward(100)
        Observe: The turtle moves forward 100 units
        
        DONE"""),
        ("human", "{input}")
    ])

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        click.echo("\nThinking...")
        messages = prompt.format_messages(input=user_input)
        response = llm.invoke(messages)
        
        current_section = None
        command = None
        
        for line in response.content.strip().split('\n'):
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('Think:'):
                click.echo(f"\n💭 {line[6:].strip()}")
            elif line.startswith('Action:'):
                command = line[7:].strip()
                execute_turtle_command(t, command)
            elif line.startswith('Observe:'):
                click.echo(f"👁️  {line[8:].strip()}")
            elif line == 'DONE':
                click.echo("\n✅ Drawing complete!")

    screen.bye()
