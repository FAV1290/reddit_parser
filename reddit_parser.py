import praw
import praw.models
import prawcore
import time


from praw_models import create_read_only_reddit_instance, create_subreddit_instance
from converters import (
    create_submissions_list,
    create_submission_authors_list,
    create_comment_authors_list,
)
from console_output import print_reports_slices, print_execution_time
from export_to_txt import save_reports_to_txt_files


def check_subreddit_name(reddit_instance: praw.Reddit, user_input: str | None) -> bool:
    try:
        assert reddit_instance.subreddit(user_input).id
        return True
    except (
        prawcore.exceptions.NotFound,
        prawcore.exceptions.BadRequest,
        prawcore.exceptions.Redirect,
        AssertionError,
        ValueError,
    ):
        return False


def fetch_valid_subreddit_name(reddit_instance: praw.Reddit) -> str:
    while True:
        user_input = input('Please enter the name of preferred subreddit: ').strip().lower()
        if check_subreddit_name(reddit_instance, user_input):
            return user_input    
        else:
            print("Subreddit not found. Let's try again...")
    

def calculate_execution_time(*args: float) -> float | None:
    if args == () or len(args) % 2 == 1:
        return None
    execution_time = 0.0
    for index, timestamp in enumerate(args):
        if index % 2 == 1:
            execution_time += timestamp
        else:
            execution_time -= timestamp
    return float(execution_time)


def prepare_target_submissions_list() -> list[praw.models.Submission]:
    reddit_instance = create_read_only_reddit_instance()
    subreddit_name = fetch_valid_subreddit_name(reddit_instance)
    subreddit_instance = create_subreddit_instance(reddit_instance, subreddit_name)
    target_submissions = create_submissions_list(subreddit_instance)
    return target_submissions


def main() -> None:
    target_submissions = prepare_target_submissions_list()
    start_timestamp = time.time()
    submission_authors = create_submission_authors_list(target_submissions)
    print(f"{len(target_submissions)} submissions found. Comments parsing is about to start...")
    comment_authors = create_comment_authors_list(target_submissions)
    save_reports_to_txt_files(target_submissions, submission_authors, comment_authors)
    print_reports_slices(target_submissions, submission_authors, comment_authors, 10)
    print_execution_time(calculate_execution_time(start_timestamp, time.time()))


if __name__ == '__main__':
    main()
