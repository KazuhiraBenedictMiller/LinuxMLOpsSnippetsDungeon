## ▪️ Python Prerequisites ✅

🐍 Install Python, alongside pip and venv:

	> $ sudo apt update && sudo apt upgrade -y
	> $ sudo apt install python3
	> $ sudo apt install python3-pip -y
	> $ sudo apt install python3 python3-venv

🐍 To Create and Activate your Virtual Env:

	> $ python3 -m venv /path/to/virtual/environment

cd into the folder that has been created by venv /path/to/virtual/environment

  	> $ source /bin/activate

🐍 To eventually create an ipython Jupyter Kernel for a Jupyter global installation from a venv, type inside the venv (while activated):

	> $ pip install jupyter
	> $ ipython kernel install --user --name=kernelname

Then, to uninstall the kernel:
	
	> $ sudo jupyter kernelspec uninstall kernelname

**In Case of EXTERNALLY MANAGED ERRORS with Python3.11 for Debian12, enter the following command:**

	> $ sudo rm /usr/lib/python3.*/EXTERNALLY-MANAGED

To install a different python version and have it alongside the "main" one:

Download the desired Python version from the official website:

	> $ wget https://www.python.org/ftp/python/3.X.Y/Python-3.X.Y.tgz

Replace X.Y with the desired version numbers.

Extract the downloaded archive:

	> $ tar xzf Python-3.X.Y.tgz
	> $ cd Python-3.X.Y

Configure the build process:

	> $ ./configure --enable-optimizations

Compile Python:

	> $ make altinstall

The altinstall option prevents overwriting the default python binary.

Verify the installation:

	> $ python3.X -V

Replace X with the minor version number.

To create a custom alias for your newly installed Python version:
Add the following line to your ~/.bashrc or ~/.zshrc file:

	> $ alias pyX='python3.X'

	OR

	> $ alias pythonX='/usr/bin/python3.X'

Replace X with the desired alias name and adjust the version number accordingly.

Reload your shell configuration:

	> $ source ~/.bashrc  
