import asyncio
import json
from yard.logger_config import get_logger
from yard.yard_agent import yard_devops
from yard.helper.depfile import find_dep_file
from yard.console.console_ui import console, success
from yard.prompt.tasks.dockerfile_prompt import prompt

logger = get_logger(__name__)


async def create_dockerfile(intent):
    
    dep_filename, version = find_dep_file()

    prompts = prompt(intent, dep_filename, version)

    with console.status(
        "[cyan]Generating Dockerfile[/cyan]"
    ):
        logger.info("Dispatching request to yard agent")

        output = await yard_devops(prompts)

        logger.info(json.dumps(output, indent=2))

        
        for doc in output["dockerfiles"]:

            logger.info(f"creating {doc["dockerfile_name"]} and writing instructions")
            success(f"Writing Docker instructions for {doc["dockerfile_name"]}")

            with open(doc["dockerfile_name"], "w") as file:
                file.write(doc["dockerfile_instructions"])

                success(f"Wrote {doc['dockerfile_name']}")
                logger.info(f"{doc["dockerfile_name"]} created successfully")

if __name__ == "__main__":
    asyncio.run(create_dockerfile("""{"intent":"create_dockerfile","runnable_file":[{"file":"modelai.py","folder":"src"}],"mode":"development","response":null}"""))