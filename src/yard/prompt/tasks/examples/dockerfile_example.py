EXAMPLE_TEMPLATES = """
#Example-1:
INPUT: 
Generate a Dockerfile based on the following project intent: 
`{
    "task":"create_dockerfile",
                 "runnable":[
                        {
                          "file":"modelai.py",
                          "folder":"src"
                        },
                        {
                          "file": "main.py",
                          "folder" : null
                        }
                ]
}`.
Use 'pyproject.toml' as the dependency file.
Use Python version '=> 3.13'.

Output: 
    `{'dockerfiles' : [{
            'dockerfile_name' : 'Dockerfile.modelai',
            'dockerfile_instructions' : '
                                         FROM python:3.13-slim

                                         # Prevents Python from creating .pyc files
                                         # Ensures logs are shown immediately in Docker
                                         # Makes uv use the system Python inside the container
                                         PYTHONDONETWRITEBYTECODE=1 \
                                         PYTHONUNBUFFERED=1 \
                                         UV_SYSTEM_PYTHON=1
                                         
                                         # Set working directory
                                         WORKDIR /app 

                                         # Install uv package manager
                                         RUN pip install -no-cache-dir uv

                                         # Copy dependency files
                                         COPY pyproject.toml uv.lock ./

                                         # Install project dependencies
                                         RUN uv sync --frozen --no-dev --no-cache
                                         
                                         # Copy application source code
                                         COPY src/ ./src/
                                         
                                         # Start the application
                                         CMD ["uv", "run", "-m", "src.modelai"] '

            },
            {
               'dockerfile_name' : 'Dockerfile.main',
                'dockerfile_instructions' : '
                                         FROM python:3.13-slim

                                         # Prevents Python from creating .pyc files
                                         # Ensures logs are shown immediately in Docker
                                         # Makes uv use the system Python inside the container
                                         PYTHONDONETWRITEBYTECODE=1 \
                                         PYTHONUNBUFFERED=1 \
                                         UV_SYSTEM_PYTHON=1
                                         
                                         # Set working directory
                                         WORKDIR /app 

                                         # Install uv package manager
                                         RUN pip install -no-cache-dir uv

                                         # Copy dependency files
                                         COPY pyproject.toml uv.lock* ./

                                         # Install project dependencies
                                         RUN uv sync --frozen --no-dev --no-cache
                                         
                                         # Copy application source code
                                         COPY . .
                                         
                                         # Start the application
                                         CMD ["uv", "run", "main.py"] ' 
            
            }]  }`

            
##Example - 2:
INPUT: 
Generate a Dockerfile based on the following project intent: 
`{
    "task":"create_dockerfile",
                 "runnable":[
                        {
                          "file":"main.py",
                          "folder": null
                        },
                        {
                          "file": "app.py",
                          "folder" : app
                        }
                ]
}`.
Use 'requirements.txt' as the dependency file.
Use Python version '=> 3.13'.


OUTPUT:
`{ 'dockerfiles': [
                {
                    'dockerfile_name' : 'Dockerfile.main',
                    'docker_instructions': '
                                             FROM python:3.13-slim

                                             # Prevents Python from creating .pyc files
                                             # Ensures logs are shown immediately in Docker
                                             ENV PYTHONDONTWRITEBYTECODE=1 \
                                             PYTHONUNBUFFERED=1

                                            # Set working directory
                                            WORKDIR / app

                                            # Copy project files
                                            COPY requirements.txt .

                                            # Install dependencies
                                            RUN pip install --no-cache-dir -r requirements.txt

                                            # Copy application source code
                                            COPY . .

                                            # Run main.py
                                            CMD ["python", "main.py"] '
                },
                {
                    'dockerfile_name' : 'Dockerfile.app',
                    'docker_instructions': '
                                            FROM python:3.13-slim

                                            # Prevents Python from creating .pyc files
                                            # Ensures logs are shown immediately in Docker
                                            ENV PYTHONDONTWRITEBYTECODE=1 \
                                                PYTHONUNBUFFERED=1

                                            # Set working directory
                                            WORKDIR /app

                                            # Copy dependency file
                                            COPY requirements.txt .

                                            # Install project dependencies
                                            RUN pip install --no-cache-dir -r requirements.txt

                                            # Copy application source code
                                            COPY app/ ./app/

                                            # Start the application
                                            CMD["python", "-m", "app.app"]
                
                }]}`


"""