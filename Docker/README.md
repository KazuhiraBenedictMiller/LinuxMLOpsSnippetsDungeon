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
Like as follows:

	> $ docker build -t myimage:tag -f /path/to/Dockerfile /path/to/context
OR
	> $ docker build -t myimage:tag git://github.com/user/repo.git#branchname 	<--- or with HTTPS https://github.com/user/repo.git#branchname

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

*MIND THAT:*
The difference between -d -it and -d -i -t in Docker commands, such as docker run, lies in the interaction and terminal allocation behavior of the container.

-d: Runs the container in detached mode, meaning it runs in the background and does not receive input or display output in the terminal.
-i: Keeps STDIN open even if not attached. This is useful for interactive applications that require user input.
-t: Allocates a pseudo-TTY, simulating a real terminal. This is often used in conjunction with -i to allow interactive shell access to the container.

-d -it
When you combine -d with -it, you're telling Docker to run the container in the background (-d) and allocate a TTY (-t), along with keeping STDIN open (-i). 
This combination is commonly used for interactive applications that you want to run in the background but still interact with via the terminal.

-d -i -t
On the other hand, -d -i -t is not a standard combination for Docker commands. 
Typically, -i and -t are used together (-it) to enable interactive terminal sessions. 
Separating them (-i -t) would imply trying to keep STDIN open and allocate a TTY separately, which is not the usual practice and might not behave as expected.

Build a Docker Volume to Share Data Local-Container Consistently:

	> $ sudo docker volume create DOCKER_VOLUME_NAME

Remember that docker volumes are meant to abstract away the specifics of the host filesystem for better portability and management. 
If you need to work with specific host directories, using the -v flag to mount them directly into the container is the recommended approach.

Then, to mount that volume:

 	> $ sudo docker run --name CONTAINER_NAME -d -it -v DOCKER_VOLUME_NAME:/container/folder/path DOCKER_IMAGE_NAME

In case you would like to have a local folder synched with a folder inside the container, to consistently share every change happens in either the Container or Locally in that folder:
 
 	> $ sudo docker run --name CONTAINER_NAME -d -it -v /host/folder/path:/container/folder/path DOCKER_IMAGE_NAME

With the above command any changes made to files within the local folder will be reflected to the container folder and vice-versa.

Keep in mind that named volume created or removed (docker volume create/rm) will persist as volumes after the container is removed.
On the other hand, if you create a volume as a folder, attaching it to a container with the -v flag as -v /host/folder/path, it will persist as a folder, and you'll have to manually delete it.
Also, the folder in that case will NOT be created automatically when running the container for the first time, so make sure to mkdir /host/folder/path first.

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

The --force flag is used when a container is spinned up using that image.

Enter into a Docker Image Terminal:

	> $ sudo docker exec -i -t RUNNING_DOCKER_CONTAINER_ID_OR_NAME /bin/bash

To connect as the Root, add the Flag -u to the docker exec command followed by the root user (-u root)

Make sure the container is running and get the container ID with docker ps, you can also use other commands by replacing /bin/bash with the command of your choice.

Compose a Multi-Container App:

	> $ sudo docker compose up -d

With the -d flag meaning it's detached.

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

	> $ sudo docker compose -f /path/to/file/TradeProducer.test.yml up -d	<--- or down instead of up.

If you have multiple docker composes that you would like to fire up or down, and they have different names:

	> $ sudo docker compose -f /path/to/file/TradeProducer.test.yml -f /path/to/file/TradeProducer.production.yml up -d

This will merge configurations with settings in the latter taking precedence.
<br>
Also, keep in mind, that using docker compose down, will detach and remove all volumes, networks and containers, if you need to stop them and then restart where you left off, use start and stop commands.

*OPTIONAL:*

.Dockerfile and docker-compose.yml configurations (Links to Docker Docs):

