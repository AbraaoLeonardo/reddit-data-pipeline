from praw import Reddit
from data_extraction.utils.constants import CLIENT_KEY, SECRET_KEY, REDDIT_AGENT, POSTS_KEY

def extract_data() -> Reddit :
    reddit = Reddit(
        client_id=CLIENT_KEY,
        client_secret=SECRET_KEY,
        user_agent=REDDIT_AGENT,
    )
    return reddit

def load_data(reddit: Reddit,time_filter='day', limit=None) -> None:
    subreddit = reddit.subreddit('dataengineering')
    posts = subreddit.top(time_filter=time_filter, limit=limit)
    posts_list = []
    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POSTS_KEY}
        posts_list.append(post)
    
    for posts in posts_list:
        print(posts)
        print("")