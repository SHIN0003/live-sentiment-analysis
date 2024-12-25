from kafka import KafkaProducer
import time

print("Starting script...")

try:
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    print("Connected to Kafka!")
    producer.send('test-topic', b'Test message')
    print("Message sent to Kafka.")
    time.sleep(100000)
except Exception as e:
    print(f"Error: {e}")
