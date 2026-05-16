from docker_agent.prompt.tasks.examples.dockerfile_example import EXAMPLE_TEMPLATES



def prompt(intent, dep_file, version):
    return f"""Generate a Dockerfile based on the following project intent: `{intent}`.
Use '{dep_file}' as the dependency file.
Use Python version '{version}'.

RULES:
- Generate ONLY valid Dockerfile content and Docker-related instructions that strictly follow the structure and format of the provided example template.
- Do NOT include explanations, markdown, notes, headings, or additional text outside the required Docker output.
- If generating more that one Dockerfile, name each file using the format `Dockerfile.<filename>`.
- If the dependency file is `requirements.txt`, use `pip` as the package manager.
- If the dependency file is `pyproject.toml`, use `uv sync` to install and synchronize dependencies.
- Do not assume or invent the Python version. Use only the Python version explicitly provided by the user. 

EXAMPLES:
`{EXAMPLE_TEMPLATES}'
        
"""