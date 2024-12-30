from kafka import KafkaConsumer



# Connect to Kafka
# Try catch loop maybe here
def return_consume_obj(subreddits=[]):
    consumer = KafkaConsumer(
        "reddit-comments",  # The topic name
        bootstrap_servers="kafka:9092",  # Kafka broker URL (match your Docker network setup)
        auto_offset_reset="earliest",  # Start reading from the earliest message
        enable_auto_commit=True,  # Commit offsets automatically
        group_id="test-group",  # Consumer group ID
    )

    return consumer
    

