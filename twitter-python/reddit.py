import praw

from utils import config


def test():
    print("Entered reddit.py")
    print(config.REDDIT_CLIENT_ID,config.REDDIT_CLIENT_SECRET,config.REDDIT_USER_AGENT)
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent=config.REDDIT_USER_AGENT,
    )

    print(reddit.read_only)
