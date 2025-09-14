import sys
import os
import time
import datetime
import pandas as pd
import praw


# Ensure the project root is in the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

def extract_100_posts(subreddit_name="news", limit=100):
    """
    Connects to Reddit using PRAW and extracts 100 posts from the specified subreddit.
    Returns a list of dictionaries with post details.
    """
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=USERNAME,
        password=PASSWORD
    )
    
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for submission in subreddit.hot(limit=limit):
        posts.append({
            "post_id": submission.id,
            "title": submission.title,
            "selftext": submission.selftext,
            "created_utc": datetime.datetime.fromtimestamp(submission.created_utc),
            "score": submission.score,
            "num_comments": submission.num_comments,
            "subreddit": submission.subreddit.display_name
        })
        
    return posts

def save_posts_to_csv(posts, filename="data/raw/live_data.csv"):
    """
    Saves the aggregated posts to a CSV file.
    Overwrites the CSV on each call.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(posts)
    df.to_csv(filename, index=False)
    print(f"Saved {len(posts)} posts to {filename}")

def one_shot_extraction(subreddit_name="news"):
    """
    Continuously extracts posts until 50,000 records are collected.
    Pauses for 3 minutes every time a multiple of 5,000 records is reached.
    Once 50,000 records are collected, the final CSV is saved and the script exits.
    """
    all_posts = []
    
    while len(all_posts) < 50000:
        new_posts = extract_100_posts(subreddit_name, limit=100)
        all_posts.extend(new_posts)
        current_count = len(all_posts)
        print(f"Extracted 100 posts. Total posts collected so far: {current_count}")
        save_posts_to_csv(all_posts)
        
        # Wait 5 seconds between each extraction call
        time.sleep(5)
        
        # If a multiple of 5,000 is reached (and not zero), pause for 3 minutes
        if current_count >= 5000 and current_count % 5000 == 0:
            print(f"Reached {current_count} records. Pausing for 3 minutes...")
            time.sleep(180)  # Pause for 3 minutes

    print("Reached 50,000 records. Final CSV is ready. Exiting extraction process.")

if __name__ == "__main__":
    one_shot_extraction("news")
