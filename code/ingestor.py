import logging
import os
import json
import sys

import pymongo
import dotenv
from kafka import KafkaConsumer

dotenv.load_dotenv()
KAFKA_BROKER = os.getenv('KAFKA_BROKER')
MONGO_URL = os.getenv('MONGO_URL')

logfile = sys.argv[1] if len(sys.argv) > 1 else 'logs/ingestor.log'
logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(logfile)])

if not KAFKA_BROKER or not MONGO_URL:
    raise Exception("KAFKA_BROKER and MONGO_URL must be set")

consumer = KafkaConsumer("measurements", bootstrap_servers=KAFKA_BROKER, group_id="ingestor")

db_client = pymongo.MongoClient(MONGO_URL)
db = db_client["ingestionDB"]
collection = db["measurements"]

logging.info("Starting ingestion")
durs = []
for message in consumer:
    data = json.loads(message.value)
    resp = collection.insert_one(data)
    logging.info(f"Inserted {data['id']}")

logging.info("Ingestion complete")

consumer.close()
db_client.close()
