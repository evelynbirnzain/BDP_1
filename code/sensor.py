import json
import os
import sys
from time import sleep

import dotenv
from kafka import KafkaProducer

dotenv.load_dotenv()

KAFKA_BROKER = os.getenv('KAFKA_BROKER')
INPUT_FILE = os.getenv('DATA_FILE')

if not KAFKA_BROKER or not INPUT_FILE:
    raise Exception("KAFKA_BROKER and DATA_FILE must be set")


def main():
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

    with open(INPUT_FILE) as f:
        messages = json.load(f)

    n = int(sys.argv[1]) if len(sys.argv) > 1 else len(messages)

    for message in messages[:n]:
        payload = json.dumps(message).encode('utf-8')
        r = producer.send('measurements', payload)
        r.get(10)
        print(f"Sent {message['id']}")
        sleep(0.1)

    print(f"Sent {n} messages")
    producer.flush()
    producer.close()


if __name__ == "__main__":
    main()
