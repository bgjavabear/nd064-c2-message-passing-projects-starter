import json
import logging
import sys
import time

from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("location-service")
BOOTSTRAP_SERVERS = ['kafka-service:9092']


def get_kafka_conn_object(timeout=3000):
    i = 0
    while True:
        time.sleep(5)
        if i > timeout:
            logger.info("---> Timeout! <---")
            sys.exit()
        try:
            return KafkaConsumer('location',
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False,
                                 value_deserializer=lambda m:
                                 json.loads(m.decode('utf-8')),
                                 bootstrap_servers=BOOTSTRAP_SERVERS)
        except Exception:
            logger.info("... Waiting for Kafka ...")
            i += 1


def serve():
    logger.log(logging.INFO, 'Begin initialization.')
    consumer = get_kafka_conn_object()
    for message in consumer:
        logger.info("get a new message")
        logger.info(message)
    logging.log(logging.INFO, 'Kafka Consumer has been successfully started.')


if __name__ == "__main__":
    serve()
