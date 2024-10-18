## Creation of conda env

- conda create -n my_env python=3.9
- conda create -p /path/to/my_env python=3.9

This creates an environment named my_env in the /path/to/my_env directory.

### Key differences:

- -n specifies the environment name.
- -p specifies the path to create the environment.
  Choosing between the two:
- Use -n when you want to create an environment in the default location (usually conda/envs).
- Use -p when you want to specify a custom location for the environment.
  Additional notes:
- You can install additional packages when creating an environment using the -n or -p flag followed by package names.
- You can activate an environment using conda activate <environment_name>.
- You can list all environments using conda env list.

---

## If using vscode one need to install ipykernal

`conda install ipykernal`

- ipykernel: The Brain Behind Jupyter Notebooks
- ipykernel is the Python package that provides the IPython kernel for Jupyter. This kernel is the computational engine that executes the code in your Jupyter Notebook.

### It's responsible for:  

- Running Python code: When you execute a code cell, the ipykernel interprets and runs the code.
- Managing communication: It handles the interaction between the Jupyter Notebook interface and the Python interpreter.
- Providing features: ipykernel offers advanced features like tab completion, object introspection, and rich output formats.

---

## Different ways to create python environment:

### 1. venv

`python -m venv venv`

On Mac Use : `source venv/bin/activate`

On Windows use : `venv\Scripts\activate`

To deactivate :

`deactivate`

---

### 2. virtualenv

`pip install virtualenv`

`virtualenv -p python3 virtual_env`

`virtual_env\Scripts\activate`

To deactivate :

`deactivate`

---

### 3. Anaconda

`conda create -p /path/to/my_env python=3.9`

or

`conda create -n my_env python=3.11`

`conda activate my_env`

To deactivate :

`deactivate`

---

### Check the below article to resolve conda is not recognized issue if you face.

https://stackoverflow.com/questions/44515769/conda-is-not-recognized-as-internal-or-external-command

---