[Dockerfiles](https://docs.docker.com/reference/dockerfile/)
[Docker Compose](https://docs.docker.com/compose/)
[Docker Docs](https://docs.docker.com/)

*EXTRA:*

To Pass env variables in dockerfiles:
	add flag --env-file /path/to/env/.env to docker run

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
	      - path/to/.env

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
Also, ENTRYPOINT command are executed everytime the container STARTS, both when run and start with docker start (after being stopped) and docker run commands.
On the other hand, CMD commands are only executed when the container is run for the first time, so if you stop and start it again, you'll have to get a terminal inside the container and restart the command.

*dockerignore:*

Docker supports the .dockerignore file that has the same syntax as a .gitignore and exclude files from the build context, so if you want to copy all files for example, with an exception for a single file, simply add the file name or file path to the .dockerignore and it will be excluded from the build context.

REMEMBER: 

The .dockerignore file should be in the same directory as the Dockerfile or in a parent directory of the Dockerfile relative to the build context, since the .dockerignore file's scope is tied to the build context, it must be in the same directory as the Dockerfile that uses it.

ALSO, Remember that you can push images to dockerhub or pull them.

In case you have some containers that need to connect to a localhost, hosted on a another container (for example, redpanda docker compose with network and microservices containerized on their own) you can connect to a given network by naming it in the docker-compose.yml file and then by passing it as argument in the docker run:

	> $ docker run --network NETWORKNAMEOFHOSTCONTAINER -d -it IMAGENAME --name CONTAINERNAME

Remember, that when connecting locally to the host container, you can put the external port exposed by the redpanda dockercompose containers, but if you're running them in the same network with containerized applications, you'd need to expose the internal port.
Also, you'd need to change the host name (or IP Address) to localhost to the service name hosting the network, for example:

	#External Port for Local Dev
        kafka_broker_address = "localhost:19092",
        #Internal Port for Containerized Production on same Docker Network
        kafka_broker_address = "redpanda-0:9092",

Where in the docker-compose it looks like this:

	name: redpanda
	networks:
	  redpanda_network:
	    name: redpanda-network
	    driver: bridge
	volumes:
	  redpanda-0: null
	services:
	  redpanda-0:
	    container_name: redpanda-message-broker
	    command:
		... rest of docker-compose

To see help for docker, use docker --help or docker COMMAND --help and you'll be good (also refer to the docs and ask an LLM/Google) (Just like with any other software though)

Remember that most flags in docker, such as --env --network --volume, can be used with both the equal sign "=" or a space " " before the correspective values.
This principle applies to most software, but it's most common to see it used in docker cli when passing arguments because of the length of the command, to have better clarity.

An interesting article on how to make Dockerfiles (Docker Images) Impressively smaller:
https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0

Here's the summary on how to make Docker Builds smaller for Python (with Poetry) based Images:

1) Warm Up
First thing first, make sure you're only copying Data that you actually need inside your container and use the --without dev flag when installing the Poetry Environment in your Dockerfile, like so:

	RUN poetry install --without dev

So, in case you are adding Packages in the dev group (usually linters and formatters) those won't be added:

	> $ poetry add --group dev PackageName

2) Cleaning Poetry cache 
Poetry also supports a --no-cache option, so why am I not using it? We’ll see it later.
Then add some ENV values for Poetry to further strengthen the determinism of the build:

	ENV POETRY_NO_INTERACTION=1 \
	    POETRY_VIRTUALENVS_IN_PROJECT=1 \
	    POETRY_VIRTUALENVS_CREATE=1 \
	    POETRY_CACHE_DIR=/tmp/poetry_cache

Now, in the SAME command as Poetry install, we also delete the Cache Directory.
If it’s done in a separate RUN command the cache will still be part of the previous Docker layer (the one containing poetry install ), effectively rendering your optimization useless.

	RUN poetry install --without dev && rm -rf $POETRY_CACHE_DIR

3) Install the Dependencies before actually copying the code and data into the container:
Every time we modify our code we’ll have to re-install our dependencies! 
That’s because we COPY our code (which is needed by Poetry to install the project) before the RUN poetry install instruction. 
Because of how Docker layer caching works, every time the COPY layer is invalidated we’ll also rebuild the successive ones.
The solution here is to provide Poetry with the minimal information needed to build the virtual environment and only later COPY our codebase. 
We can achieve this with the --no-root option, which instructs Poetry to avoid installing the current project into the virtual environment.

	FROM python:TAG		<--- Make sure the Base Image is a Slim one

	RUN pip install poetry==VERSION		<--- Make sure you have same Poetry Version as your Local Development Machine (Reproducibility!!)

	ENV POETRY_NO_INTERACTION=1 \
	    POETRY_VIRTUALENVS_IN_PROJECT=1 \
	    POETRY_VIRTUALENVS_CREATE=1 \
	    POETRY_CACHE_DIR=/tmp/poetry_cache

	WORKDIR /app

	COPY pyproject.toml poetry.lock ./	<--- Copy Base Poetry Environment Files
	RUN touch README.md	<--- Or Poetry will complain

	RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR		<--- First Installation of Poetry Env

	COPY Data ./Data

	RUN poetry install --without dev	<--- Actually wise and fast to Install the Project in the Virtual Environment one more time

	ENTRYPOINT ["poetry", "run", "python", "Path/To/PythonFile.py"]

