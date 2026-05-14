import asyncio
import json
from docker_agent.yard_agent import yard_devops
from docker_agent.helper.depfile import find_dep_file
from docker_agent.console.console_api import console


async def create_dockerfile(intent):
    
    dep_filename, version = find_dep_file()

    prompt = f"""
        Generate a Dockerfile based on the following project intent: `{intent}`.
        Use '{dep_filename}' as the dependency file.
        Use Python version '{version}'.
"""
    with console.status(
        "[bold cyan]Generating Dockerfiles files...."
    ):
        output = await yard_devops(prompt)

        print(output)
        
        for doc in output["dockerfiles"]:
            console.print(f"[green] Generating Docker instructions for {doc["dockerfile_name"]}...")  
            with open(doc["dockerfile_name"], "w") as file:
                file.write(doc["dockerfile_instructions"])
                console.print(f"✓ [green] {doc["dockerfile_name"]} created.")

#     print("done")

if __name__ == "__main__":
    asyncio.run(create_dockerfile("""{"intent":"create_dockerfile","runnable_file":[{"file":"modelai.py","folder":"src"}],"mode":"development","response":null}"""))

  
