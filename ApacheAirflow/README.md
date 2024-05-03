## ▪️ Apache Airflow 🪅

**Local Installation:**

[Apache Airflow pip Installation](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)
	
Create and Activate your Virtual Env (venv), then:

⚠️  **NOTE:** For Airflow venv installations all airflow commands must be typed in terminals after activating your venv.

	> $ pip install "apache-airflow[celery]==2.8.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.8.txt"
	> $ airflow db init

Export Airflow Home Variable:

	> $ export AIRFLOW_HOME=~/airflow

Setup plugins and dags folders (logs folder should be already installed):

	> $ cd airflow
	> $ mkdir ./dags ./plugins
	> $ sudo chmod 777 ./dags ./plugins

Create Admin User:

	> $ airflow users create \  
	    --username admin \  
	    --password admin  \  
	    --firstname <YourFirstName> \  
	    --lastname <YourLastName> \  
	    --role Admin \  
	    --email admin@example.com

Start the Airflow webserver and scheduler components in separate terminals:

	> $ airflow webserver --port 8080  
	> $ airflow scheduler

You can now access Airflow at `http://localhost:8080`

Move your Dags inside your venv to the AIRFLOW_HOME with:

	 > $ sudo cp path/to/DAG_NAME.py $AIRFLOW_HOME/dags

List all your Dags:

	> $ airflow dags list

Unpause a Dag:

	> $ airflow dags unpause DAG_ID

Trigger a Dag:

	> $ airflow dags trigger DAG_ID

**Docker:**

Create a Directory for Apache Airflow:

	> $ mkdir airflowdocker

Then cd in that Directory and create the 4 main folders and change their ownership:
	
	> $ cd airflowdocker
	> $ mkdir -p ./dags ./logs ./plugins ./config
	> $ sudo chmod 777 ./dags ./logs ./plugins ./config

Then, while still in that dir:

	> $ echo -e "AIRFLOW_UID=$(id  -u)" > .env
	
And fetch the Docker Compose for Airflow:

	> $ curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml'

Docker Compose to build and run the containers:

	> $ sudo docker compose up airflow-init
	> $ sudo docker compose up

Let that terminal run.

The dags folder is now located on airflowdocker/dags, so to move a dag there:

	> $ sudo cp path/to/DAG_NAME.py path/to/airflowdocker/dags

You can now access Airflow at `http://localhost:8080`

Also, you can enter some airflow-cli commands from the webserver container id, or run a bash shell inside the container with:

	> $ sudo docker exec -i-t AIRFLOW_WEBSERVER_CONTAINER_ID sh
	> $ sudo docker compose exec -i -t AIRFLOW_WEBSERVER_CONTAINER_ID airflow dags unpause DAG_ID

To stop and delete containers, delete volumes with database data and downloaded images, run:

	> $ sudo docker compose down --volumes --remove-orphans --rmi  all
	> $ sudo docker compose down --volumes --remove-orphans

⚠️  **NOTE:** On Docker Compose Airflow the default user and password are airflow and airflow, when accessing the Web UI, but you can always setup a new user in a containers' terminal.