You can now try to modify the application code, and you’ll see that just the last 3 layers will be re-computed.

The additional RUN poetry install --without dev instruction is needed to install your project in the virtual environment. 
This can be useful for example for installing any custom script. 
Depending on your project you may not even need this step. 
Anyways, this layer execution will be super fast since the project dependencies have already been installed.

4) Using Docker multi-stage builds:
Up to now builds are fast, but we still end up with big Docker images. 
We can win this fight by calling multi-stage builds into the game. 
The optimization is achieved by using the right base image for the right job:

Python buster is a big image that comes with development dependencies, and we will use it to install a virtual environment.
Python slim-busteris a smaller image that comes with the minimal dependencies to just run Python, and we will use it to run our application.
Thanks to multi-stage builds we can pass information from one stage to the other, in particular the virtual environment being built. 
Notice how:
Poetry isn’t even installed in the runtime stage. 
Poetry is in fact an unnecessary dependency for running your Python application once your virtual environment is built. 
We just need to play with environment variables (such as the VIRTUAL_ENV variable) to let Python recognize the right virtual environment.
For simplicity I removed the second installation step (RUN poetry install --without dev ) as I don’t need it for my toy project, although one could still add it in the runtime image in a single instruction: 

	RUN pip install poetry && poetry install --without dev && pip uninstall poetry

Once Dockerfiles get more complex I also suggest using Buildkit, the new build backend plugged into the Docker CLI. 
If you are looking for fast and secure builds, that’s the tool to use. [Buildkit](https://docs.docker.com/build/buildkit/)
	
	#Set DOCKER_BUILDKIT=1 environment variable as 1 to use Buildkit
	> $ DOCKER_BUILDKIT=1 docker build --target=runtime .

	#The builder image, used to build the virtual environment
	FROM python:3.11-buster as builder 	<--- Complete Heavy Image

	RUN pip install poetry==VERSION

	ENV POETRY_NO_INTERACTION=1 \
	    POETRY_VIRTUALENVS_IN_PROJECT=1 \
	    POETRY_VIRTUALENVS_CREATE=1 \
	    POETRY_CACHE_DIR=/tmp/poetry_cache

	WORKDIR /app

	COPY pyproject.toml poetry.lock ./	<--- Copying only Necessary Files
	RUN touch README.md	<--- Or Poetry will complain

	RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR		<--- Installing only the Virtual Environment Dependencies and Removing Cache

	#The runtime image, used to just run the code provided its virtual environment (Passed by the Builder Image)
	FROM python:3.11-slim-buster as runtime

	ENV VIRTUAL_ENV=/app/.venv \
	    PATH="/app/.venv/bin:$PATH"		<--- Setting up the Venv and adding it to PATH

	COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

	#Optional, we don't need Poetry in runtime image, but might be worth it (Eventually simply avoid Uninstalling Poetry) (we build the Virtual Env in our Builder Image, passed only the Venv Specs to our Runtime)
	RUN pip install poetry && poetry install --without dev && pip uninstall poetry

	COPY Data ./Data

	ENTRYPOINT ["python", "Path/To/Your/PythonFile.py"]

The result? Our runtime image just got 6x smaller! Six times! From > 1.1 GB to 170 MB.

6) Buildkit Cache Mounts:
We already got a small Docker image and fast builds when code changes, but we can also get fast builds when dependencies change 
This final trick is not known to many as it’s rather newer compared to the other features above. 
It leverages Buildkit cache mounts, which basically instruct Buildkit to mount and manage a folder for caching reasons. 
The interesting thing is that such cache will persist across builds!
By plugging this feature with Poetry cache (now you understand why I did want to keep caching?) we basically get a dependency cache that is re-used every time we build our project. 
The result we obtain is a fast dependency build phase when building the same image multiple times on the same environment.
Notice how the Poetry cache is not cleared after installation, as this would prevent to store and re-use the cache across builds. 
This is fine and wanted, as Buildkit will not persist the managed cache in the built image (plus, it’s not even our runtime image).

	FROM python:3.11-buster as builder

	RUN pip install poetry==VERSION

	ENV POETRY_NO_INTERACTION=1 \
	    POETRY_VIRTUALENVS_IN_PROJECT=1 \
	    POETRY_VIRTUALENVS_CREATE=1 \
	    POETRY_CACHE_DIR=/tmp/poetry_cache

	WORKDIR /app

	COPY pyproject.toml poetry.lock ./
	RUN touch README.md

	RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root		<--- Setting Up Persistent Cache

	FROM python:3.11-slim-buster as runtime

	ENV VIRTUAL_ENV=/app/.venv \
	    PATH="/app/.venv/bin:$PATH"

	COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

	COPY Data ./Data

	ENTRYPOINT ["python", "Path/To/Your/PythonFile.py"]

