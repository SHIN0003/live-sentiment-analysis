# from producer.reddit_fetcher import fetch_reddit_comments

import os
import time

from kafka import KafkaProducer


def start_producer():
    kafka_broker = os.getenv("KAFKA_BROKER_URL", "kafka:9092")

    print(f"Connecting to Kafka at {kafka_broker}...")

    while True:  # Keep trying to connect
        try:
            producer = KafkaProducer(bootstrap_servers=[kafka_broker])
            print("Connected to Kafka!")

            # Main loop
            while True:
                try:
                    producer.send("test-topic", b"Test message")
                    print("Message sent to Kafka")
                    time.sleep(5)  # Wait 5 seconds between messages
                except Exception as e:
                    print(f"Error sending message: {e}")
                    time.sleep(5)  # Wait before retrying

        except Exception as e:
            print(f"Error connecting to Kafka: {e}")
            time.sleep(5)  # Wait before retrying connection
