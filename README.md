# Turtle-CLI: AI-Powered Turtle Graphics

This project combines Python's Turtle graphics with AI to create an interactive drawing tool. It provides three different ways to control the turtle:

1. A Python REPL console for direct turtle commands
2. A simple AI chat interface that executes single commands
3. An AI agent that thinks step-by-step through complex drawings

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/turtle-cli.git
cd turtle-cli

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .

# Create a .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" > .env
```

## Commands

### `turtle-cli console`

A Python REPL with turtle commands pre-loaded. Perfect for direct control and experimentation.

```bash
$ turtle-cli console
Welcome to Turtle Console! Type help() for help.
>>> forward(100)
>>> right(90)
>>> circle(50)
```

Available commands:
- `forward(distance)`
- `backward(distance)`
- `right(angle)`
- `left(angle)`
- `circle(radius)`
- `color(color_name)`
- `penup()`
- `pendown()`
- `clear()`

### `turtle-cli chat`

A simple AI chat interface that converts your natural language requests into single turtle commands.

```bash
$ turtle-cli chat
You: Move forward 100 steps
AI: t.forward(100)
You: Turn right 90 degrees
AI: t.right(90)
```

The AI will interpret your request and execute a single turtle command each time.

### `turtle-cli agentic`

An AI agent that can handle complex drawing requests by thinking through them step by step.

```bash
$ turtle-cli agentic
You: Draw a house
💭 I'll start by drawing the base square
Action: t.forward(100)
👁️ The turtle moves forward to create the first wall
...
✅ Drawing complete!
```

The agent will:
1. Think about each step
2. Execute the appropriate command
3. Observe the result
4. Continue until the drawing is complete

## Examples

Try these commands with the agentic interface:
- "Draw a house"
- "Make a spiral"
- "Draw a star"
- "Create a flower pattern"

The agent will break down complex drawings into simple steps and execute them while explaining its thought process.

## Exit

To exit any command, type `exit` or `quit`.

## Requirements

- Python 3.8+
- OpenAI API key (for chat and agentic commands)
- Required packages (installed automatically):
  - click
  - langchain
  - openai
  - python-dotenv
  - langgraph
