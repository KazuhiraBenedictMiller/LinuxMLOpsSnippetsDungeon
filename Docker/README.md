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
	
The last dot is import as it's telling Docker where to look for the Dockerfile and which folder to use as context.
If you want to change context, you can do so by adding the full path instead of the . like /path/to/directory to specify the context, or add a remote git repo url like git://github.com/user/repo.git

OR, if you have a custom named Dockerfile, like CustomName.Dockerfile, you can tell which file to use to build the Docker image.

	> $ docker build -t ImageName . -f CustomName.Dockerfile

Build your Image from docker-compose.yaml:

	> $ sudo docker compose up -d		<--- Where the -d Flag allows you to let it run in the background (daemon)

List all Docker Images:

	> sudo docker images

List all Running Containers:

	> $ sudo docker ps

Use the -a Flag to also show Stopped Containers.

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
<br>
Also, keep in mind, that using docker compose down, will detach and remove all volumes, networks and containers, if you need to stop them and then restart where you left off, use start and stop commands.

*OPTIONAL:*

.Dockerfile and docker-compose.yml configurations (Links to Docker Docs):

[Dockerfiles](https://docs.docker.com/reference/dockerfile/)
[Docker Compose](https://docs.docker.com/compose/)
[Docker Docs](https://docs.docker.com/)

*EXTRA:*

If you need to pass Build Time or Runtime Variables for your Dockerfile:

	ARG variable=value	<--- Build Time
	ENV variable=value	<--- Run Time

You can then access them as follows in the Dockerfile (this is an example):

	# Define a build-time variable
	ARG VERSION=latest

	# Use the ARG variable
	FROM ubuntu:$VERSION

	> $ docker build --build-arg VERSION=20.04 -t IMAGENAME .	<--- Passing Build Time Variable (ARG in Dockerfiles) 


For Environment Variables, instead:

	ENV environment=default_env_value
	ENV cluster=default_cluster_value

	CMD ["sh", "-c", "node server.js ${cluster} ${environment}"]	<--- Accessing them in the Dockerfile

	> $ docker run -p 9000:9000 -e environment=customvalue -e cluster=vustomvalue -d me/app		<--- Passing them as cli arguments (you can use --env flag instead of -e)

For Docker Compose:

In Docker Compose, you can set environment variables using the environment attribute or an external file with the env_file attribute.

	services:
	  web:
	    image: nginx:latest
	    environment:
	      - DEBUG=1
	    env_file:
	      - .env

.env FILE CONTENT:

	DEBUG=value	

To use environment variables within the docker-compose.yml file itself, such as for dynamic configuration, you can utilize variable substitution:

	services:
	  db:
	    image: "postgres:${POSTGRES_VERSION}"

Ensure the environment variable (POSTGRES_VERSION in this case) is exported in your shell or defined in an .env file located in the same directory as your docker-compose.yml, since docker compose automatically detects .env file.
Alternatively, if you need to pass a different .env file and spcify it, you can simply call the variables in your docker compose as follow and then pass the custom .env file via the cli:

	# .env file
	POSTGRES_VERSION=13
	DB_USER=mydbuser
	DB_PASS=mypassword

	version: '3'
	services:
	  db:
	    image: "postgres:${POSTGRES_VERSION}"
	    environment:
	      - POSTGRES_USER=${DB_USER}
	      - POSTGRES_PASSWORD=${DB_PASS}


	> $ docker compose --env-file .env up

OR, you can set up multiple .env files and pass them directly:
Let's say you have two environment files: .env.dev for development and .env.prod for production.

	# .env.dev
	POSTGRES_VERSION=13-dev
	DB_USER=mydbuser_dev
	DB_PASS=mypassword_dev

	# .env.prod
	POSTGRES_VERSION=13-prod
	DB_USER=mydbuser_prod
	DB_PASS=mypassword_prod

	You can specify which environment files to use by setting the COMPOSE_ENV_FILES environment variable. For example, to use the development environment file:

	export COMPOSE_ENV_FILES=".env.dev,.env.prod"
	docker compose up

This command tells Docker Compose to merge the variables from both .env.dev and .env.prod files, with later files overriding earlier ones if there are conflicts.

If you have a different path for your .env file:

	version: '3'
	services:
	  webapp:
	    env_file:
	      - /full/path/to/your/.env

This configuration tells Docker Compose to load the environment variables from the specified .env file located at /full/path/to/your/.env.

Using --env-file Flag
If you prefer to specify the environment file at runtime, you can use the --env-file flag with the docker compose command. This is particularly handy for one-off commands or when you need to override the default .env file.

	> $ docker compose --env-file /full/path/to/your/.env up

This command instructs Docker Compose to use the environment variables defined in the .env file located at /full/path/to/your/.env.

Using COMPOSE_ENV_FILES Environment Variable
For scenarios where you need to use multiple environment files, including those with full paths, you can set the COMPOSE_ENV_FILES environment variable. This variable accepts a comma-separated list of paths to .env files.

	> $ export COMPOSE_ENV_FILES="/full/path/to/first.env,/full/path/to/second.env"
	> $ docker compose up

Use the COMPOSE_ENV_FILES environment variable to specify multiple environment files, allowing for flexible configuration management across different environments or setups.

Passing Variables via CLI:

For Docker Compose, you can pass environment variables temporarily when running a service using the --env or -e option:

	> $ docker compose run -e DEBUG=1 web python console.py 	<--- THIS IS ONLY FOR A ONE OFF TASK, NOT THE ENTIRE LIFECYCLE

Alternatively, you can export environment variables in your shell before running Docker Compose commands, and these variables will be accessible within your docker-compose.yml file:

	> $ export POSTGRES_VERSION=14
	> $ docker-compose up -d

Or pass them directly when invoking Docker Compose:

	> $ POSTGRES_VERSION=14 docker-compose up -d

Use ARG and ENV in Dockerfiles for build-time and runtime variables.
In Docker Compose, use the environment attribute for inline environment variables and env_file for external files, since you cannot use the -e flag.
Utilize variable substitution in docker-compose.yml for dynamic configurations based on environment variables.
Pass environment variables temporarily with --env when running services or export/set them in the shell before running Docker Compose commands.
Remember, values present in the environment at runtime override those defined inside .env files, and command-line arguments take precedence over both.

*PASSING VARIABLES AT BUILD TIME DYNAMICALLY TO DOCKERFILES:*

To dynamically set environment variables in a Dockerfile at build time using values from an .env file, you cannot directly load the .env file within the Dockerfile itself. 
Docker does not support an --env-file option during the build process like it does with docker run. 
However, you can achieve a similar outcome by passing each variable individually as a build argument (ARG) and then converting it into an environment variable (ENV) within the Dockerfile.

To achieve that:

Step 1: Define Variables in Your .env File
Create an .env file with the variables you want to pass to the Docker build process:

	VERSION=1.2.0
	DATE=2022-05-10

Step 2: Export Variables and Build the Image
Before running the Docker build command, export the variables from your .env file in your shell session. Then, use the --build-arg flag to pass them to the Docker build command:

	> $ export $(cat .env | xargs)
	> $ docker build --build-arg VERSION=$VERSION --build-arg DATE=$DATE -t my-image .
	
This command exports all variables from the .env file into your shell environment and then passes them as build arguments to Docker.

OR, in case you have you have some of them and do not want to hardcode the docker build command, first ensure that variables in your .env file have the same name of the ones declared in your Dockerfile, and then:

Create a Bash Script to Automate all that:

	#!/bin/bash

	# Initialize an empty string to hold the build arguments
	build_args=""

	# Read the .env file line by line
	while IFS='=' read -r key value; do
	  # Append each variable as a --build-arg to the build_args string
	  build_args+="--build-arg $key=$value "
	done < .env

	# Execute the Docker build command with dynamically constructed build arguments
	docker build $build_args -t IMAGENAME .

Make sure to give execute permissions to your script:

	> $ chmod +x build.sh

Run Your Script to Build the Docker Image
Now, instead of manually running the Docker build command, you simply run your script:

	> $ ./build.sh

Step 3: Modify Your Dockerfile to Accept Build Arguments
Update your Dockerfile to accept these arguments and set them as environment variables:

	# Define build arguments
	ARG VERSION
	ARG DATE

	# Set them as environment variables
	ENV APP_VERSION=$VERSION
	ENV BUILD_DATE=$DATE

	# Rest of your Dockerfile...

In this Dockerfile, ARG is used to declare build-time variables, and ENV is used to set runtime environment variables inside the container. 
The values passed through --build-arg during the build process will be available as environment variables (APP_VERSION and BUILD_DATE) in the built image.

Summary
While Docker does not support loading an .env file directly during the build process, you can achieve dynamic variable setting at build time by exporting the variables from your .env file and passing them individually as build arguments using the --build-arg flag. 
This method allows you to parameterize your Docker builds effectively without hardcoding values in the Dockerfile.

[Docker Compose Environment Variables](https://docs.docker.com/compose/environment-variables/set-environment-variables/)

Remember that CMD and ENTRYPOINT are different, since:

ENTRYPOINT defines the base command that should always be executed when the container starts.
CMD provides default arguments that can be overridden by providing arguments at runtime.

Which means that ENTRYPOINT command parameters are immutable, while with CMD they are mutable when running the container.

ALSO, Remember that you can push images to dockerhub or pull them.