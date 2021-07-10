from kafka import KafkaProducer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LocationService")

producer = KafkaProducer(bootstrap_servers=['kafka-service:9092'])


def send_location(location_data):
    logging.info(location_data)
    producer.send('location', location_data)
    producer.flush()
