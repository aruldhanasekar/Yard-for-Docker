# Yard for Docker

Yard is an AI agent for Docker, at first version that helps developers instantly create Dockerfiles for their projects.

# Status
    v0 — under active development.

## What it does
    Generates a one or more Dockerfile from a simple command
    Detects the Python version from project metadata
    Designed to help package a Python app for Docker quickly from the terminal

    
### Example:
    ```bash
            yard "create a dockerfile for this main.py file" 
    ```

## Privacy:
    This project does not send raw files, scripts, or .env varibles to the AI.
    No Data is used for training the AI model. 
    This project only accesses pyproject.toml or pyvenv.cfg files to determine the user's Python version.
