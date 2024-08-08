TEMPORARY


Install Poetry (https://python-poetry.org/docs/#installing-with-the-official-installer)

On Debian: curl -sSL https://install.python-poetry.org | python3 -

then add Poetry to your path with nano ~/.bashrc and then source ~/.bashrc 
as soon as you install poetry it will also tell you which path to add to your .bashrc file, in general it looks like this:

/home/username/.local/bin

So, add to your .bashrc file:

export PATH="/home/username/.local/bin:$PATH"

The system will then automatically fetch the content of that folder, including the Poetry executable.

check Poetry version
poetry --version

to update poetry

poetry self update
poetry self update --preview
poetry self update VERSION

to uninstall Poetry:
curl -sSL https://install.python-poetry.org | python3 - --uninstall

to get you started, you have to create a new poetry project with:

mkdir newfolder
cd newfolder
poetry new newproject --name main		<--- Poetry will initialize a bunch of folders and files, the main folder can be named with the --name flag, usually named main or src

here's how the folder will then look like:

newfolder
└── newproject
    ├── pyproject.toml
    ├── README.md
    ├── main
    │   └── __init__.py
    └── tests
        └── __init__.py

then:
cd newproject
poetry install

The above install command, will read all dependencies in the pyproject.toml file, resolve them, create and package the virtual environment, as well as building the poetry.lock file that is basically a list of all the dependencies files downloaded compiled and locked for later usage.
You should commit the poetry.lock file to your project repo so that all people working on the project are locked to the same versions of dependencies.

if you want to install an already existing pyproject.toml file:

in case you already have the pyproject.toml file (from a repo, or from somewhere you are sharing code) BUT NOT the poetry.lock file:

simply pull or download the pyproject.toml and run poetry install in the folder (it will create the poetry.lock)

if you instead have both of them (best scenario when you want your dependencies to be locked inside a file to avoid unexpected break due to conflicts in dependencies):

when you run poetry install, it means either you ran the install command before, or someone else on the project ran the install command and committed the poetry.lock file to the project (which is good).

Either way, running install when a poetry.lock file is present resolves and installs all dependencies that you listed in pyproject.toml, but Poetry uses the exact versions listed in poetry.lock to ensure that the package versions are consistent for everyone working on your project. As a result you will have all dependencies requested by your pyproject.toml file, but they may not all be at the very latest available versions (some dependencies listed in the poetry.lock file may have released newer versions since the file was created). This is by design, it ensures that your project does not break because of unexpected changes in dependencies.

To add a package to the virtual environment, you can do it both manually by editing the pyproject.toml file(you'll have to reinstall and recreate the poetry.lock file):

[tool.poetry.dependencies]
pendulum = "^2.1"

or by using poetry add pendulum, and with poetry add the dependency is already installed in your virtual environment automatically.

to run a python script with your virtual environment:
poetry run file.py

to get info about the environment:

poetry env info

to remove a package
poetry remove packagename

to list all packages:
poetry show

 The check command validates the content of the pyproject.toml file and its consistency with the poetry.lock file. It returns a detailed report if there are any errors.
poetry check

to spin up an interactive shell within the virtual environment:

poetry shell

This will spawn a shell within the project’s virtual environment and activates it, if no virtual environment does exist, a new one will be created and activated, so make sure you are in the folder where the virtual environment is.
*NOTE:* 
The scope of commands like shell, show, add, run, etc... are where you're at with the terminal when launching them, make sure you're in the right folder.

to export the .lock file in other formats:

poetry export -f requirements.txt --output requirements.txt

*NOTE:*
If you would like to change the python version, you'd need to use poetry env use /full/path/to/python
If you have it on your PATH, use instead poetry env use python3.7

https://python-poetry.org/
https://python-poetry.org/docs/

MORE FLEXIBLE, LIGHTER AND SECURE THAN USING OTHER VENV MANAGER TOOLS









