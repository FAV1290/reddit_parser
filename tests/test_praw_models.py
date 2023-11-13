import praw


from app.praw_models_creator import create_read_only_reddit_instance, create_subreddit_instance


def test_create_read_only_reddit_instance() -> None:
    reddit_instance = create_read_only_reddit_instance()
    assert isinstance(reddit_instance, praw.Reddit)
    assert not reddit_instance.username_available('Stunning-Decision245')
    reddit_instance.redditor('Stunning-Decision245').id == 'vhofyen9'


def test_create_subreddit_instance() -> None:
    reddit_instance = create_read_only_reddit_instance()
    subreddit_instance = create_subreddit_instance(reddit_instance, 'reddit')
    assert subreddit_instance.id == '5s5qbl'
    assert subreddit_instance.created_utc == 1643751441.0
