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
poetry run python file.py

If for some reason you move the folder, you might need to rerun poetry install.

*A BRIEF NOTE ON POETRY RUN:*

Sometimes, if you name your main python file main.py and you only have modules inside the source folder, you can use poetry run main.py or poetry run main.py.
However, if you renamed the python file and there is no main.py, you main incur in some errors.
The poetry run command is designed to run a command in the virtual environment managed by Poetry. 
When you specify a Python file directly (like main.py), Poetry tries to find an executable named main.py in the system's PATH, which leads to the error if such an executable doesn't exist (Poetry only sets up the one for main.py).

Correct Usage of poetry run
To run a Python script located in your project directory, you should prefix the command with python to indicate that you're executing a Python script. For example:

poetry run python myscriptname.py

This tells Poetry to run the python main.py command inside the virtual environment, correctly interpreting main.py as a Python script rather than trying to execute it as a standalone command.

Specifying Script Location
If your script is located in a subdirectory, ensure you specify the path relative to the project root. For example, if main.py is inside a src directory, you would run:

poetry run python src/myscriptname.py

Check for Misconfigurations
Ensure there are no misconfigurations in your pyproject.toml file that might affect how scripts are executed. 
For instance, incorrectly defined scripts in the [tool.poetry.scripts] section could lead to unexpected behavior.


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
To Deactivate, "deactivate" within the spawned shell env

*NOTE:* 
The scope of commands like shell, show, add, run, etc... are where you're at with the terminal when launching them, make sure you're in the right folder.
Also, you can run commands inside the shell like within a normal terminal, such as python3 main.py

to export the .lock file in other formats:

poetry export -f requirements.txt --output requirements.txt

*NOTE:*
If you would like to change the python version, you'd need to use poetry env use /full/path/to/python
If you have it on your PATH, use instead (for example) poetry env use python3.7

*WALKTHROUGH EXAMPLE ON HOW TO CHANGE PYTHON VERSION FOR POETRY VIRTUAL ENVIRONMENT:*

First of all, Ensure your system has the necessary packages required to build Python's Binaries:
	> $ sudo apt update
	> $ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev

