import json
from docker_agent.yard_agent import yard_devops
from docker_agent.helper.depfile import find_dep_file




async def create_dockerfile(intent):

    dep_filename, version = find_dep_file()

    prompt = f"""
        Understand the '{intent}', and write a dockerfile. 
        Project uses '{dep_filename} as dependency file'.
        Version of the python is '{version}'.
"""
    docker_instructions = await yard_devops(prompt)

    files = json.loads(docker_instructions)

    # Creating multiple Dockerfiles with the running filename as the extension
    for file in files["dockerfiles"]:
        with open(file["dockerfile_name"], "w", encoding="utf-8") as df:
            df.write(file["docker_instructions"])
