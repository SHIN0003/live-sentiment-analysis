from kafka import KafkaProducer
import time

print("Starting script...")

try:
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    print("Connected to Kafka!")
    producer.send('test-topic', b'Test message')
    print("Message sent to Kafka.")
    # while True:
    #     time.sleep(60)  # Replace long sleep with periodic checks
    #     print("Still running...")
    while True:
        time.sleep(1)
        print("Still running...")
except Exception as e:
    print(f"Error: {e}")
