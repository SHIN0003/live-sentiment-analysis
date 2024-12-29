import nltk
from kafka import KafkaConsumer

from sentiment import analyze


# Connect to Kafka
def consume(subreddits=[]):
    consumer = KafkaConsumer(
        "reddit-comments",  # The topic name
        bootstrap_servers="kafka:9092",  # Kafka broker URL (match your Docker network setup)
        auto_offset_reset="earliest",  # Start reading from the earliest message
        enable_auto_commit=True,  # Commit offsets automatically
        group_id="test-group",  # Consumer group ID
    )

    print("Waiting for messages...")
    # Consume messages
    for message in consumer:
        print(analyze(message.value.decode("utf-8")))


nltk.download("vader_lexicon")
consume()
