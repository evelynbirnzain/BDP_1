import json
import os
import time

import dotenv
from kafka import KafkaProducer

dotenv.load_dotenv()

KAFKA_BROKER = os.getenv('KAFKA_BROKER')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
INPUT_FILE = os.getenv('DATA_FILE')

if not KAFKA_BROKER or not KAFKA_TOPIC or not INPUT_FILE:
    raise Exception("KAFKA_BROKER, KAFKA_TOPIC and INPUT_FILE must be set")

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

with open(INPUT_FILE) as f:
    messages = json.load(f)

for message in messages:
    payload = json.dumps(message).encode('utf-8')
    future = producer.send(KAFKA_TOPIC, payload)
    result = future.get(timeout=60)
    print(result)
    time.sleep(10)