The con of this optimization? Cache mounts are not very CI friendly at the moment, as Buildkit doesn’t allow you controlling the storage location of the cache. 
It’s unsuprising that this is the most voted open GitHub issue on the Buildkit repo.

Summary:

- Keep layers small, minimizing the amount of stuff you copy and install in it
- Exploit Docker layer caching and reduce cache misses as much as possible
- Slow-changing things (project dependencies) must be built before fast-changing things (application code)
- Use Docker multi-stage builds to make your runtime image as slim as possible

This is how you can put them in practice in Python projects managed by Poetry, but the same principles can be applied to other dependency managers (such as PDM) and other languages.

Using Custom Dockerfiles in docker-compose:

To use a custom Dockerfile with Docker Compose, you need to specify the build context and optionally the Dockerfile name in your docker-compose.yml file. This allows Docker Compose to build images based on your custom Dockerfiles instead of pulling them from a registry. Here's how you can do it:

Basic Syntax
In your docker-compose.yml file, under the service that you want to build from a custom Dockerfile, you use the build directive. You can specify just the build context (a path to the directory containing your Dockerfile), or you can also specify the Dockerfile name if it's not the default Dockerfile.

Specifying Build Context Only
If your Dockerfile is named Dockerfile and located in the root of your context directory:

version: '3.8'
services:
  your_service:
    build: ./path/to/build/context	<--- will automatically find .Dockerfile file like docker build given the context
Specifying Both Build Context and Dockerfile Name
If your Dockerfile has a custom name or you want to specify it explicitly:

version: '3.8'
services:
  your_service:
    build:
      context: ./path/to/build/context
      dockerfile: CustomDockerfileName
Example
Let's say you have a project structure like this:

/myapp
  /myapp-service
    Dockerfile.custom
  docker-compose.yml
And you want to use Dockerfile.custom for building the image of myapp-service. Your docker-compose.yml would look something like this:

version: '3.8'
services:
  myapp-service:
    build:
      context: ./myapp-service
      dockerfile: Dockerfile.custom
    ports:
      - "8080:8080"
This configuration tells Docker Compose to build an image for the myapp-service using the Dockerfile located at ./myapp-service/Dockerfile.custom. The built image will then be used to run containers as defined under the service.

Additional Tips
Build Arguments: You can pass build arguments to your Dockerfile by adding an args subsection under build:
services:
  your_service:
    build:
      context: ./path/to/build/context
      dockerfile: CustomDockerfileName
      args:
        - MY_VARIABLE=value

Using Environment Variables: If you need to use environment variables in your Docker Compose file, you can reference them like ${VARIABLE_NAME} within the file.
By specifying the build context and optionally the Dockerfile name in your docker-compose.yml, you instruct Docker Compose to build your services using your custom Dockerfiles, giving you flexibility in how your containers are built and run.

