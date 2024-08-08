<img src="/pics/Docker.png">

## ▪️ Docker 🐋 

**Docker in a Nutshell:**

You first Build your Image, which is going to be just like an OS image containing the very basic and necessary components to run an app.
You Run your Image, and by doing so a Container gets created with your App Running.
You can then Stop and Start your container without the need to follow the Previous 2 Steps.
The Container is going to last even after you've stopped it.

Install Docker at [Docker Debian Installation Guide](https://docs.docker.com/engine/install/debian/), then verify your installation:

	> $ sudo docker run hello-world

Install Compose Plugin:

	> $ sudo apt-get install docker-compose-plugin

Super Basic Commands:

1.  The Dockerfile is used to build images while the docker-compose.yaml file is used to run images.

2.  The Dockerfile uses the `docker build` command, while the _docker-compose.yaml_ file uses the `docker-compose up` command.

3.  A docker-compose.yaml file can reference a Dockerfile, but a Dockerfile can’t reference a docker-compose file.

Build your Image from Dockerfile:

	> sudo docker build -t DOCKER_IMAGE_NAME .
	
The last dot is import as it's telling Docker where to look for the Dockerfile.

Build your Image from docker-compose.yaml:

	> $ sudo docker compose up -d		<--- Where the -d Flag allows you to let it run in the background (daemon)

List all Docker Images:

	> sudo docker images

List all Running Containers:

	> $ sudo docker ps

Use the -a Option to also show Stopped Containers.

Run a Docker Image:

	> $ sudo docker run -i -t DOCKER_IMAGE_NAME --name CUSTOM_CONTAINER_NAME

Where -i stands for interactive and -t stands for terminal, this way you'll see the terminal outputs and can interact with it.

Build a Docker Volume to Share Data Local-Container Consistently:

	> $ sudo docker volume create DOCKER_VOLUME_NAME

Then, to mount that volume:

 	> $ sudo docker run --name CONTAINER_NAME -d -i -t -v DOCKER_VOLUME_NAME:/container/folder/path DOCKER_IMAGE_NAME

In case you would like to have a local folder synched with a folder inside the container, to consistently share every change happens in either the Container or Locally in that folder:
 
 	> $ sudo docker run --name CONTAINER_NAME -d -i -t -v /host/folder/path:/container/folder/path DOCKER_IMAGE_NAME

With the above command any changes made to files within the local folder will be reflected to the container folder and vice-versa.
<br>
If you want to get the complete list of Docker Volumes:
	
	> $ sudo docker volume ls

Then, to inspect one:

	> $ sudo docker volume inspect DOCKER_VOLUME_NAME
	
Get the IP Address of a Container: 

	> $ sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' CONTAINER_ID_OR_NAME

Get the Logs for a given Container:

	> $ sudo docker logs RUNNING_DOCKER_CONTAINER_ID

Start a Stopped Docker Container:

	> $ sudo docker start STOPPED_DOCKER_CONTAINER_ID

Stop a Running Docker Container:

	> $ sudo docker stop RUNNING_DOCKER_CONTAINER_ID

Remove a Docker Container:

	> $ sudo docker rm DOCKER_CONTAINER_ID

Stop all Running Containers:

	> $ sudo docker stop $(sudo docker ps -a -q)

Remove all Stopped Containers:

	> $ sudo docker rm $(sudo docker ps -a)

Remove a Docker Image:

	> $ sudo docker rmi DOCKER_IMAGE_NAME_OR_ID --force

Enter into a Docker Image Terminal:

	> $ sudo docker exec -i -t RUNNING_DOCKER_CONTAINER_ID_OR_NAME /bin/bash

To connect as the Root, add the Flag -u to the docker exec command followed by the root user (-u root)

Make sure the container is running and get the container ID with docker ps, you can also use other commands by replacing /bin/bash with the command of your choice.

Compose a Multi-Container App:

	> $ sudo docker compose up

To then shut it down:

	> $ sudo docker compose down
	
Copy files from local to docker:Start
	
	> $ sudo docker cp <local_path_or_filename> <container_id_or_name>:<container_path>

Copy files from Docker to Local:

	> $ sudo docker cp <container_id_or_name>:<container_path> <local_path>

[Docker Docs](https://docs.docker.com/)

**EXTRA:**

In case you need docker to run without sudo permissions, but this process can be done for other services on linux too, follow these commands:

	> $ sudo groupadd docker
	> $ sudo usermod -aG docker yourusername

Then, check that Docker group has been added to your system:

	> $ groups yourusername

Lastly, Change Ownership of the Docker Socket and Modify Permissions of the Docker Socket:

	> $ sudo chmod 666 /var/run/docker.sock

To revert, the changes made:

	> $ sudo chmod 660 /var/run/docker.sock

Or, in case you changed ownership: 

	> $ sudo chown root:root /var/run/docker.sock

Then, Restart the Docker service ot make sure all changes are in place:

	> $ sudo chown root:root /var/run/docker.sock

*OPTIONAL:*

Say that you have docker compose files with custom name, for example TradeProducer.test.yml (or .yaml), to spin it up or down:

	> $ sudo docker compose -f /path/to/file/TradeProducer.test.yml up 	<--- or down instead of up.

If you have multiple docker composes that you would like to fire up or down, and they have different names:

	> $ sudo docker compose -f /path/to/file/TradeProducer.test.yml -f /path/to/file/TradeProducer.production.yml up

This will merge configurations with settings in the latter taking precedence.
