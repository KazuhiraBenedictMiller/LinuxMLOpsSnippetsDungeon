
## ▪️ Apache Kafka 🛗

**Local Installation:**

[Apache Kafka Installation](https://kafka.apache.org/quickstart)

Make sure you have Java installed with:

	> $ java --version

If not Installed, install it with:

	> $ apt install openjdk-17-jdk

Then, mkdir for a Kafka folder and cd into it:

	> $ mkdir KafkaFolder
	> $ cd KafkaFolder

Now, Download the latest Kafka Binaries and Extract them:

	> $ wget https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz
	> $ tar kafka_2.13-3.6.1.tgz

cd into the newest extracted folder:

	> $ cd kafka_2.13-3.6.1

Start the Zookeper Service and let it run:

	> $ bin/zookeeper-server-start.sh config/zookeeper.properties

Open another terminal, cd into path/to/kafka_2.13-3.6.1, then start the Kafka Broker Server and let it run:

	> $ bin/kafka-server-start.sh config/server.properties

On another Terminal,  cd into path/to/kafka_2.13-3.6.1 and Create a new Kafka Topic:

	> $ bin/kafka-topics.sh --create --topic YOUR_TOPIC_NAME --bootstrap-server localhost:9092

Apache Kafka is now running and ready to be used both in the CLI and Python.

**Docker:**

This one is a bit more tricky as there are no officials Docker images and docker-compose.yaml files from the Apache Kafka Project.
We'll use one that can be found at this [Repo](https://github.com/wurstmeister/kafka-docker).
You can also a custom docker-compose.yaml that I made myself, that I'll write down later.

Create a KafkaDocker folder and cd into it:

	> $ mkdir KafkaDocker
	> $ cd KafkaDocker

Create a docker-compose.yaml and copy paste inside it the following (any way to make this is valid, will show just one:

	> $ touch docker-compose.yaml
	> $ nano docker-compose.yaml

**docker-compose.yaml**

```yml
version: '3'

services:
  zookeeper:
    image: wurstmeister/zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
  kafka:
    image: wurstmeister/kafka
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: localhost
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
```

This way it will compose and run 2 containers and name them respectively, one for Zookeeper and one for Kafka.
Run the compose command and check if the container are up and running:

	> $ sudo docker compose up -d
	> $ sudo docker ps
 
The -d flag stands for "detach", which means that the container will run in the background in case you don't want them to keep running in a terminal.

Now that both Kafka and Zookeeper are up and running, we'll need to get into the Kafka Terminal:

	> $ sudo docker exec -i -t kafka /bin/bash

While in the Kafka Container Terminal, we'll need to do a couple of things, first of which creating a topic:

	> $ kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic TOPIC_NAME

Only one of Zookeeper or Bootstrap Server needs to be specified, just in case: --zookeeper zookeeper:2181

Before moving on, we can list out our topics by Bootstrap server or zookeeper with (2 options given, but both fine):

	> $ kafka-topics.sh --list --zookeeper localhost:2181
	> $ kafka-topics.sh --list --zookeeper zookeeper:2181
	
OR

	> $ kafka-topics.sh --list --bootstrap-server localhost:9092
	> $ kafka-topics.sh --list --bootstrap-server kafka:9092

Now that Kafka is up and running and we are in the Kafka Container Terminal, we can run Kafka command with Bash, such as:

	> $ kafka-console-producer.sh --topic TOPIC_NAME --bootstrap-server localhost:9092
	> $ kafka-console-consumer.sh --topic TOPIC_NAME --from-beginning --bootstrap-server localhost:9092

Now, Kafka would be fine and running, but in case we want to use it with Python, while still in the kafka container terminal:

	> $ apt-get update && apt-get upgrade
	> $ apt-get install python3
	> $ apt-get install python3-pip -y
	> $ apt-get pip install kafka-python

We now have a fully functioning Kafka Container with python installed, but what if I want to move my local Python Consumer and Producer Scripts?

First of all, while in Kafka Container Terminal:

	> $ mkdir newfolder
	> $ cd newfolder

Now, we can either clone a Git Repo after installing Git:

	> $ apt-get install git
	> $ git clone GIT_REPO_LINK

OR, we can move files from the host to Kafka Container or vice-versa:

	> $ cd FOLDER_WHERE_FILES_TO_DOCKER_IS
	> $ sudo docker cp ./FILE_NAME CONTAINER_ID:/FOLDER_IN_CONTAINER

Finally, execute the Consumer and Producer Scripts either in 2 separate Terminals, while both in the Kafka Container, or, with exec command as it follows:

	> $ sudo docker exec -i -t RUNNING_KAFKA_CONTAINER_ID_OR_NAME python3 /path/to/producer.py
	> $ sudo docker exec -i -t RUNNING_KAFKA_CONTAINER_ID_OR_NAME python3 /path/to/consumer.py

Beware that consumer and producer paths are actually the paths INSIDE your Container.

**To use Apache Kafka with Python:**

	> $ pip install kafka-python

[Apache Kafka  Docs](https://kafka.apache.org/documentation/)
[kafka-python Docs](https://kafka-python.readthedocs.io/en/master/#)
[Apache Kafka Unofficial Docker Repo](https://github.com/wurstmeister/kafka-docker)

**[BONUS]:**

Let's build a multi-container Application using Kafka for real-time Streaming.
So far, we know that a docker-compose.yaml file can actually spin up containers from different Dockerfiles, so, here's the folder structure for such project:

	project-root/
	│
	├── docker-compose.yml
	│
	├── kafka-processor-1/
	│   ├── Dockerfile
	│   └── kafka_script_1.py
	│
	├── kafka-processor-2/
	│   ├── Dockerfile
	│   └── kafka_script_2.py
	│
	└── kafka-processor-3/
	   ├── Dockerfile
	   └── kafka_script_3.py

After the directories setup, cd into it and:

	> $ sudo docker compose up

With this given architecture, the docker-compose file is going to build 2 different containers running on the same kafka cluster, here's an example of how that compose file would look like:


```yml
version: '3'

networks:
  kafka-net:
    driver: bridge

services:
  zookeeper:
    image: wurstmeister/zookeeper:latest
    container_name: zookeeper
    networks:
      - kafka-net
    ports:
      - "2181:2181"
    environment:
      ALLOW_ANONYMOUS_LOGIN: 'yes'
    healthcheck:
      test: ["CMD", "nc", "-z", "localhost", "2181"]
      interval: 10s
      retries: 3
      timeout: 5s

  kafka:
    image: wurstmeister/kafka:latest
    container_name: kafka
    depends_on:
      - zookeeper
    networks:
      - kafka-net
    ports:
      - "9092:9092"
    environment:
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_CREATE_TOPICS: "input-topic:1:1 intermediate-topic:1:1 output-topic:1:1"
      KAFKA_ADVERTISED_PORT: 9092
      KAFKA_BROKER_ID: 1
      KAFKA_HOST_NAME: kafka
      KAFKA_LOG_DIRS: /kafka/kafka-logs
      KAFKA_UNCLEAN_LEADER_ELECTION_ENABLE: "false"
      ALLOW_PLAINTEXT_LISTENER: 'yes'
    healthcheck:
      test: ["CMD", "nc", "-z", "localhost", "9092"]
        interval: 10s
        retries: 3
        timeout: 5s

  kafka-processor-1:
    container_name: processor1
    restart: always
    build: ./processor1
    depends_on:
      - zookeeper
      - kafka
    networks:
      - kafka-net
    volumes:
      - ./processor1:/app
    working_dir: /app
    command: python3 kafka_script.py

  kafka-processor-2:
    container_name: processor2
    restart: always
    build: ./processor2
    depends_on:
      - zookeeper
      - kafka
      - kafka-processor-1
    networks:
      - kafka-net
    volumes:
      - ./processor2:/app
    working_dir: /app
    command: python3 kafka_script.py
    
  kafka-processor-3:
    container_name: processor3
    restart: always
    build: ./processor3
    depends_on:
      - zookeeper
      - kafka
      - kafka-processor-1
      - kafka-processor-2
    networks:
      - kafka-net
    volumes:
      - ./processor3:/app
    working_dir: /app
    command: python3 kafka_script.py
```

The Syntax is pretty much self-explainatory, every container is ran after the dependency is met and then everything works smoothly.
The docker-compose also contains health checks for the zookeeper service and the kafka broker connection status

The Dockerfile inside each folder, will look like this instead:

```docker
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run your_script.py when the container launches
CMD ["python3", "kafka_script.py"]
```

And here you have an example of a fully functioning multi-layer kafka architecture.

A simple Producer and Consumer Python Script will look like this:

**Producer:**

```python
import json
from datetime import datetime
import time
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import logging

# Configure logging to write logs to a file
logging.basicConfig(filename='producer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_producer():
    while True:
        try:
            return KafkaProducer(bootstrap_servers='kafka:9092')
        except NoBrokersAvailable:
            logging.info("Waiting for Kafka broker...")
            time.sleep(5)  # Wait for 5 seconds before retrying

# Create Kafka producer
producer = create_producer()

# Create a Kafka producer with JSON serializer
prod = KafkaProducer(bootstrap_servers=['kafka:9092'], value_serializer=lambda x:json.dumps(x).encode('utf-8'))

n = 0

while True:
    data = {"num": n, "date": datetime.now().strftime("%H:%M:%S")}

    logging.info("Produced %s at %s", str(data["num"]), data["date"])

    # Send message to Kafka input-topic
    prod.send('input-topic', value=data)

    time.sleep(1)

    n += 1
```

**Consumer:**

```python
import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(filename='consumer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_producer():
    while True:
        try:
            return KafkaProducer(bootstrap_servers='kafka:9092')
        except NoBrokersAvailable:
            logging.info("Waiting for Kafka broker...")
            time.sleep(5)  # Wait for 5 seconds before retrying

# Create Kafka producer
producer = create_producer()

# Continue with the rest of your script

# Create Kafka consumer
cons = KafkaConsumer(
    'input-topic',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for message in cons:
    # Write the message value to the log file
    logging.info("Got %s at %s", str(message.value), datetime.now().strftime("%H:%M:%S"))
```

As you can see in Both Scripts, you have a first check to wait for the Broker Connection and a logging logic that will also help detecting anomalies. (the logs file will be located in the working dir)
