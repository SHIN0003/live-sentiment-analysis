from kafka import KafkaConsumer

# Connect to Kafka
consumer = KafkaConsumer(
    'test-topic',  # The topic name
    bootstrap_servers='kafka:9092',  # Kafka broker URL (match your Docker network setup)
    auto_offset_reset='earliest',  # Start reading from the earliest message
    enable_auto_commit=True,       # Commit offsets automatically
    group_id='test-group'          # Consumer group ID
)

print("Waiting for messages...")
# Consume messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
