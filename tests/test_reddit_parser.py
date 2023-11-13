from app.praw_models_creator import create_read_only_reddit_instance
from app.reddit_parser import check_subreddit_name, calculate_execution_time


def test_check_subreddit_name() -> None:
    reddit_instance = create_read_only_reddit_instance()
    input_to_check_result_map = {
        '': False,
        '0': False,
        'afsofsjsfilksjsifkjs': False,
        'all': False,
        'python': True,
        'gaming': True,
        'webdev': True,
    }
    for input, result in input_to_check_result_map.items():
        assert check_subreddit_name(reddit_instance, input) == result


def test_calculate_execution_time() -> None:
    timestamps_to_execution_time_map = {
        (): None,
        (10.0,): None,
        (3.0, 10.0): 7.0,
        (3.0, 10.0, 15.0): None,
        (3.0, 10.0, 15.0, 16.0): 8.0,
        (10.0, 3.0): -7.0,
    }
    for timestamps, result in timestamps_to_execution_time_map.items():
        assert calculate_execution_time(*timestamps) == result
