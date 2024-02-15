# Installation & Deployment

## Coredms

Set up any MongoDB instance (e.g. 3-node replicat set on Atlas, any local deployment, etc.).
Add the connection string to the `.env` file.

```bash
# .env
MONGO_URL="mongodb+srv://<username>:<password>@<host>/<dbname>?retryWrites=true&w=majority"
```

## Dataingest

### Kafka

* Set up any Kafka instance. A local testing instance can be set up using the `code/docker-compose_kafka.yml` file.
* Add the broker URL to the `.env` file.

```bash
# .env
KAFKA_BROKER_URL="localhost:9092"
```

* Create a topic "measurements" with an appropriate number of partitions and replication factor.E.g. when using the
  local Kafka, use the following:

```bash
docker-compose -f code/
docker-compose_kafka.yml exec kafka kafka-topics.sh --create --topic measurements --partitions 32 --replication-factor 1 --bootstrap-server kafka:9092
```

### Ingestor

* Create a ``venv`` and install the dependencies.
* Run any number of ingestors using the `ingestor.py` script. The ingestors will poll Kafka and insert measurements into
  the `coredms`.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r code/requirements.txt

python3 code/ingestor.py
```

## Simulate sensors

Run `sensor.py` to simulate the sensors using the same ``venv``. The script will produce messages to the Kafka topic.

```bash
python3 code/sensor.py
```












