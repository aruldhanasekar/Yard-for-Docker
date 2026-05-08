import re
from pathlib import Path


def find_dep_file(start=None):
    if start is None:
        current_root = Path(__file__).resolve()
    else:
        current_root = Path(start).resolve()
    
    
    project_root = [current_root] + list(current_root.parents)

    for parent in project_root:
        if (parent / "pyproject.toml").exists():
            with Path.open(parent/"pyproject.toml") as f:
                config = f.read()

                match = re.search(r'requires-python\s*=\s*"((?:<=|>=|==|<|>|=)\s*([0-9.]+))"', config)
                if match:
                    version = match.group(1)

                    return "pyproject.toml", version       

        elif (parent / "requirements.txt").exists():
            for venv_name in [".venv", "venv", "env"]:
                cfg = parent / venv_name / "pyvenv.cfg"
                if cfg.exists():
                    text = cfg.read_text()

                    match = re.search(r"version\s*=\s*([0-9.]+)", text)
                    if match:
                        version = match.group(1)

                        return "requirements.txt", version
                
    return None, None
        


if __name__ == "__main__":
   print(find_dep_file())
