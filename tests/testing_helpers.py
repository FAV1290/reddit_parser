import requests


def parse_control_title() -> str | None:
    reddit_response = requests.get('https://www.reddit.com/r/reddit/new/')
    if reddit_response.status_code == 200:
        start_point = reddit_response.text.find('post-title="') + 12
        end_point = reddit_response.text.find('"', start_point)
        return reddit_response.text[start_point:end_point].strip()
    else:
        return None
