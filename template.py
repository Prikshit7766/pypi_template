import os 
from pathlib import Path # it makes your application os independent   (solves path issues)
import logging


logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')



while True:
    project_name = input("Enter project name: ") # input is a blocking function
    if project_name != "": # if project_name is not empty
        break


logging.info(f"Creating Project name: {project_name}")

# list of files 
list_of_files = [
    ".github/workflows/.gitkeep",   # dummpy file t does not do anything (used to keep your structure intact on github) 
   f"src/{project_name}/__init__.py",  # keeping my source code in src folder
   f"tests/__init__.py",
   f"tests/unit/__init__.py",
   f"tests/integration/__init__.py",
    "init_setup.sh", # this file will be used to install all the dependencies (that is conda env setup)
    "requirements.txt", 
    "requirements_dev.txt", # only used for testing (keeping main requirements.txt clean)
    "setup.py", # this file will be used to do the basic setup
    "pyproject.toml", 
    "setup.cfg",
    "tox.ini", # python pakages need to be tested on different environments
]

#https://packaging.python.org/en/latest/tutorials/packaging-projects/



for filepath in list_of_files:
    filepath=Path(filepath) 
    filedir,filename=os.path.split(filepath) # exampe src/project_name/__init__.py    so  --> filedir=src/project_name/ filename=__init__.py
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # if filedir does not exist create it
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    # some time we have to re-run this and if i re-run this it will erase all the files
    # so we have to check if file already exists or not   or if the file exists and is empty then also we have to create it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        logging.info(f"Creating file: {filepath}")
        with open(filepath, "w") as fp:
            pass
            logging.info(f"Created new file: {filename} at path: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
           