To remove images created by Docker Compose along with stopping and removing containers, networks, and volumes, you can use the --rmi option with the docker-compose down command. The --rmi option specifies what types of images to remove after stopping and removing the containers:

--rmi local: Removes only images that don't have a custom tag. These are typically images built locally by Docker Compose.
--rmi all: Removes all images used by services defined in the Docker Compose file.
Example Usage
If you want to remove all images used by services defined in your Docker Compose file when you bring down your application, you would run:

docker-compose down --rmi all
This command stops and removes containers, networks, and volumes defined by your docker-compose.yml, as well as removing all images used by those services.

Additional Options
Removing Orphan Containers: If you also want to remove containers for services not defined in the current Compose file (orphans), you can add the --remove-orphans flag:
docker-compose down --rmi all --remove-orphans
Removing Volumes: To remove named volumes declared in the "volumes" section of the Compose file and anonymous volumes attached to containers, add the -v or --volumes flag:
docker-compose down --rmi all -v
Important Considerations
Data Persistence: Be cautious when removing volumes, especially if they contain data you wish to persist across container restarts or deployments.
Image Reuse: Removing images with custom tags (using --rmi all) means you'll need to rebuild those images or pull them again from a registry if you redeploy the services later.
Networks: By default, docker-compose down removes networks defined in the Compose file. Be mindful of external networks connected to your services; they won't be removed automatically.
By using the --rmi option with docker-compose down, you gain control over the cleanup process, allowing Docker Compose to manage images alongside containers, networks, and volumes, simplifying environment teardown and setup processes


To ensure that your Redpanda instance resets partitions and topics every time you bring it up with Docker Compose, you indeed need to manage the persistence of data stored in volumes. By default, Docker volumes persist data across container restarts and removals, which means that unless you explicitly remove these volumes, the data (including Kafka topics and partitions) will remain intact across docker-compose down and subsequent docker-compose up commands.

Here's how you can modify your Docker Compose setup to reset partitions and topics every time you compose up:

Option 1: Remove Volumes on Down
You can modify the down command to also remove the volumes associated with your Redpanda service. This ensures that all data is wiped clean when you bring the services down, and thus, when you bring them back up, they start fresh without any existing topics or partitions.

Modify your docker-compose down command to include the --volumes flag:

docker compose -f ./MicroServices/RedPanda.yml down --volumes
This command stops and removes containers, networks, and volumes defined in your RedPanda.yml file. Note that this will remove all data stored in the Redpanda volume, ensuring a clean state on the next startup.

Option 2: Use a Different Volume for Development
If you occasionally need to persist data across restarts (for example, during development testing), you could conditionally mount a volume only when needed. This approach requires manual intervention but gives you flexibility.

Remove the volume definition from your docker-compose.yml file temporarily when you want a clean state.
Run docker-compose up without the volume attached.
When you need persistence again, re-add the volume definition and run docker-compose up.
Option 3: Scripted Volume Removal
For a more automated approach, you could write a simple script that wraps your Docker Compose commands and conditionally removes volumes based on a flag or environment variable. This way, you can control whether volumes should be preserved or removed without manually editing the docker-compose.yml file.

Here's a basic example of such a script:

#!/bin/bash

# Check if the first argument is "up" or "down"
if [ "$1" = "up" ]; then
  docker compose -f ./MicroServices/RedPanda.yml up -d
elif [ "$1" = "down" ]; then
  if [ "$2" = "--reset" ]; then
    docker compose -f ./MicroServices/RedPanda.yml down --volumes
  else
    docker compose -f ./MicroServices/RedPanda.yml down
  fi
else
  echo "Usage: $0 {up|down} [--reset]"
fi
With this script, running ./script.sh up would start your services normally, and ./script.sh down --reset would stop the services and remove the volumes, resetting the state.

Conclusion
Choosing between these options depends on your development workflow and how often you need to reset the state of your Redpanda instance. Removing volumes on down is straightforward but destroys all data. Using conditional volume mounting or scripting provides more control over when data should be persisted or discarded.

