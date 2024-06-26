# MAIAI

This package provides tools to make working with AI simple.

## Installation

You can install this package using pip:

```bash
pip install MAIAI
```

## Components

This project contains two main classes: `Task` and `Agent`.

## Agent

The `Agent` class is defined in the `MAIAI` module. An `Agent` represents an AI model that can perform tasks. It has the following attributes:

- `model`: The name of the AI model.
- `temperature`: The temperature parameter for the AI model, which controls the randomness of the model's output.
- `role`: The role of the AI agent.

## Task

The `Task` class represents a task that an `Agent` can perform. It has the following attributes:

- `agent`: The `Agent` that will perform the task.
- `goal`: The goal of the task.
- `expected_output`: The expected output format of the task.

The `Task` class has a method `execute` that uses the `agent` to perform the task. The `execute` method sends a chat message to the OpenAI API with the `goal` and `expected_output` as content. The API responds with a completion, which is the `agent`'s attempt at performing the task. The `execute` method returns the content of the completion.

## Usage

Here's a basic example of how to use these classes:

```python
from MAIAI import Agent
from MAIAI import Task

# Create an agent
agent = Agent(model="gpt-3.5-turbo", temperature=0.5, role="You are an English to French translator, you translate the text given to you to French.")

# Create a task
task = Task(agent=agent, goal="Hellow world!", expected_output="French Sentence")

# Execute the task
output = task.execute()

# Print the output
print(output)
```
