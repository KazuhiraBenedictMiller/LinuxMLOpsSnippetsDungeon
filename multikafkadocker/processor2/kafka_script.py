import json
from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import time
from datetime import datetime

def create_producer():
    while True:
        try:
            return KafkaProducer(bootstrap_servers='kafka:9092')
        except NoBrokersAvailable:
            print("Waiting for Kafka broker...")
            time.sleep(5)  # Wait for  5 seconds before retrying

producer = create_producer()
# Continue with the rest of your script


cons = KafkaConsumer(
    'input-topic',
    bootstrap_servers=['kafka:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

contents = ''

for message in cons:
    # Write the message value to the file
        
    print('got ' + str(message.value) + " at " + datetime.now().strftime("%H:%M:%S") + '\n')    


