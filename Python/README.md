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
