import dotenv
import os


dotenv.load_dotenv()


CLIENT_ID = os.environ['REDDIT_APP_CLIENT_ID']
CLIENT_SECRET = os.environ['REDDIT_APP_CLIENT_SECRET']
USER_AGENT = os.environ['REDDIT_APP_USER_AGENT']
CUT_OFF_TIME_DAYS = 3
SECONDS_IN_DAY = 86400
CLEAR_SCREEN_COMMANDS_MAP = {
    'nt': 'cls',
    'posix': 'clear',
}
SUBMISSION_TITLES_FILEPATH = 'submission_titles.txt'
SUBMISSION_AUTHORS_FILEPATH = 'submission_authors.txt'
COMMENT_AUTHORS_FILEPATH = 'comment_authors.txt'
SLEEP_TIME_SEC = 0.8
LOGGING_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'
LOGFILE_FILEPATH = 'reddit_parser.log'
PROGRESS_BAR_FORMAT = '{desc}: {percentage:3.0f}%|{bar} {n_fmt}/{total_fmt}'
