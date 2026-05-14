from docker_agent.yard_agent import yard_devops





async def dockerignore_file(intent):
    prompt = f"""
    Create a .dockerignore file with these files and directories {intent}
"""
    
    content = await yard_devops(prompt)

    print(content)
