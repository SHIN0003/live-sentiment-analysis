import time

import praw

from producer import return_producer_obj
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

    producer = return_producer_obj()
    # either have multiple forloops? I dont think thatll work as itll block, so make a variable that concats
    # all sub reddits that we want to send
    for comment in reddit.subreddit("all").stream.comments():
        # Feed this into producer? yes
        # try catch loop here
        print(comment.body)
        try:
            producer.send("test-topic", comment.body.encode("utf-8"))
            print("comment sent")
        except Exception as e:
            print(f"Error sending message: {e}")
            time.sleep(5)