Shareable 
SUGGESTIONS
with option 2 can i remove the volume and then reattach it when running docker compose up with a flag?
ANSWER | PHIND-70B MODEL
Yes, you can conditionally remove and reattach a volume when running docker-compose up with a flag by utilizing environment variables and Docker Compose's ability to use these variables in the docker-compose.yml file. This approach allows you to dynamically change the behavior of your Docker Compose setup based on the presence or value of an environment variable.

Based on the information from 1, you can achieve this by defining an environment variable that controls whether the volume should be mounted or not. Then, in your docker-compose.yml, you can use this variable to conditionally specify the volume path.

Here's how you can implement this:

Step 1: Define an Environment Variable
Create a .env file in the same directory as your docker-compose.yml. Inside this file, define an environment variable that will control the volume mounting. For example:

# .env
MOUNT_VOLUME=true
Step 2: Modify docker-compose.yml
In your docker-compose.yml, use the environment variable to conditionally set the volume mount. You can do this by using a ternary-like expression with the ${VARIABLE:-default} syntax, which evaluates to the value of VARIABLE if it exists and is not null, otherwise it evaluates to default.

services:
  redpanda-0:
    volumes:
      - ${MOUNT_VOLUME:+redpanda-0:/var/lib/redpanda/data}
In this example, if MOUNT_VOLUME is set to any value (indicating true), the volume redpanda-0 will be mounted at /var/lib/redpanda/data inside the container. If MOUNT_VOLUME is unset or empty, the expression after the colon (:) will be ignored, effectively removing the volume mount.

Step 3: Running Docker Compose Conditionally
Now, you can control whether the volume is mounted by setting the MOUNT_VOLUME environment variable when running docker-compose up. To mount the volume, ensure MOUNT_VOLUME is set in your .env file or export it before running Docker Compose:

export MOUNT_VOLUME=true
docker-compose up
To run without mounting the volume (effectively resetting the data), you can either comment out or remove the MOUNT_VOLUME line in your .env file or unset the environment variable:

unset MOUNT_VOLUME
docker-compose up
Or, you can override the environment variable directly in the command line:

MOUNT_VOLUME=false docker-compose up


Step 1: Define Environment Variables
Create a .env file in the same directory as your docker-compose.yml. Inside this file, define an environment variable that will control which volume should be mounted. For example:

# .env
ENVIRONMENT=dev
Step 2: Create Separate Compose Files for Development and Production
Create two Docker Compose override files: docker-compose.dev.yml for development configurations and docker-compose.prod.yml for production configurations. Each file will specify the volume mounts relevant to its environment.

docker-compose.dev.yml:

services:
  redpanda-0:
    volumes:
      - dev-volume:/var/lib/redpanda/data
volumes:
  dev-volume:
docker-compose.prod.yml:

services:
  redpanda-0:
    volumes:
      - prod-volume:/var/lib/redpanda/data
volumes:
  prod-volume:
Step 3: Modify Main docker-compose.yml
In your main docker-compose.yml, remove the volume specification from the service definition to allow the override files to control the volumes.

docker-compose.yml:

services:
  redpanda-0:
    # Other configurations...
    # Volumes are now defined in the override files
Step 4: Running Docker Compose with Environment-Specific Configurations
Now, you can control which volume gets mounted by specifying the appropriate override file when running docker-compose up. Use the -f option to specify the main compose file along with the override file.

To run with development configuration:

ENVIRONMENT=dev docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
To run with production configuration:

ENVIRONMENT=prod docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
This setup allows you to dynamically switch between different configurations based on the environment variable ENVIRONMENT, enabling you to easily toggle between development and production setups.

Remember, the .env file should be updated accordingly before running the commands, or you can set the ENVIRONMENT variable directly in the command line as shown above.

*HEALTHCHEKS AND RESTARTS:*

Implementing health checks and automatic restart mechanisms in Docker can significantly enhance the reliability and uptime of your applications. Below, I'll guide you through setting up health checks in both Dockerfiles and Docker Compose files, along with configuring automatic restarts for your containers.

Dockerfile Health Checks

In your Dockerfile, you can specify a health check instruction to periodically check the health of your containerized application. 
Here's an example Dockerfile snippet for a simple web server:

FROM nginx:latest

# Set a health check
HEALTHCHECK --interval=30s --timeout=10s \
  CMD curl --fail http://localhost/ || exit 1

