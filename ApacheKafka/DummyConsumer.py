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
