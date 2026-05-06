# AI agent for Docker

# This project builds an AI agent for docker. 

# Status
    v0 — under active development.

## What it does
    - Generates a Dockerfile from a simple command
    - Detects the Python version from project metadata
    - Designed to help package a Python app for Docker quickly from the terminal
    
### Example:
    ```bash
            agent "create a dockerfile for this main.py file"

## Privacy:
    - This project does not send raw files, scripts, or .env varibles to the AI.
    - No Data is used for training the AI model. 
    - This project only accesses pyproject.toml or pyvenv.cfg files to determine the user's Python version.