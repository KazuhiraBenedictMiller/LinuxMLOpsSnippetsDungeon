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
