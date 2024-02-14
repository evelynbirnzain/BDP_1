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

* Set up any Kafka instance. A local testing instance can be set up using the `docker-compose_kafka.yml` file in
  the `code` directory.
* Add the broker URL to the `.env` file.

```bash
# .env
KAFKA_BROKER_URL="localhost:9092"
```

### Ingestor

Run any number of ingestors using the `ingestor.py` script. The ingestors will poll Kafka and measurements into
the `coredms`.

```bash
    python3 code/ingestor.py
```

## Simulate sensors

Run `sensor.py` to simulate the sensors. The script will produce messages to the Kafka topic.

```bash
    python3 code/sensor.py
```












