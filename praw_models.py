import praw
import praw.models


from constants import CLIENT_ID, CLIENT_SECRET, USER_AGENT


def create_read_only_reddit_instance() -> praw.Reddit:
    reddit_instance = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
    )
    return reddit_instance


def create_subreddit_instance(
    reddit_instance: praw.Reddit,
    subreddit_name: str
) -> praw.models.Subreddit:
    return reddit_instance.subreddit(subreddit_name)
