import os
import praw.models


from praw_models import create_read_only_reddit_instance
from export_to_txt import (
    save_submissions_titles_to_txt_file,
    save_top_authors_to_txt_file,
    save_most_active_redditors_to_txt_file,
)


def test_save_submissions_titles_to_txt_file() -> None:
    reddit_instance = create_read_only_reddit_instance()
    ids_list = ['16ryhv9', '16gx179', '16tqihd']
    submissions_list = [praw.models.Submission(reddit_instance, id=id) for id in ids_list]
    save_submissions_titles_to_txt_file(submissions_list, 'test.txt')
    with open('test.txt', 'r', encoding='utf-8') as file_handler:
        titles_list = file_handler.readlines()
    for index in range(len(titles_list)):
        assert f'{index + 1}. {submissions_list[index].title}\n' == titles_list[index]
    os.remove('test.txt')


def test_save_top_authors_to_txt_file() -> None:
    top_authors_list = [('author1', 10), ('author2', 5), ('author3', 2)]
    index_to_line_map = {
        0: f'1. author1 (10 thread(s) started)\n',
        1: f'2. author2 (5 thread(s) started)\n',
        2: f'3. author3 (2 thread(s) started)\n',
    }
    save_top_authors_to_txt_file(top_authors_list, 'test.txt')
    with open('test.txt', 'r', encoding='utf-8') as file_handler:
        control_list = file_handler.readlines()
    for index, correct_answer in enumerate(control_list):
        assert index_to_line_map[index] == correct_answer
    os.remove('test.txt')


def test_save_most_active_redditors_to_txt_file() -> None:
    active_redditors_list = [('redditor1', 10), ('redditor2', 5), ('redditor3', 2)]
    index_to_line_map = {
        0: f'1. redditor1 (10 comment(s) written)\n',
        1: f'2. redditor2 (5 comment(s) written)\n',
        2: f'3. redditor3 (2 comment(s) written)\n',
    }
    save_most_active_redditors_to_txt_file(active_redditors_list, 'test.txt')
    with open('test.txt', 'r', encoding='utf-8') as file_handler:
        control_list = file_handler.readlines()
    for index, correct_answer in enumerate(control_list):
        assert index_to_line_map[index] == correct_answer
    os.remove('test.txt')
