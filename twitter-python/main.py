import producer
import reddit


def main():
    # Get Kafka broker URL from environment variable
    reddit.fetch_comments()
    producer.start_producer()


if __name__ == "__main__":
    main()
