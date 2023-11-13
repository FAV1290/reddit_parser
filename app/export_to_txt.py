from praw.models import Submission


from app.constants import (
    SUBMISSION_TITLES_FILEPATH,
    SUBMISSION_AUTHORS_FILEPATH,
    COMMENT_AUTHORS_FILEPATH,
)


def save_submissions_titles_to_txt_file(submissions: list[Submission], filepath: str) -> None:
    with open(filepath, 'w', encoding='utf-8') as file_handler:
        for number, submission in enumerate(submissions, start=1):
            file_handler.write(f'{number}. {submission.title}\n')


def save_top_authors_to_txt_file(top_authors_list: list[tuple[str, int]], filepath: str) -> None:
    rank = 0
    with open(filepath, 'w', encoding='utf-8') as file_handler:
        for author, submissions_posted in top_authors_list:
            rank += 1
            file_handler.write(f'{rank}. {author} ({submissions_posted} thread(s) started)\n')


def save_most_active_users_to_txt_file(most_active: list[tuple[str, int]], filepath: str) -> None:
    rank = 0
    with open(filepath, 'w', encoding='utf-8') as file_handler:
        for redditor, comments_written in most_active:
            rank += 1
            file_handler.write(f'{rank}. {redditor} ({comments_written} comment(s) written)\n')


def export_reports_to_txt(
    submissions_list: list[Submission],
    submissions_authors_list: list[tuple[str, int]],
    comments_authors_list: list[tuple[str, int]],
) -> None:
    save_submissions_titles_to_txt_file(submissions_list, SUBMISSION_TITLES_FILEPATH)
    save_top_authors_to_txt_file(submissions_authors_list, SUBMISSION_AUTHORS_FILEPATH)
    save_most_active_users_to_txt_file(comments_authors_list, COMMENT_AUTHORS_FILEPATH)
