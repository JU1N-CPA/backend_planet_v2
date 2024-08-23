# Django App Template

Django App

## Table of content

| Content | Description |
| :------ | :---------- |
| [1. Installation](#1_installation) | Steps for dependencies installation and other configurations |

## 1. Installation

### 1.1 Dependendencies installation
To install this project, it is recommended to use `virtualenv` python package. By default, macOS has installed `python3` binary. So the following commands should work:

Install virtualenv to create an environment for your python packages:
```
python3 -m pip install virtualenv
```
If pip is not installed follow the guide at https://pip.pypa.io/en/stable/installation/. Use get-pip.py code.

Create an environment:
```
python3 -m virtualenv -p python3 venv
```

Activate the environment:
```
source venv/bin/activate
```

Install python dependencies:
```
pip install -r dev-requirements.txt -r requirements.txt
```

Run tests (tests configuration is set in pytest.ini):
```
python -m pytest tests/
```

Run tests and get coverage:
```
coverage run -m pytest tests/ && coverage report -m
```

Check linting (linting configuration is set in .flake8):
```
flake8
```

Check more linting:
```
black -l 88 --preview .
```

```
isort --profile=black .
```

Check docstyle in the code (docstyle configuration is set in .pydocstyle):
```
pydocstyle
```

Check commits:
```
pre-commit install --hook-type commit-msg --hook-type pre-push
```

### 1.2. IDE Extensions

The following extensions for Visual Studio Code are recommended to improve your coding experience:

- For basic formatting of files, new lines, and indentation:
```
Name: EditorConfig for VS Code
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig
```

- For python linting and other utilities like formatting:
```
Name: Python
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python
```

- For generating automatically docstring in functions:
```
Name: autoDocstring - Python Docstring Generator
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
```
This tool is pretty useful if you have already set types for arguments and return variables of the function. After that only typing """ will trigger the extension.
