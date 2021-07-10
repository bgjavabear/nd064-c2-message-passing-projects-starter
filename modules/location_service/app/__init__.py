from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from kafka import KafkaConsumer
import threading
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LocationService")

db = SQLAlchemy()

BOOTSTRAP_SERVERS = ['kafka-service:9092']


def register_kafka_listener(topic, listener):
    def poll():
        # Initialize consumer Instance
        consumer = KafkaConsumer(topic, bootstrap_servers=BOOTSTRAP_SERVERS)

        consumer.poll(timeout_ms=6000)
        for msg in consumer:
            listener(msg)
        t1 = threading.Thread(target=poll)
        t1.start()


def kafka_listener(data):
    print(data)


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)
    register_kafka_listener('location', kafka_listener)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
