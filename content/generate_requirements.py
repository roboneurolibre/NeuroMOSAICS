import os
import ast
import json
import importlib.metadata

def extract_imports_from_py(file_path):
    """Extract imports from a Python (.py) file."""
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    imports = {name.name.split('.')[0] for node in ast.walk(tree) if isinstance(node, ast.Import) for name in node.names}
    imports |= {node.module.split('.')[0] for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) and node.module}
    return imports

def extract_imports_from_ipynb(file_path):
    """Extract imports from a Jupyter Notebook (.ipynb) file, ignoring magic commands."""
    with open(file_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    imports = set()
    for cell in notebook.get("cells", []):
        if cell["cell_type"] == "code":
            code_lines = [
                line for line in cell["source"] 
                if not line.strip().startswith(("%", "!", "?"))  # Ignore magic commands
            ]
            try:
                tree = ast.parse("".join(code_lines))
                imports |= {name.name.split('.')[0] for node in ast.walk(tree) if isinstance(node, ast.Import) for name in node.names}
                imports |= {node.module.split('.')[0] for node in ast.walk(tree) if isinstance(node, ast.ImportFrom) and node.module}
            except SyntaxError:
                pass  # Skip cells with unrecognized syntax

    return imports

def get_installed_versions(packages):
    """Get installed package versions."""
    installed_packages = {pkg.metadata["Name"].lower(): pkg.version for pkg in importlib.metadata.distributions()}
    return {pkg: installed_packages.get(pkg.lower(), "latest") for pkg in packages}

def generate_requirements(folder_path):
    """Scan the folder and create a requirements.txt file."""
    all_imports = set()

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".py"):
                all_imports |= extract_imports_from_py(file_path)
            elif file.endswith(".ipynb"):
                all_imports |= extract_imports_from_ipynb(file_path)

    if not all_imports:
        print("No imports found.")
        return

    package_versions = get_installed_versions(all_imports)

    with open("requirements.txt", "w") as f:
        for pkg, version in package_versions.items():
            f.write(f"{pkg}=={version}\n")

    print("✅ requirements.txt generated successfully!")

# Run the script on the current folder
if __name__ == "__main__":
    generate_requirements(".")
