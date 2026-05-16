import re
from pathlib import Path
from docker_agent.console.console_ui import console, success


def find_dep_file(start=None):
    if start is None:
        current_root = Path(__file__).resolve()
    else:
        current_root = Path(start).resolve()
    
    
    project_root = [current_root] + list(current_root.parents)

    for parent in project_root:

        with console.status(
                "[cyan]Resolving dependencies[cyan]"
            ):
            # Search for pyproject.toml file in the root directory
            if (parent / "pyproject.toml").exists():

                success("Dependencies resolved")

                with Path.open(parent/"pyproject.toml") as f:
                    config = f.read()

                    with console.status(
                        "[cyan]Detecting Python environment[/cyan]"
                    ):
                        match = re.search(r'requires-python\s*=\s*"((?:<=|>=|==|<|>|=)\s*([0-9.]+))"', config)
                        if match:
                            version = match.group(1)

                            success(f"Detected Python {version}")

                            return "pyproject.toml", version

            # Search for requirements.txt file in the root directory
            elif (parent / "requirements.txt").exists():

                success("✓ Dependencies resolved")

                with console.status(
                        "[cyan]Detecting Python environment[/cyan]"
                    ):
                    for venv_name in [".venv", "venv", "env"]:
                        # Searching python version in the venv
                        cfg = parent / venv_name / "pyvenv.cfg"
                        if cfg.exists():
                            text = cfg.read_text()

                            match = re.search(r"version\s*=\s*([0-9.]+)", text)
                            if match:
                                version = match.group(1)

                                success(f"Detected Python {version}")

                                return "requirements.txt", version
                
    return None, None
        


if __name__ == "__main__":
   print(find_dep_file())
