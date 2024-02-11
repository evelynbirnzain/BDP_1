import os
import json
import pymongo
import dotenv
from kafka import KafkaConsumer

dotenv.load_dotenv()
KAFKA_BROKER = os.getenv('KAFKA_BROKER')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')

MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_HOST = os.getenv('MONGO_HOST')

if not KAFKA_BROKER or not KAFKA_TOPIC or not MONGO_USERNAME or not MONGO_PASSWORD or not MONGO_HOST:
    raise Exception("KAFKA_BROKER, KAFKA_TOPIC, MONGO_USERNAME, MONGO_PASSWORD and MONGO_HOST must be set")

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKER)

db_client = pymongo.MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}/")
db = db_client["ingestionDB"]
collection = db["measurements"]

for message in consumer:
    data = json.loads(message.value)
    resp = collection.insert_one(data)
    print(f"Inserted document: {collection.find_one({'_id': resp.inserted_id})}")
