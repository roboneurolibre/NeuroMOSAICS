import os
import ast
import json
import importlib.metadata

def extract_imports_from_py(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=file_path)
    except Exception as e:
        print(f"Failed to parse {file_path}: {str(e)}")
        return set()
    
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.add(name.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def extract_imports_from_ipynb(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"Failed to load {file_path}: {str(e)}")
        return set()

    imports = set()
    for cell in notebook.get("cells", []):
        if cell["cell_type"] == "code":
            code = "".join([
                line for line in cell.get("source", [])
                if not line.strip().startswith(("%", "!", "?"))
            ])
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for name in node.names:
                            imports.add(name.name.split('.')[0])
                    elif isinstance(node, ast.ImportFrom) and node.module:
                        imports.add(node.module.split('.')[0])
            except Exception as e:
                print(f"Failed to parse code in {file_path}: {str(e)}")
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
            print('ok')
            f.write(f"{pkg}=={version}\n")

    print("✅ requirements.txt generated successfully!")

# Run the script on the current folder
if __name__ == "__main__":
    target_dir = os.path.dirname(os.path.abspath(__file__))
    generate_requirements(target_dir)
