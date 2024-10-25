import click

from turtle_cli.console import console

@click.group()
def cli():
    """Turtle graphics command line tool."""
    pass

cli.add_command(console)

if __name__ == '__main__':
    cli()
