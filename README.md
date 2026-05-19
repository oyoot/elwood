# Elwood

A minimal Claude Code implementation — a single-loop AI coding agent with tool use.

## What it does

Elwood takes a prompt, sends it to an LLM (Claude Haiku 4.5 via OpenRouter), and enters an agent loop: the model can call tools (read files, write files, run shell commands), observe results, and keep going until it produces a final text response.

## Tools

| Tool | Description |
|------|-------------|
| Read | Read the contents of a file |
| Write | Write content to a file |
| Bash | Execute a shell command |

## Usage

```sh
export OPENROUTER_API_KEY="your-key"
uv run -m app.main -p "your prompt here"
```

## Origin

Built by following the [CodeCrafters "Build Your Own Claude Code" challenge](https://codecrafters.io/challenges/claude-code).
