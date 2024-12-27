import os
from dotenv import load_dotenv
load_dotenv()

# Kafka Configuration
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL', 'kafka:9092')
KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC', 'reddit_comments')

# Reddit API Configuration
REDDIT_CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.environ.get('REDDIT_USER_AGENT', 'reddit-kafka-producer')

# Subreddit to Monitor
SUBREDDIT = os.environ.get('SUBREDDIT', 'technology')
