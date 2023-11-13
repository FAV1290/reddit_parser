import tqdm
import time
import logging
import collections
from praw.models import Submission, Subreddit
from praw.models.reddit.comment import Comment
from praw.models.reddit.more import MoreComments


from app.constants import (
    CUT_OFF_TIME_DAYS, SECONDS_IN_DAY, SLEEP_TIME_SEC,
    LOGGING_FORMAT, LOGFILE_FILEPATH, PROGRESS_BAR_FORMAT
)


logging.basicConfig(filename=LOGFILE_FILEPATH, level=logging.INFO, format=LOGGING_FORMAT)


def create_submissions_list(
    subreddit: Subreddit,
    cut_off_time_days: int = CUT_OFF_TIME_DAYS,
) -> list[Submission]:
    submissions: list[Submission] = []
    cut_off_time_sec = cut_off_time_days * SECONDS_IN_DAY
    for submission in subreddit.new(limit=None):
        if time.time() - submission.created_utc > cut_off_time_sec:
            return submissions
        else:
            submissions.append(submission)
    return submissions


def create_submission_authors_list(submissions_list: list[Submission]) -> list[tuple[str, int]]:
    submission_authors = [
        submission.author.name for submission in submissions_list if submission.author is not None]
    submission_authors_list = collections.Counter(submission_authors)
    return submission_authors_list.most_common()


def flatten_comments_list(
    comments_list: list[Comment | MoreComments],
) -> list[Comment]:
    flat_comments_list = []
    for comment in comments_list:
        if isinstance(comment, Comment):
            flat_comments_list.append(comment)
        else:
            time.sleep(SLEEP_TIME_SEC)
            flat_comments_list = flat_comments_list + flatten_comments_list(comment.comments())
    return flat_comments_list


def create_comment_authors_list(submissions: list[Submission]) -> list[tuple[str, int]]:
    comment_authors, comments_parsed, submission_num = [], 0, 0
    submissions_tqdm = tqdm.tqdm(submissions, ncols=80, bar_format=PROGRESS_BAR_FORMAT)
    logging.info(f'\n{"-"*50}\nComments parsing starts\n{"-"*50}')
    for submission in submissions_tqdm:
        submission_num += 1
        logging.info(f'Parsing submission #{submission_num}: {submission.title}')
        comments_list = flatten_comments_list(submission.comments.list())
        for comment in comments_list:
            if comment.author:
                comment_authors.append(comment.author)
        parsed_submission_report = [
            f'{len(comment_authors) - comments_parsed} comment(s) parsed ',
            f'({len(comment_authors)} comment(s) total)\n'
        ]
        logging.info(''.join(parsed_submission_report))
        comments_parsed = len(comment_authors)
    comment_authors_counter = collections.Counter(comment_authors)
    return comment_authors_counter.most_common()
