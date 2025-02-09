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

	> $ alias pythonX='/usr/local/bin/python3.X'

Replace X with the desired alias name and adjust the version number accordingly.

Reload your shell configuration:

	> $ source ~/.bashrc  

To Export to PATH eventually:

	> $ export PATH=$PATH:/usr/local/bin

Note that When you use make altinstall, Python is typically installed in /usr/local/bin/pythonX.X instead of /usr/bin/python, where X.X is the version number.

You can also use the Full Path:

	> $ /usr/local/bin/python3.9 script.py


The core issue is that you're missing the necessary build tools, specifically a C compiler (like GCC).  You installed make, which is good, but configure needs a C compiler to generate the Makefiles that make uses.

Here's the corrected and more robust approach:

Install Build Essentials:
Bash

sudo apt update  # Update package lists
sudo apt install build-essential
This will install GCC, make, and other essential tools needed for compiling software.

Re-run Configure: It's crucial to re-run ./configure after installing the build tools. This is because configure checks for the presence of these tools and creates the appropriate Makefiles based on what it finds.
Bash

./configure --enable-optimizations
Check for Errors: Carefully examine the output of ./configure.  If there are any errors, address them before proceeding. The config.log file (which you mentioned) will contain detailed information about any issues encountered during configuration. Use cat config.log or less config.log to view it.  Common problems might be missing libraries or dependencies.

Make and Altinstall: Now that configure should have succeeded, you can compile and install Python.  It's highly recommended to use altinstall to avoid replacing your system's default Python:

Bash

make
sudo make altinstall
altinstall installs Python with a different name (like python3.13) and avoids overwriting the existing python3 command.  This prevents breaking system tools that rely on the older Python version.

Verify Installation:
Bash

python3.13 --version  # Check the installed version
which python3.13     # Find the installation path
(Optional) Create a Symbolic Link (if needed): If you want to use python313 (or some other short command) to refer to this version, create a symbolic link:
Bash

sudo ln -s /usr/local/bin/python3.13 /usr/local/bin/python313 # Example path, adjust if necessary
Key Improvements and Explanations:

build-essential: This package installs all the necessary tools in one go, including GCC, make, and other crucial components.
Re-running configure: This is the most critical step. You must re-run configure after installing build tools so that it can detect them and generate the correct Makefiles.
altinstall: This is strongly recommended to prevent breaking your system. It installs the new Python version alongside the existing one.
Checking config.log: This is essential for troubleshooting. If configure fails, the log file will tell you why.
Example Troubleshooting from config.log:

If config.log shows errors about missing libraries (e.g., zlib), you'll need to install them before re-running configure:

Bash

sudo apt install zlib1g-dev # Example for zlib, replace with the actual missing library
./configure --enable-optimizations  # Re-run configure
make
sudo make altinstall
By following these steps carefully and checking the config.log for any errors, you should be able to install Python 3.13 successfully. Remember to adapt the paths and library names to your specific system.


YOU CAN ALSO USE INSTALL IF YOU WANT TO OVERWRITE THE DEFAULT PYTHON INSTALLATION