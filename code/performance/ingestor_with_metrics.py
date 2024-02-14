import os
import json
import pymongo
import dotenv
from kafka import KafkaConsumer
import time

"""
Slight modification to the ingestor.py script to measure the time it takes to insert a message into the database and log it to a file.
"""

dotenv.load_dotenv()
KAFKA_BROKER = os.getenv('KAFKA_BROKER')
MONGO_URL = os.getenv('MONGO_URL')

if not KAFKA_BROKER or not MONGO_URL:
    raise Exception("KAFKA_BROKER and MONGO_URL must be set")

consumer = KafkaConsumer("measurements", bootstrap_servers=KAFKA_BROKER, consumer_timeout_ms=5000)

db_client = pymongo.MongoClient(MONGO_URL)
db = db_client["ingestionDB"]
collection = db["measurements"]

durs = []
for message in consumer:
    data = json.loads(message.value)
    start = time.time()
    resp = collection.insert_one(data)
    end = time.time()
    durs.append(end - start)

average_response_time = sum(durs) / len(durs)
with open("logs/ingestor.log", "a") as f:
    f.write(f"{average_response_time}\n")

consumer.close()
db_client.close()
