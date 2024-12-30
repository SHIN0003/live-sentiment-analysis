import nltk
from kafka import KafkaConsumer
import db
from sentiment import analyze


# Connect to Kafka
# Try catch loop maybe here
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
    conn = db.return_connection()
    print("Connected to the database!")
    cursor = conn.cursor()
    # Example query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("PostgreSQL version:", db_version)
    db.close_connection(conn, cursor)
    for message in consumer:
        print(analyze(message.value.decode("utf-8")))


nltk.download("vader_lexicon")
consume()
