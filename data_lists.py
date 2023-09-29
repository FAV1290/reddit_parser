import time
import praw.models
import praw.models.reddit.more
import praw.models.reddit.comment
import collections
import tqdm


from constants import CUT_OFF_TIME_DAYS, SECONDS_IN_DAY


def create_submissions_list(
    subreddit: praw.models.Subreddit,
    cut_off_time_days: int = CUT_OFF_TIME_DAYS,
) -> list[praw.models.Submission]:
    submissions_list: list[praw.models.Submission] = []
    cut_off_time_sec = cut_off_time_days * SECONDS_IN_DAY
    for submission in subreddit.new(limit=None):
        if time.time() - submission.created_utc > cut_off_time_sec:
            return submissions_list
        else:
            submissions_list.append(submission)
    return submissions_list


def create_submission_authors_list(
    submissions_list: list[praw.models.Submission],
) -> list[tuple[str, int]]:
    submission_authors = [submission.author.name for submission in submissions_list]
    submission_authors_list = collections.Counter(submission_authors)
    return submission_authors_list.most_common()


def flatten_comments_list(
    comments_list: list[praw.models.reddit.comment.Comment | praw.models.reddit.more.MoreComments],
    progress_bar: bool = False,
) -> list[praw.models.reddit.comment.Comment]:
    flat_comments_list = []
    comments_list_tqdm = tqdm.tqdm(
        comments_list,
        ncols=80,
        disable=not progress_bar,
        bar_format='{desc}: {percentage:3.0f}%|{bar} {n_fmt}/{total_fmt}'
    )
    for comment in comments_list_tqdm:
        if type(comment) == praw.models.reddit.comment.Comment:
            flat_comments_list.append(comment)
        else:
            time.sleep(1)
            flat_comments_list = flat_comments_list + flatten_comments_list(comment.comments())
    return flat_comments_list
        

def create_comment_authors_list(
    submissions_list: list[praw.models.Submission],
    prints_on: bool = True,
) -> list[tuple[str, int]]:
    comment_authors = []
    comments_parsed = 0
    for num, submission in enumerate(submissions_list, start=1):
        if prints_on:
            print(f'Parsing submission #{num}: {submission.title}')
        comments_list = flatten_comments_list(submission.comments.list(), progress_bar=prints_on)
        for comment in comments_list:
            if comment.author is not None:
                comment_authors.append(comment.author)
        if prints_on:
            parsed_submission_report = [
                f'{len(comment_authors) - comments_parsed} comment(s) parsed from submission ',
                f'({len(comment_authors)} comment(s) total)\n'
            ]
            print(''.join(parsed_submission_report))
        comments_parsed = len(comment_authors)
    comment_authors_counter = collections.Counter(comment_authors)
    return comment_authors_counter.most_common()
