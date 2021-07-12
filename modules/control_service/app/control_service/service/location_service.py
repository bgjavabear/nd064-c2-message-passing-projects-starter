from kafka import KafkaProducer
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LocationService")

producer = KafkaProducer(bootstrap_servers=['kafka-service:9092'])


def send_location(location_data):
    """
     Pushes location data to kafka broker under the 'location' topic
    """
    logger.info(location_data)
    producer.send('location', json.dumps(location_data).encode('utf-8'))
    producer.flush()
