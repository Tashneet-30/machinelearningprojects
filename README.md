# MLProject

## Project Setup

This project is structured to create an ML application as a package so that anybody can install and deploy it.

### Folder Structure
```
MLProject/
│-- src/
│   ├── __init__.py   # Makes src a package
│-- venv/             # Virtual environment
│-- .gitignore        # Files to ignore in Git
│-- requirements.txt  # List of dependencies
│-- setup.py          # Package configuration file
```

### Definitions

- **`src/`**: This folder contains the source code of the project.
- **`__init__.py`**: This makes `src` a package, allowing Python to recognize it.
- **`venv/`**: The virtual environment where dependencies are installed.
- **`.gitignore`**: Specifies files and folders to ignore in Git, such as `venv/` and `__pycache__/`.
- **`requirements.txt`**: Lists all required dependencies for the project.
- **`setup.py`**: A script to package the project, making it installable.

### Today's Checklist-25 February 2025
1. Created a **`src/`** folder and added `__init__.py` to define it as a package.
2. Set up a **virtual environment (venv)** for dependency management.
3. Added a **`.gitignore`** file to exclude unnecessary files.
4. Created a **`requirements.txt`** file to list dependencies.
5. Wrote a **`setup.py`** script to configure the package for installation.

### What is `setup.py`?
The `setup.py` file is responsible for defining the project as an installable package. It includes:
- Package name
- Version number
- Author details
- Required dependencies

### Example `setup.py`
```python
from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """This function returns a list of requirements."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='Tashneet',
    author_email='tashneetkaur343@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
```

This `setup.py` file ensures that the ML project can be installed and used as a package.

The `-e .` (editable mode) is used in requirements.txt to install the package in development mode. This allows you to make changes to the code without reinstalling the package every time.
