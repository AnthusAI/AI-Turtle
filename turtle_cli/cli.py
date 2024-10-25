import click

from turtle_cli.console import console
from turtle_cli.chat import chat
from turtle_cli.agentic import agentic

@click.group()
def cli():
    """Turtle graphics command line tool."""
    pass

cli.add_command(console)
cli.add_command(chat)
cli.add_command(agentic)

if __name__ == '__main__':
    cli()
