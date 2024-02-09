


import json
from datetime import datetime
import time
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

def create_producer():
    while True:
        try:
            return KafkaProducer(bootstrap_servers='kafka:9092')
        except NoBrokersAvailable:
            print("Waiting for Kafka broker...")
            time.sleep(5)  # Wait for  5 seconds before retrying

producer = create_producer()
# Continue with the rest of your script

prod = KafkaProducer(bootstrap_servers=['kafka:9092'], value_serializer=lambda x:json.dumps(x).encode('utf-'))

for n in range(555):
    
    data = {"num":n, "date":datetime.now().strftime("%H:%M:%S")}

    print("produced " + str(data["num"]) +' ' + data["date"])
    
    prod.send('input-topic', value=data)
    
    time.sleep(1)
