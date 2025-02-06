from praw import Reddit
from data_extraction.utils.constants import CLIENT_KEY, SECRET_KEY, REDDIT_AGENT

def extract_data() -> Reddit :
    reddit = Reddit(
        client_id=CLIENT_KEY,
        client_secret=SECRET_KEY,
        user_agent=REDDIT_AGENT,
    )
    return reddit
def load_data(reddit: Reddit) -> None:
    print(reddit.read_only)