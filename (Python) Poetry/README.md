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
poetry run python3 file.py

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

https://python-poetry.org/
https://python-poetry.org/docs/



MORE FLEXIBLE, LIGHTER AND SECURE THAN USING OTHER VENV MANAGER TOOLS









