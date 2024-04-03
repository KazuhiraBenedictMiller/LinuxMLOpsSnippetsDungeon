## ▪️ Debian Empty Container for Isolated Development 🐧

Tired of all those Package Management Tools or just want to make local development a breeze?
<br>
I got ur back!  

Run an Ubuntu empty container, that runs in the background consistently and with a shared volume within the local host with:

	> $ sudo docker run --name ubuntu -i -t -d -v /local/path/to/folder:/container/path/to/folder ubuntu

By doing so, you just created a tiny virtual machine with minimal setting that you can use for local development.
Also, every change made to the folder shared (mounted with the volume  -v flag) will be reflected in both places, so, git init in the local folder, and develop/test/run your apps in Docker Container.

However, it's worth nothing that the Container is only a very minimal setup, and you'd need to literally install pretty much everything.

To connect to the Bash Terminal of your Container and start working on stuff:

	> $ sudo docker exec -i -t -u root ubuntu /bin/bash

**Did you know? 💡**

If you don't really like Ubuntu, most Linux distros have their own Docker Image, you can check them out and explore around here :

[DockerHub](https://hub.docker.com/)
[DockerLinuxDistros](https://hub.docker.com/search?q=linux)
  
If you also are developing in Python and want an Ubuntu Base Docker Image that once Built and Ran automatically runs a list of commands to setup your development environment, I also wrote out a Dockerfile for that:

**Docker Image:**
```docker
FROM ubuntu:latest

# Expose Jupyter Lab port
EXPOSE 8888

# Update package repositories and install necessary packages
RUN apt-get update -y && \
    apt-get install -y nano python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# OPTIONAL - Remove Externally Managed to install packages directly with pip if you're not going to run the Container Shell as root user - Uncomment if Necessary.
# RUN  rm /usr/lib/python3.*/EXTERNALLY-MANAGED

#Update and Upgrade Package Repositories (Sometimes you'd need to do it later when the Container is Running)
RUN apt update && apt upgrade -y

# Install IPython and create a kernel
RUN pip3 install ipython ipykernel jupyter elyra-python-editor-extension

# Start Jupyter Lab when the Container launches
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
```

Now, what does this Dockerfile do?
Simply put, it creates an Empty Ubuntu Docker Container, run some setups command, exposes the port 8888 (used for JupyterLab) and as soon as the Docker Image is ran, it starts a Jupyter Lab Server, that can be accessed by the localhost.

So, to put it to Work:

	> $ mkdir ubuntudockerdev
	> $ cd ubuntudockerdev

Then, Create the Dockerfile and copy paste the above code into it, then build the Image:

	> $ sudo docker build -t ubuntudockerdev .

You can use the -f flag to specify where the Image actually is if it's in a sub folder, for example:

	> $ sudo docker build -t ubuntudockerdev . -f /Path/To/Dockerfile.ubuntudockerdev

Run the Image and spin up a Container:

	> $ sudo docker run --name ubuntudev -p 8888:8888 -i -t -d -v ./:/localsynch ubuntudockerdev

This will spin up a Container with the Docker Image, bind the port 8888 (for Jupyter lab), start a Jupyter Server and attach a volume that will share the resources between Localhost and Container.
<br>
After that, you can simply open up a browser and type [localhost:8888](), press enter and start coding.
<br>
Need to install more packages or access the Ubuntu Container's terminal? No Problems:

	> $ sudo docker exec -i -t -u root ubuntudev /bin/bash
	> $ pip install WHATEVER_PACKAGE_YOU_WANT

Would you also like to publish to github all the content of the mounted volume on the folder?
<br>
Best way to do so it to simply git init on the folder, on localhost, but can also be done from within the Container, as long as you install git into it.
<br>
In case you need to stop the container, but get back on your jupyter lab later on running on the container, simply stop the container, turn off and on the pc later on, start the container again and exec the jupyter lab command:

	> $ sudo docker stop ubuntudev
	> $ sudo docker start ubuntudev
	> $ sudo docker exec -i -u root ubuntudev jupyter lab

	OR

	> $ sudo docker exec -i -t -u root ubuntudev /bin/bash
	> $ jupyter lab (inside the container's terminal)

**OPTIONAL:**

Need an empty Debian Container to use as Virtual Machine?
<br>
Here's the Docker Image (Dockerfile) to do that:

```docker
FROM debian:12.5

# Update package repositories and install necessary packages
RUN apt-get update -y && \
    apt-get install -y nano python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# OPTIONAL - Remove Externally Managed to install packages directly with pip if you're not going to run the Container Shell as root user - Uncomment if Necessary.
# RUN  rm /usr/lib/python3.*/EXTERNALLY-MANAGED

#Update and Upgrade Package Repositories (Sometimes you'd need to do it later when the Container is Running)
RUN apt update && apt upgrade -y
```

Then, to build and run it:

	> $ sudo docker build -t emptydebian .
	> $ sudo docker run --name emptydebian -i -t -d -v ./:/localsynch emptydebian





