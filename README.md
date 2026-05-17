# Yard for Docker

Yard is a terminal-based AI agent for Docker.

## Status

v1 — under active development.

## What it does

- Generates one or more Dockerfiles and a `.dockerignore` file from a simple command
- Detects the Python version from project metadata
- Helps package Python applications for Docker quickly from the terminal

## Install

```bash
pipx install yardx
```

## Setup

Yard currently uses OpenAI models.

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your_api_key"
```

### Linux/macOS

```bash
export OPENAI_API_KEY="your_api_key"
```

## Example

```bash
yard "create a dockerfile for this main.py file"
```

## Privacy

- This project does not send raw files, scripts, or `.env` variables to the AI
- No data is used for training AI models
- Yard only reads `pyproject.toml` or `pyvenv.cfg` files to detect the Python version

## License

MIT
