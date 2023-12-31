import os
from praw.models import Submission


from app.constants import (
    CLEAR_SCREEN_COMMANDS_MAP,
    SUBMISSION_TITLES_FILEPATH,
    SUBMISSION_AUTHORS_FILEPATH,
    COMMENT_AUTHORS_FILEPATH,
)


def clear_screen() -> None:
    os.system(CLEAR_SCREEN_COMMANDS_MAP.get(os.name, ''))


def print_execution_time(execution_time: float | None) -> None:
    if not execution_time:
        print("Can't calculate execution time due incorrect arguments or their odd quantity")
    else:
        print(f'Script execution time: {"{:.2f}".format(execution_time)} second(s)')


def print_submissions_titles(submissions: list[Submission], limit: int | None = None) -> None:
    try:
        subreddit_name = submissions[0].subreddit.display_name
    except IndexError:
        print('Sorry, but recent submissions in subreddit were not found...')
        return
    submissions_report = [
        f'{len(submissions)} submissions were found in {subreddit_name} subreddit.',
        f'Titles of {limit} are shown here, full list in {SUBMISSION_TITLES_FILEPATH}:\n',
    ]
    if not limit or limit > len(submissions):
        limit = len(submissions)
    for number, submission in enumerate(submissions[:limit], start=1):
        submissions_report.append(f'{number}. {submission.title}')
    print('\n'.join(submissions_report))


def print_top_authors(top_authors: list[tuple[str, int]], limit: int | None = None) -> None:
    if not len(top_authors):
        print('No authors found...')
        return
    if not limit or limit > len(top_authors):
        limit = len(top_authors)
    rank = 0
    authors_report = [
        f'Submissions were started by {len(top_authors)} unique authors.',
        f'{limit} most efficient are shown here, full list in {SUBMISSION_AUTHORS_FILEPATH}:\n',
    ]
    for author, submissions_posted in top_authors[:limit]:
        rank += 1
        authors_report.append(f'{rank}. {author} ({submissions_posted} submission(s) started)')
    print('\n'.join(authors_report))


def print_most_active_redditors(
    comment_authors: list[tuple[str, int]],
    limit: int | None = None
) -> None:
    rank = 0
    comments_total = sum(map(lambda x: x[1], comment_authors))
    comments_report = [
        f'{comments_total} comments were written by {len(comment_authors)} unique authors.',
        f'{limit} most active of them are shown here, full list in {COMMENT_AUTHORS_FILEPATH}:\n',
    ]
    if not len(comment_authors):
        print('No comments found...')
        return
    if not limit or limit > len(comment_authors):
        limit = len(comment_authors)
    for redditor, comments_written in comment_authors[:limit]:
        rank += 1
        comments_report.append(f'{rank}. {redditor} ({comments_written} comment(s) written)')
    print('\n'.join(comments_report))


def print_reports_slices(
    submissions: list[Submission],
    submission_authors: list[tuple[str, int]],
    comment_authors: list[tuple[str, int]],
    slice_size: int,
) -> None:
    clear_screen()
    print_submissions_titles(submissions, limit=slice_size)
    print(f'\n{"-" * 50}\n')
    print_top_authors(submission_authors, limit=slice_size)
    print(f'\n{"-" * 50}\n')
    print_most_active_redditors(comment_authors, limit=slice_size)
    print(f'\n{"-" * 50}\n')
