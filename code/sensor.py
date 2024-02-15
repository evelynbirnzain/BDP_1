import json
import logging
import os
import sys
from time import sleep

import dotenv
from kafka import KafkaProducer

dotenv.load_dotenv()

KAFKA_BROKER = os.getenv('KAFKA_BROKER')
INPUT_FILE = os.getenv('DATA_FILE')

logfile = sys.argv[2] if len(sys.argv) > 2 else 'logs/sensor.log'
logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(logfile)])

if not KAFKA_BROKER or not INPUT_FILE:
    raise Exception("KAFKA_BROKER and DATA_FILE must be set")


def main():
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

    with open(INPUT_FILE) as f:
        messages = json.load(f)

    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(messages)

    logging.info(f"Sending {n} messages")
    for message in messages[:n]:
        payload = json.dumps(message).encode('utf-8')
        r = producer.send('measurements', payload)
        r.get(10)
        logging.info(f"Sent {message['id']}")
        sleep(0.1)

    logging.info("All messages sent")
    producer.flush()
    producer.close()


if __name__ == "__main__":
    main()
