import asyncio
import json
from docker_agent.yard_agent import yard_devops
from docker_agent.helper.depfile import find_dep_file


async def create_dockerfile(intent):

    dep_filename, version = find_dep_file()

    prompt = f"""
        Generate a Dockerfile based on the following project intent: `{intent}`.
        Use '{dep_filename}' as the dependency file.
        Use Python version '{version}'.
"""
    docker_instructions = await yard_devops(prompt)

    files = json.loads(docker_instructions)

    for doc in files["dockerfiles"]:
        with open(doc["dockerfile_name"], "w") as file:
            file.write(doc["docker_instructions"])

    print("done")

if __name__ == "__main__":
    asyncio.run(create_dockerfile("""{"intent":"create_dockerfile","runnable_file":[{"file":"modelai.py","folder":"src"}],"mode":"development","response":null}"""))

  
