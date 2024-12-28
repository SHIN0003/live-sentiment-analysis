import producer
import reddit


def main():
    # Get Kafka broker URL from environment variable
    reddit.fetch_comments()


if __name__ == "__main__":
    main()
