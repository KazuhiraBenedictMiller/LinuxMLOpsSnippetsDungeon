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

Start the Airflow web server and scheduler components in separate terminals:

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

To stop and delete containers, delete volumes with database data and download images, run:

	> $ sudo docker compose down --volumes --remove-orphans --rmi  all
	> $ sudo docker compose down --volumes --remove-orphans

⚠️  **NOTE:** On Docker Compose Airflow the default user and password are airflow and airflow, when accessing the Web UI, but you can always setup a new user in a containers' terminal.

[Apache Airflow Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
[Apache Airflow Docs](https://airflow.apache.org/docs/)
