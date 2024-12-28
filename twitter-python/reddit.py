import praw

from utils import config


def fetch_comments():
    print("Entered reddit.py")

    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent=config.REDDIT_USER_AGENT,
    )

    # for submission in reddit.subreddit("viktormains").new(limit=25):
    #     arr = submission.comments.list()
    #     for comment in arr:
    #         print(comment.body)
    for comment in reddit.subreddit("all").stream.comments():
        # Feed this into producer? yes
        print(comment.body)