Then, Download the desired Python Version at https://www.python.org/downloads/ in our example, we'll test Python 3.9.1 (Download on Debian Linux the Gzipped Source Tarball)
You can directly download the Desired Python Version Manually with the above link or with the Command line as Follows:

	> $ cd WhereYouWantPythonToBeDownloaded (Usually /home/USERNAME/Downloads
	> $ wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tar.xz 	<--- (You can also use curl -O eventually instead of wget, and replace 3.9.1 with your Desired Version)

Extract the Files in the Source Tarball somewhere, usually on the same folder, but i like to put them on Desktop Sometimes:

	> $ tar -xzvf Python-3.9.1.tar.xz -C /Path/To/Destination	<--- You can avoid -C and the Destination Path if you want them in the same folder as the Tarball
	
Now, cd in the Extracted Files' Folder and Run the Configuration Script that will create the Makefile to install our Specific Python Version:
	
	> $ cd Python-3.9.1		<--- or cd /Path/To/Destination/Python-3.9.1 in case you used the -C flag
	> $ ./configure --enable-optimizations

Now, we need to find the number of cores our processor has, and insert them manually in the makefile arguments or automatically with a scripting trick.

	> $ nproc
	> $ make -j x	<--- x is the number of processors returned by nproc OR simply use make -j $(nproc)

Once the build is done, install the Python binaries by running the following command as a user with sudo access (whilist still in the folder):

	> $ sudo make altinstall

Do not use the standard make install as it will overwrite the default system python3 binary, so in case you already have a system-wide Python Version you want to keep and just play around with a different one, you should always use altinstall.

At this point, Python 3.9.1 is installed on your Debian system and ready to be used, You can verify it by typing:

	> $ python3.9 --version

If you want to list all the Different Python Versions on your system and see their paths, I found that the best way is to play around and tweak the ls command:

	> $ ls -l /usr/bin/python* /usr/local/bin/python*

In case you would like to use specific aliases for different Python Versions, to better remember their names, you have 2 possible solutions:

*METHOD 1 - EASY-GOING SOLUTION FOR NON-NECKBEARDS:*

Simply create a symbolic link with the Python Version Path you have identified in the /usr/local/bin folder (and eventually remove it later if not in need anymore):

	> $ sudo ln -s /usr/bin/python3.11 /usr/local/bin/CustomLinkName

Then Check if it worked with:
	
	> $ CustomLinkName --version

To delete the Custom Link:

	> $ sudo rm /usr/local/bin/CustomLinkName

If you try again the CustomLinkName --version command, or simply CustomLinkedName (which should launch the Python Executable linked to the Custom Link in the shell), it should output as follows, so you can make sure the Custom Link has been eliminted:

	bash: /usr/local/bin/CustomLinkName: No such file or directory

*METHOD 2 - FOR LINUX ENTHUSIASTS:*

Edit your .bashrc file with the alias pointing to the Newer Installed Alternative Python Version:

	> $ nano ~/.bashrc

Then, add the following alias and reload the .bashrc file or restart the terminal:

	> $ alias mycustompythonalias='/usr/bin/python3.11'
	> $ nano ~/.bashrc

Finally test the alias in your terminal:

	> $ mycustompythonalias --version

To delete the Alias, you'd have to remove it from the .bashrc file and reload it or restart the terminal.

*METHOD 3 - IN CASE OF LINUX NERD BREAK GLASS:*

Some people like to store their aliases separated by a newline in a .aliasesrc file with same path as the .bashrc and then source them in the bashrc file in case the aliasesrc file does exist with a scripting trick, as follows:
NOTE: I really like this approach in case you are intensively working on a Linux Machine, as this also leverages Linux's Files only type of OS.

Create the ~/.aliases file and populate it with each line representing a new alias:

	> $ touch ~/.aliasesrc
	> $ sudo echo "alias mycustomalias='/usr/bin/python3.11'" >> ~/.aliasesrc		<---  Replace '/usr/bin/python3.11' with '/usr/local/bin/python3.9' for our example
	
	YOU CAN USE THE COMMAND ABOVE AS MUCH AS YOU WANT FOR EACH OF YOUR ALIASES, IT WILL AUTOMATICALLY ADD A NEWLINE AS SEPARATOR

Then, in your ~/.bashrc file add the following lines:

	if [ -f ~/.aliasesrc ]; then
   	   . ~/.aliasesrc
	fi

Then reload the bashrc file and the alias is working:

	> $ source ~/.bashrc
	> $ mycustomalias --version

Lastly, simply updating your aliasesrc file will eventually reflect all aliases when reloading the terminal or resourcing the bashrc file.

*MOVING ON WITH CHANGING POETRY ENVIRONMENT:*

Let's now create a new Poetry Env and use our Python3.9.1 Version as the Python Version for the Virtual Environment (aliased as mycustomalias=/usr/local/bin/python3.9):

	> $ mkdir testpoetryenv
	> $ cd testpoetryenv
	> $ poetry new test
	> $ poetry env use python3.9 		<--- OR poetry env use /full/path/to/python3.9
	> $ poetry install

*NOTE:*
Make sure the Python Version Required in the pyproject.toml file are loose enough for your version:

	[tool.poetry.dependencies]
	python = "^3.11"	<--- Change this to suit your needs under the tool.poetry.dependencies section of your pyproject.toml file, BEFORE running poetry install

*EXTRA:*
If for some reason, you need the python executable of your Poetry Virtual Environment to change interpreter on your code editor (VS Codium/VS Code for example), run (whilist on the folder where your Potery Env is located):

	> $ poetry env info

It should return something like this:

	Virtualenv
	Python:         3.11.2
	Implementation: CPython
	Path:           /home/nomad/.cache/pypoetry/virtualenvs/source-XEL_2frX-py3.11
	Executable:     /home/nomad/.cache/pypoetry/virtualenvs/source-XEL_2frX-py3.11/bin/python	<--- This is the Path to your Poetry Virtual Enviroment Executable that you'd need to use to change interpreter on your code editor
	Valid:          True

	Base
	Platform:   linux
	OS:         posix
	Python:     3.11.2
	Path:       /usr
	Executable: /usr/bin/python3.11

In case your pyptoject.toml changes significantly since when it got installed and locked the last time, you can fix it by not forcing the lock to not update and then reinstall the venv, as follows:

	> $ poetry lock --no-update
	> $ poetry install

This usually happens if you changes a lot of dependencies specifications in the pyproject.toml file due to a conflict before installing some desired packages.

As a Matter of fact, the lock command locks (without installing) the dependencies specified in pyproject.toml.

By default, this will lock all dependencies to the latest available compatible versions. 
To only refresh the lock file, use the --no-update option. 
This command is also available as a pre-commit hook. 
See pre-commit hooks for more information.

poetry lock
Options
--check: Verify that poetry.lock is consistent with pyproject.toml. (Deprecated) Use poetry check --lock instead.
--no-update: Do not update locked versions, only refresh lock file.

https://python-poetry.org/
https://python-poetry.org/docs/

*DEPENDENCY HELL TIP:*

For some reasons, poetry might work on your local machine, but when building the Docker Image and running poetry install, you might end up with poetry being able to install your project locally but then running into problems when building the image with docker (and failing to do so).
Here's an example of an error:

	20.59 Note: This error originates from the build backend, and is likely not a problem with poetry but with twofish (0.3.0) not supporting PEP 517 builds. You can verify this by running 'pip wheel --no-cache-dir --use-pep517 "twofish (==0.3.0)"'.
	20.59 

First thing first, if the Poetry venv is working fine on your local machine, assuming you can run programs locally with poetry run python myapp.py, cd in the directory where the venv is located and spawn a shell within there:

	> $ cd myprojectfolder
	> $ poetry shell

Then, copy paste the command inside the shell spawned and see if within the poetry venv, you can build the wheel for the desired package, in our example:

	 > $ pip wheel --no-cache-dir --use-pep517 "twofish (==0.3.0)"

CASE A:

If the error still persists, you can try some options to try to fix it:

OPTION 1:

Try running the following command, since you're maybe missing some dependencies in your linux distro in the shell spawned within the poetry venv:

	apt-get update && apt-get install -y --no-install-recommends \
    	build-essential \
    	libssl-dev \
    	python3-dev \
    	&& rm -rf /var/lib/apt/lists/*

OPTION 2:

If the Previous option didn't fix the problem, try to loosen the dependency requirement for the package or use an updated version, by modifying dependencies in your pyproject.toml.

CASE B:

If the error doesn't persist and you see this kind of output after running the pip wheel command within the spawned shell:

	Collecting twofish==0.3.0
	   Downloading twofish-0.3.0.tar.gz (26 kB)
	   Installing build dependencies ... done
	   Getting requirements to build wheel ... done
	   Preparing metadata (pyproject.toml) ... done
	Building wheels for collected packages: twofish
	   Building wheel for twofish (pyproject.toml) ... done
	   Created wheel for twofish: filename=twofish-0.3.0-cp311-cp311-linux_x86_64.whl size=25034 sha256=44aa0a2dd858617a62e416a4979fe0b6f22f4221860dfaed2f2f7cca938d4b19
	   Stored in directory: /tmp/pip-ephem-wheel-cache-cprxrxe9/wheels/4f/0b/b1/d97875c8e719f4a31f39c3ea718798318be32cf0068b042351
	Successfully built twofish

Then, this means that the problem is only within the Docker container when trying to build the image.

Here are some possible solutions:

OPTION 1:

You can trying some workaround using a different base image, I don't like this approach, but it might work.
You may also consider using a complete and not a slim base image, for example.

OPTION 2:

Add this command to your Dockerfile before Running pip install poetry:

	RUN apt-get update && apt-get install -y --no-install-recommends \
    		build-essential \
    		libssl-dev \
    		python3-dev \
    		&& rm -rf /var/lib/apt/lists/*

	RUN pip install poetry

This should do the Work, but there is a MASSIVE DRAWBACK, your image is going to be incredibly heavy.

OPTION 3:

You can Build the wheels locally, and then import them within your docker container and build them there.
There are some ways to achieve this:

CASE 1) 
First export the requirements.txt file with poetry export, then spawn a shell within the poetry vevn and build the wheels there:

	> $ cd myprojectfolder
	> $ poetry export
	> $ poetry shell
	> $ pip wheel --no-cache-dir --use-pep517 --wheel-dir=./wheels -r requirements.txt	<--- in our example we are using PEP517 as its the version we care about

Now you should see a wheels directory full of built wheels for your project.
We now need to copy them into the docker image and install them there.
Here's what your docker file will look like:
	
	...

	RUN pip install poetry==1.8.3

	WORKDIR /app

	COPY pyproject.toml poetry.lock /app/

	COPY ./wheels /app

	RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

	RUN poetry add --no-interaction --no-root ./wheels/*.whl \		<--- Command used to add custom build from path or url to poetry venv.
	    && rm -rf wheels/*.whl

	COPY . /app

	RUN poetry install --without dev

	ENTRYPOINT ["poetry", "run", "python", "myapp.py"]

CASE 2)
You can also use a multi-stage dockerfile for this:

	# Stage 1: Prepare the environment and install Poetry
	FROM python:3.9 AS builder

	WORKDIR /app

	RUN pip install --no-cache-dir --upgrade pip \
	 && pip install --no-cache-dir poetry

	COPY . .

	# Assuming your wheel files are in a directory named "wheels"
	COPY ./wheels/*.whl .

	RUN poetry add --no-interaction --no-root *.whl \
	    && rm -rf wheels/*.whl

	# Stage 2: Set up the final image
	FROM python:3.9

	ENV PYTHONUNBUFFERED=1

	WORKDIR /app

	# Copy the virtual environment from the builder stage
	COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

	CMD ["python", "-m", "your_module"]

OPTION 4:

My favourite approach, using a multi-stage docker with the Builder Image fully equipped.
This way we can leverage a Complete Builder Image while still preserving the lightweight of the runtime image.
In this specific case, the size of the Docker Image went from 1.15 GB (OPTION 2) to 831 MB (Hopsworks is such an heavy package!) 

Here's what the .Dockerfile will look like:

#Complete Heavy Builder Image to Actually Build the Virtual Env with Complete Docker Image
FROM python:3.11-bookworm as Builder

#Setting Deterministic Environment Variables
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

#Installing Specific Poetry Version
RUN pip install poetry==1.8.3

WORKDIR /app

#Copying Only Necessary Files
COPY pyproject.toml poetry.lock ./

#Adding README or Poetry will complain
RUN touch README.md

#Installing only the Virtual Environment with Dependencies and not the Project, then Removing Cache
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

#Slim Runtime Docker Image, used to just run the code provided its Virtual Environment Built and Passed by the Builder Image
#Here, we don't even need Poetry installed, so we are passing the Virtual Environment, Installing the Project (Optional) and then Removing Poetry
FROM python:3.11-slim-bookworm as Runtime

#Setting up the Venv Location and adding it to PATH
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"		

#Copying the Venv from Builder Image at VIRTUAL_ENV Location to Runtime Image at VIRTUAL_ENV Location
COPY --from=Builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

#Copying Poetry files to actually Install the Project
COPY pyproject.toml poetry.lock /app/

#We don't need Poetry in runtime image, but might be worth it to reinstall it as we built the Virtual Env in our Builder Image, passed only the Venv Specs and Files to our Runtime
#However, if you need to Install Specific Script or anything Like that, you'll want to make sure you are installing the Project in the Runtime Image.
RUN pip install poetry==1.8.3 && cd /app && poetry install --no-cache --without dev && pip uninstall poetry -y

#Copying Actual Codebase
COPY ./source /app

ENTRYPOINT ["python", "source/KafkaToFSQuixStreamsApp.py"]


TO USE JUPYTER WITH POETRY AND DEFAULT POETRY ENV AS KERNEL:

	> $ poetry add jupyterlab
	> $ poetry run jupyter lab --ip=0.0.0.0 --port=8899 --allow-root --NotebookApp.token='' --NotebookApp.password='' --no-browser

Then open your browser and go to locahost:8899

OR, if you would like to install your poetry env to a system wide jupyter installation:
	
	> $ poetry add jupyterlab
	> $ poetry run python -m ipykernel install --user --name=KERNEL_NAME
	> $ jupyter lab command

OR, another kernel, within the same jupyter installation within poetry:

	> $ poetry add jupyterlab
	> $ poetry run python -m ipykernel install --name=KERNEL_NAME
	> $ poetry run jupyter lab command

If you would like to permanently delete a poetry env, cd into the directory where the venv is located and:

	> $ cd Path/To/PoetryVenv
	> $ poetry env list	<--- grab the venv name such as pyexamsvenv-w-zx_hGQ-py3.11 (Activated)
	> $ poetry env remove VENV_NAME

Then Remove the Dir with all the files.

ANOTHER GUIDE:

1. First, deactivate and delete any virtual environments created with Poetry, using the poetry env remove command followed by the corresponding Python version OR VENV_NAME. 
“`bash $ poetry env remove python3.8 “` 
2. Next, locate the Poetry installation script, which is usually stored in your home directory under the .local/bin folder. If you installed it with a different method or location, find the appropriate directory. 
3. Remove the poetry executable file from the installation directory. “`bash $ rm ~/.local/bin/poetry “` 
4. Optional: If you would like to completely clean up the Poetry configuration and cache files from your system, delete the following directories as well: “`bash $ rm -r ~/.config/poetry $ rm -r ~/.cache/pypoetry “` 
By following these simple steps, you can achieve an effortless uninstallation of Python Poetry from your system, ensuring a clean environment for your future projects.

Read more here: https://locall.host/python-uninstall-poetry/

Say that you want to use a different python version than your default one in the system for poetry, but for some reason you are forced to use the default one:  
  
you can store the AltPyPoetryNew function in a separate file and then load it within your .bashrc. This approach helps keep your .bashrc organized and makes it easier to manage custom functions. Here's how you can set this up:

    Create a Directory for Custom Scripts:

    It's a good practice to store your custom scripts in a dedicated directory. For example, create a .bash.d directory in your home folder:

mkdir -p ~/.bash.d

Create the Function File:

Inside the .bash.d directory, create a file to hold your AltPyPoetryNew function. Let's name it alt_py_poetry_new.sh:

nano ~/.bash.d/alt_py_poetry_new.sh

Add the following content to this file:

#!/bin/bash

function AltPyPoetryNew() {
    while [[ "$#" -gt 0 ]]; do
        case $1 in
            --projectname) project_name="$2"; shift ;;
            --pyalias) py_alias="$2"; shift ;;
            *) echo "Unknown parameter passed: $1"; return 1 ;;
        esac
        shift
    done

    if [[ -z "$project_name" || -z "$py_alias" ]]; then
        echo "Usage: AltPyPoetryNew --projectname <name> --pyalias <python_alias>"
        return 1
    fi

    # Create the new project
    poetry new "$project_name" --name src

    # Navigate into the project directory
    cd "$project_name" || return 1

    # Set the specified Python interpreter for the project
    poetry env use "$(which "$py_alias")"
}

Save and close the file.

Make the Script Executable:

Ensure the script has executable permissions:

chmod +x ~/.bash.d/alt_py_poetry_new.sh

Modify Your .bashrc to Source the Function:

Edit your .bashrc file to source the alt_py_poetry_new.sh script during shell initialization:

nano ~/.bashrc

Add the following line at the end of the file:

# Load custom functions
if [ -f ~/.bash.d/alt_py_poetry_new.sh ]; then
    source ~/.bash.d/alt_py_poetry_new.sh
fi

This snippet checks if the alt_py_poetry_new.sh file exists and sources it, making the AltPyPoetryNew function available in your shell sessions.

Reload Your .bashrc:

Apply the changes by reloading your .bashrc:

    source ~/.bashrc

Using the AltPyPoetryNew Function:

After completing these steps, you can use the AltPyPoetryNew function as follows:

AltPyPoetryNew --projectname miao --pyalias python311

This command will create a new Poetry project named miao with the internal package name src and configure it to use the Python interpreter associated with the alias python311.

Alternative Approach:

If you have multiple custom functions or scripts, you can source all scripts in the ~/.bash.d directory by adding the following to your .bashrc:

# Source all scripts in ~/.bash.d
if [ -d ~/.bash.d ]; then
    for script in ~/.bash.d/*.sh; do
        [ -r "$script" ] && source "$script"
    done
    unset script
fi

This loop will source all .sh files in the ~/.bash.d directory, making any functions or aliases defined in those scripts available in your shell sessions.

By organizing your custom functions in separate files and sourcing them in your .bashrc, you maintain a cleaner and more manageable configuration, facilitating easier updates and maintenance.



MORE FLEXIBLE, LIGHTER AND SECURE THAN USING OTHER VENV MANAGER TOOLS











