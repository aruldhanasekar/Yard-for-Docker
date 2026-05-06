from docker_agent.agent import devops_agent
from docker_agent.helper.depfile import find_dep_file




async def create_dockerfile(intent):

    dep_filename, version = find_dep_file()

    prompt = f"""
        Understand the '{intent}', and write a dockerfile. 
        Project uses '{dep_filename} as dependency file'.
        Version of the python is '{version}'.
"""
    docker_instructions = await devops_agent(prompt)

    with open("Dockerfile", "w") as file:
        file.write(docker_instructions)
    
    print("Done")