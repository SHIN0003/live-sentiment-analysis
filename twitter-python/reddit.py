import time

import praw

from producer import return_producer_obj
from utils import config


def fetch_comments(subreddits):
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent=config.REDDIT_USER_AGENT,
    )
    producer = return_producer_obj()
    # either have multiple forloops? I dont think thatll work as itll block, so make a variable that concats
    # all sub reddits that we want to send
    for comment in reddit.subreddit("+".join(subreddits)).stream.comments():
        # Feed this into producer? yes
        # try catch loop here
        # print(comment.body)
        try:
            producer.send("reddit-comments", value=comment.body.encode("utf-8"), key=comment.subreddit.display_name.encode("utf-8"))
            print("comment sent")
        except Exception as e:
            print(f"Error sending message: {e}")
            time.sleep(5)
