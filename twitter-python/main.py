import producer
import reddit


def main():
    # Get Kafka broker URL from environment variable
    subreddits = {"viktormains", "Eldenring"}
    reddit.fetch_comments(subreddits)


if __name__ == "__main__":
    main()