This health check uses curl to make a request to the web server running inside the container every 30 seconds. 
If the request fails, Docker marks the container as unhealthy after 10 seconds.

Docker Compose Health Checks and Auto-Restarts

In Docker Compose, you can define health checks and restart policies for your services. 
Here's an example docker-compose.yml snippet that demonstrates setting up health checks and auto-restarts for a FastAPI service:

version: "3.8"

services:
  fastapi:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    restart: on-failure
    command: ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    healthcheck:
      test: curl --fail http://localhost:8000/health || exit 1
      interval: 2s
      timeout: 5s
      retries: 3
      start_period: 5s

  autoheal:
    restart: always
    image: willfarrell/autoheal
    environment:
      - AUTOHEAL_CONTAINER_LABEL=all
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

In this example:

The fastapi service has a health check configured to periodically test the /health endpoint. 
It uses curl to make the request, and Docker considers the service unhealthy if the check fails three times consecutively.
The restart: on-failure policy tells Docker to restart the container if it exits due to an error.
The autoheal service uses the willfarrell/autoheal image to monitor all containers labeled with AUTOHEAL_CONTAINER_LABEL=all. 
If any container becomes unhealthy, autoheal restarts it automatically.

*SYNTAX:*

Docker and Docker Compose offer a wide range of commands to manage containers, images, networks, and volumes. 
Below is a comprehensive list of commands for Dockerfiles and Docker Compose, along with brief descriptions of what they do.

Dockerfile Commands

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. 
Here are some common Dockerfile instructions:

FROM: Specifies the base image from which you are building.
RUN: Executes any commands in a new layer on top of the current image and commits the result.
CMD: Provides defaults for an executing container.
LABEL: Adds metadata to an image as a pair of key-value.
EXPOSE: Informs Docker that the container listens on the specified network ports at runtime.
ENV: Sets the environment variable.
ADD: Copies new files, directories or remote file URLs from <src> and adds them to the filesystem of the image at the path <dest>.
COPY: Copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
ENTRYPOINT: Allows you to configure a container that will run as an executable.
VOLUME: Creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers.
USER: Specifies the user name (or UID) and optionally the user group (or GID) to use when running the image and for any RUN, CMD and ENTRYPOINT instructions that follow it in the Dockerfile.
WORKDIR: Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile.
ARG: Defines a variable that users can pass at build-time to the builder with the docker build command.
ONBUILD: Adds a trigger instruction when the image is used as the base for another build.
STOPSIGNAL: Specifies the system call signal that will be sent to the container to exit.
HEALTHCHECK: Tells Docker how to test a container to check that it is still working.
SHELL: Overrides the default shell used for the shell form of the RUN instruction.

Docker Compose Commands

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. Here are some Docker Compose commands:

docker compose up: Builds, (re)creates, starts, and attaches to containers for a service.
docker compose down: Stops and removes containers, networks, and volumes defined in your docker-compose.yml file.
docker compose build: Builds or rebuilds services.
docker compose config: Validates and displays the Compose file.
docker compose cp: Copies files/folders between a service container and the local filesystem.
docker compose create: Creates containers for a service.
docker compose exec: Executes a command in a running container.
docker compose images: Lists images used by the created containers.
docker compose kill: Force stops service containers.
docker compose logs: Views output from containers.
docker compose ps: Lists containers.
docker compose pull: Pulls service images.
docker compose push: Pushes service images.
docker compose restart: Restarts service containers.
docker compose rm: Removes stopped service containers.
docker compose run: Runs a one-off command on a service.
docker compose start: Starts services.
docker compose stop: Stops services.
docker compose version: Shows the Docker Compose version information.
docker compose wait: Blocks until the first service container stops.
docker compose watch: Watches build context for service and rebuilds/refreshes containers when files are updated.

These commands cover a broad spectrum of operations, from building and running containers to managing their lifecycle and interacting with them.

Below is an overview of common elements and their meanings in a Docker Compose YAML file.

Version
Specifies the version of the Docker Compose file format. This should be defined at the root level of the file.

version: '3.8'
Services
Defines the containers to be created. Each service runs in its own container.

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
Image
Specifies the Docker image to use for the container.

