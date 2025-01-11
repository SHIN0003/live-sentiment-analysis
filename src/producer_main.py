import producer
import reddit


def main():
    # Get Kafka broker URL from environment variable
    subreddits = {"technology", "tech", "realtech", "startups", "techolitics"}
    reddit.fetch_comments_live(subreddits)
    # reddit.fetch_top_comments(subreddits)


if __name__ == "__main__":
    main()
