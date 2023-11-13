from praw import Reddit
from praw.models import Subreddit


from app.constants import CLIENT_ID, CLIENT_SECRET, USER_AGENT


def create_read_only_reddit_instance() -> Reddit:
    return Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)


def create_subreddit_instance(reddit_instance: Reddit, subreddit_name: str) -> Subreddit:
    return reddit_instance.subreddit(subreddit_name)
