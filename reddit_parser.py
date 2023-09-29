import praw
import praw.models
import prawcore
import time


from praw_models import create_read_only_reddit_instance, create_subreddit_instance
from data_lists import (
    create_submissions_list,
    create_submission_authors_list,
    create_comment_authors_list,
)
from console_output import print_reports_slices
from export_to_txt import save_reports_to_txt_files


def fetch_valid_subreddit_name(reddit_instance: praw.Reddit) -> str:
    while True:
        user_input = input('Please enter the name of preferred subreddit: ').strip().lower()
        try:
            assert reddit_instance.subreddit(user_input).id
        except (
            prawcore.exceptions.NotFound,
            prawcore.exceptions.BadRequest,
            prawcore.exceptions.Redirect,
            AssertionError,
            ValueError,
        ):
            print("Subreddit not found. Let's try again...")
            continue
        return user_input


def main() -> None:
    
    reddit_instance = create_read_only_reddit_instance()
    subreddit_name = fetch_valid_subreddit_name(reddit_instance)
    timestamp_one = time.time()
    subreddit_instance = create_subreddit_instance(reddit_instance, subreddit_name)
    target_submissions = create_submissions_list(subreddit_instance)
    submission_authors = create_submission_authors_list(target_submissions)
    print(f"{len(target_submissions)} submissions found. Starting to parse comments from them...")
    comment_authors = create_comment_authors_list(target_submissions, prints_on=True)
    timestamp_two = time.time()
    input('All submissions are parsed. Press Enter to continue...')
    timestamp_three = time.time()
    save_reports_to_txt_files(target_submissions, submission_authors, comment_authors)
    print_reports_slices(target_submissions, submission_authors, comment_authors, 10)
    print()
    timestamp_four = time.time()
    execution_time = float(timestamp_two - timestamp_one + timestamp_four - timestamp_three)
    print(f'\nScript execution time: {"{:.2f}".format(execution_time)} second(s)')


if __name__ == '__main__':
    main()