image: nginx:latest
Build
Used instead of image to build an image from a Dockerfile.

build:
  context: .
  dockerfile: Dockerfile
Ports
Maps ports between the host and the container.

ports:
  - "8080:80"
Environment Variables
Sets environment variables in the container.

environment:
  - MY_VAR=value
Or using the env_file option:

env_file:
  - .env
Volumes
Mounts paths or named volumes.

volumes:
  - ./data:/data
Or using named volumes:

volumes:
  myvolume:
And then referencing them in services:

services:
  db:
    image: postgres
    volumes:
      - myvolume:/var/lib/postgresql/data
Networks
Defines custom networks to be used by the containers.

networks:
  frontend:
  backend:
And then specifying which network(s) a service should connect to:

services:
  web:
    networks:
      - frontend
      - backend
Depends On
Specifies dependencies between services, ensuring they start in dependency order.

depends_on:
  - db
Healthcheck
Defines how to check the health of a service.

healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 30s
  timeout: 10s
  retries: 3
Restart Policies
Configures restart policies for containers.

restart: always
Options include no, always, on-failure, and unless-stopped.

Command and Entry Point
Overrides the default command or entrypoint set in the Dockerfile.

command: ["bundle", "exec", "rails", "server"]
entrypoint: ["php", "-a"]
Deploy
Specifies deployment options (like replicas) for services in swarm mode.

deploy:
  replicas: 3
  placement:
    constraints: [node.role == worker]

This overview covers many of the essential elements you'll encounter in Docker Compose YAML files. 
For a complete reference, including advanced options and detailed explanations, refer to the official Docker documentation.

[Docker Compose](https://docs.docker.com/reference/cli/docker/compose/)
[Another Docker Compose Reference](https://docs.divio.com/reference/docker-docker-compose/)

TO PUSH OR PULL TO A DOCKERHUB REPO

Create a DockerHub Repo, then:

docker push kazuhirabenedictmiller/alfredoaiapp:tagname


Authentication:

docker login -u <username> -p <password>: Logs in to your Docker Hub account. You can omit the -p flag, and it will prompt you for the password. This is essential before pushing images.
docker logout: Logs out of your Docker Hub account.
Image Management (Pushing/Pulling):

docker push <username>/<repository>:<tag>: Pushes a Docker image to your Docker Hub repository. For example: docker push kazuhirabenedictmiller/alfredoaiapp:latest. The <username> is your Docker Hub username, <repository> is the name of your repository on Docker Hub, and <tag> is the image tag (e.g., latest, v1.0, etc.).
docker pull <username>/<repository>:<tag>: Pulls a Docker image from Docker Hub to your local machine. Same naming convention as docker push. Example: docker pull kazuhirabenedictmiller/alfredoaiapp:latest.
Repository Management (Less Frequent):

Docker Hub's repository management is primarily done through the web interface on the Docker Hub website. There are limited command-line options for this. You'd typically create, manage (set visibility, collaborators, etc.), and delete repositories via the website.
Searching:

docker search <term>: Searches Docker Hub for images matching a given term. Example: docker search python. This is helpful for finding base images or other pre-built images you might want to use.
Local Image Operations (Related, but not directly Docker Hub):

docker images: Lists locally stored Docker images. You'll often use this to find the image you want to push.
docker tag <image_id_or_name> <username>/<repository>:<tag>: Tags a local image. This is important because you need to tag the image with your Docker Hub username and repository name before you can push it. Example: docker tag my-app kazuhirabenedictmiller/alfredoaiapp:latest. You can use the image ID or the existing image name.
docker rmi <username>/<repository>:<tag> or docker rmi <image_id>: Removes a local Docker image.
Example Workflow (Local to Docker Hub):

docker build -t my-app . (Build your image locally)
docker tag my-app kazuhirabenedictmiller/alfredoaiapp:latest (Tag the image)
docker login -u <username> -p <password> (Log in to Docker Hub)
docker push kazuhirabenedictmiller/alfredoaiapp:latest (Push the image)
This is the core set of commands you'll use for interacting with Docker Hub from the command line or within scripts (like your GitHub Action).  The repository management commands are less frequent, as you'll usually handle those through the Docker Hub website.

Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credential-stores
