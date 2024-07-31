import os

def create_project_structure():
    base_dir = "LiNotium"
    directories = [
        os.path.join(base_dir, "backend", "app"),
        os.path.join(base_dir, "frontend", "public"),
        os.path.join(base_dir, "frontend", "src", "components")
    ]
    files = [
        os.path.join(base_dir, "backend", "Dockerfile"),
        os.path.join(base_dir, "backend", "requirements.txt"),
        os.path.join(base_dir, "frontend", "package.json"),
        os.path.join(base_dir, "docker-compose.yml"),
        os.path.join(base_dir, "README.md")
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

    for file in files:
        with open(file, 'w') as f:
            f.write("")
        print(f"Created file: {file}")

if __name__ == "__main__":
    create_project_structure()
