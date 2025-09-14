-- Create the "posts" table to store Reddit post data and sentiment analysis results

CREATE TABLE IF NOT EXISTS posts (
    post_id TEXT PRIMARY KEY,         -- Unique identifier for each Reddit post
    title TEXT,                       -- Post title
    selftext TEXT,                    -- Post content/body of the post
    created_utc TIMESTAMP,            -- Timestamp when the post was created (converted from UNIX time)
    score INTEGER,                    -- Upvote score of the post
    num_comments INTEGER,             -- Number of comments on the post
    subreddit TEXT,                   -- Name of the subreddit from which the post was extracted
    sentiment_score FLOAT,            -- Compound sentiment score (e.g., from VADER)
    sentiment_label TEXT              -- Sentiment label (e.g., positive, negative, neutral)
);
