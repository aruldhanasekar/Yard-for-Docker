import json
from pathlib import Path
from docker_agent.console.console_ui import console, success
from docker_agent.logger_config import get_logger


logger = get_logger(__name__)




async def dockerignore_file(intent):

    logger.info(json.dumps(intent, indent=2))
    success(f"Adding ignored files and folders")

    files = intent["ignored"]

    logger.info("Adding ignored files and folders")
    success(f"Adding ignored files and folders")
    for file in files:
      with open(".dockerignore", "a+") as f:
         f.write(f"{file}\n")

    success(".dockerignore file created")
    logger.info("dockerignore file created")