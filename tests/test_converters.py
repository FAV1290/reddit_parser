import praw.models


from testing_helpers import parse_control_title
from converters import create_submissions_list, create_submission_authors_list, flatten_comments_list
from praw_models import create_read_only_reddit_instance, create_subreddit_instance


def test_create_submissions_list() -> None:
    reddit_instance = create_read_only_reddit_instance()
    subreddit_instance = create_subreddit_instance(reddit_instance, 'reddit')
    submissions_list = create_submissions_list(subreddit_instance)
    control_title = parse_control_title()
    assert isinstance(submissions_list, list)
    assert isinstance(submissions_list[0], praw.models.Submission)
    if control_title is not None:
        assert submissions_list[0].title == control_title


def test_create_submission_authors_list() -> None:
    reddit_instance = create_read_only_reddit_instance()
    ids_list = ['16ryhv9', '16gx179', '16tqihd']
    submissions_list = [praw.models.Submission(reddit_instance, id=id) for id in ids_list]
    authors_list = create_submission_authors_list(submissions_list)
    assert authors_list[0][0] == 'werksquan'
    assert authors_list[1][0] == 'JabroniRevanchism'
    assert authors_list[2][0] == 'snoo-tuh'
