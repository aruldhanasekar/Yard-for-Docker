# Yard for Docker

Yard is an AI agent for Docker. In this first version, it helps developers instantly create Dockerfiles for their projects.

## Status

v0 — under active development.

## What it does

* Generates one or more Dockerfiles and a .dockerignore file from a simple command
* Detects the Python version from project metadata
* Is designed to help package a Python app for Docker quickly from the terminal
* 

## Example

```bash
yard "create a dockerfile for this main.py file"
```

## Privacy

* This project does not send raw files, scripts, or `.env` variables to the AI.
* No data is used for training the AI model.
* This project only accesses `pyproject.toml` or `pyvenv.cfg` files to determine the user's Python version.

