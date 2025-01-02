import os
from dotenv import load_dotenv
load_dotenv()

# Kafka Configuration
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL', 'kafka:9092')
KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC', 'reddit_comments')

# Reddit API Configuration
REDDIT_CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.environ.get('REDDIT_SECRET')
REDDIT_USER_AGENT = os.environ.get('REDDIT_USER_AGENT', 'reddit-kafka-producer')

# Subreddit to Monitor
SUBREDDIT = os.environ.get('SUBREDDIT', 'technology')

DATABASE=os.environ.get('POSTGRES_DB')
USER=os.environ.get('POSTGRES_USER')
PASSWORD=os.environ.get('POSTGRES_PASSWORD')
DB_PORT=os.environ.get('DB_PORT')
DB_HOST=os.environ.get('DB_HOST')