[Apache Airflow Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
[Apache Airflow Docs](https://airflow.apache.org/docs/)

**[BONUS]:**

Let's build a multi-container Application using Airflow for batch Streaming.
So far, we know that a docker-compose.yaml file can actually spin up containers from different Dockerfiles, so, here's the folder structure for such project:

	project-root/
	│
	├── docker-compose.yml
	├── Dockerfile.airflow
	├── requirements.txt
	│
	├── Sevice1/
	│   ├── Dockerfile
	│   └── python_script_1.py
	│
	└── Service2/
	   ├── Dockerfile
	   └── python_script_2.py

After the directories setup, cd into the project root and:
	
	> $ mkdir -p ./dags ./logs ./plugins ./config ./postgres_data
	> $ sudo chmod 777 ./dags ./logs ./plugins ./config ./postgres_data
	> $ sudo docker compose up

With this given architecture, the docker-compose file is going to build 2 different containers running on the same Airflow cluster, one for the WebServer and one for the Scheduler here's an example of how that compose file would look like:

```yml
#version: '3.8'
version: '3'

networks:
  airflow_network:
    driver: bridge

services:
  webserver:
    build:
      context: .
      dockerfile: ./Dockerfile.airflow
    image: airflow-webserver
    ports:
      - "8080:8080"
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
      - AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
      - AIRFLOW__CORE__LOAD_EXAMPLES=False
    volumes:
      - ./dags:/opt/airflow/dags
      - ./logs:/opt/airflow/logs
      - ./plugins:/opt/airflow/plugins
      - ./config:/opt/airflow/config
    command: >
      bash -c "airflow db init &&
               airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com &&
               airflow webserver"
    networks:
      - airflow_network
    depends_on:
      - postgres

  scheduler:
    build:
      context: .
      dockerfile: ./Dockerfile.airflow
    image: airflow-scheduler
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
      - AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
      - AIRFLOW__CORE__LOAD_EXAMPLES=False
    volumes:
      - ./dags:/opt/airflow/dags
      - ./logs:/opt/airflow/logs
      - ./plugins:/opt/airflow/plugins
      - ./config/:/opt/airflow/config
    command: airflow scheduler
    networks:
      - airflow_network
    depends_on:
      - postgres

  ubuntu:
    image: ubuntu:latest
    tty: true
    stdin_open: true
    networks:
      - airflow_network

  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - ./postgres_data:/var/lib/postgresql/data
    networks:
      - airflow_network
```

This one above is a super simple Containerization for a multi container application that also uses Apache Airflow.
<br>
However, we can actually tweak the docker compose by taking inspiration from the official one to make it more suitable for production purposes.

After Launching the docker compose simply copy your dags in the dags folder and open the web UI at localhost:8080.
<br>
To unpause and use the airflow cli, enter into the webserver container terminal to launch your commands:

 	> $ sudo docker exec -i -t -u root AIRFLOW_WEBSERVER_CONTAINER_ID_OR_NAME airflow dags unpause DAG_ID
 
To install requirements for your dags, you'll need to extend the docker compose, that's why we needed a docker file that does nothing but installing the requirements.

Here's how the Dockerfile.airflow will look like:

```docker
# Use the official Airflow image as the base
FROM apache/airflow:2.8.1

# Set the working directory in the container to /opt/airflow
WORKDIR /opt/airflow

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
```

**⚠️ NOTE:** There are some serious consideration to be made regarding the usage of the Executor and a production environment setup:

For a basic Airflow setup, you typically only need two main components: the `webserver` and the `scheduler`. These two services handle the core functionality of Airflow:

-   The `webserver` provides the UI where you can manage and monitor your workflows (DAGs).
-   The `scheduler` is responsible for scheduling tasks and executing them.

However, depending on your specific use case and architecture, you might want to consider additional components or services:

1.  **Worker Containers:** If you're using the CeleryExecutor or KubernetesExecutor, you'll need worker containers to actually execute the tasks. These workers can be scaled independently of the scheduler and webserver.

2.  **Triggerer:** If you're using the Triggerer component, which allows external systems to trigger DAG runs, you may need to add a separate service for it.

3.  **Database:** Although you already have a PostgreSQL service in your `docker-compose.yml`, it's worth noting that Airflow requires a database backend to store metadata about the workflows and their state. Which is correctly included in this setup, sometimes for production environment, it's better to use 2 separate database services for airflow metadata and actual data.

4.  **Redis:** If you're using the LocalExecutor, Redis is used as a message broker for task queuing. You don't need a separate Redis service if you're using the LocalExecutor, as it's included in the Airflow image. However, if you switch to the CeleryExecutor, you'll need to add a Redis service.

5.  **Additional Services:** Depending on your workflows, you might need additional services such as data warehouses, data lakes, or other APIs that your DAGs interact with.

6.  **Logging and Monitoring:** For production environments, you might want to add logging and monitoring services to collect logs and metrics from your Airflow instance.

7.  **Volume Mounts:** With this docker compose, you've mounted several volumes for persisting data and configurations. Ensure that these are sufficient for your needs, especially if you're running multiple executors or workers.

In summary, the `webserver` and `scheduler` are the minimum required components for Airflow to function. Additional services depend on your specific workflow requirements and the executor you choose to use.

[Official Docker Compose for Apache Airflow](https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml)
[TaskFlow API for Apache Airflow >= 2.0.0](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)
