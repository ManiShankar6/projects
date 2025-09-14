import sys
import os
import time
import pandas as pd
from sqlalchemy import create_engine, text

# Ensure the project root is in the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def create_tables(engine):
    """
    Creates the posts table in the database if it does not exist.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS posts (
        post_id TEXT PRIMARY KEY,
        title TEXT,
        selftext TEXT,
        created_utc TIMESTAMP,
        score INTEGER,
        num_comments INTEGER,
        subreddit TEXT,
        sentiment_score FLOAT,
        sentiment_label TEXT
    );
    """
    with engine.connect() as connection:
        connection.execute(text(create_table_query))
        connection.commit()
    print("Table 'posts' ensured in the database.")

def ingest_data(csv_file="data/processed/live_data_with_sentiment.csv"):
    """
    Reads the processed CSV and inserts its data into the PostgreSQL database,
    but only when the CSV contains at least 50,000 records.
    """
    if not os.path.exists(csv_file):
        print(f"CSV file {csv_file} does not exist. Exiting.")
        return False

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    total_records = len(df)
    print(f"Current CSV record count: {total_records}")

    if total_records >= 50000:
        print("Threshold reached (50,000 records). Updating the database...")
        engine = create_engine(DATABASE_URL)
        create_tables(engine)  # Ensure table exists
        try:
            df.to_sql("posts", engine, if_exists="replace", index=False, method="multi")
            print(f"Ingested {total_records} records into the 'posts' table.")
        except Exception as e:
            print(f"Error during data ingestion: {e}")
            return False
        return True
    else:
        print("Not enough records to update the database. Exiting without updating.")
        return False

def main():
    csv_file = "data/processed/live_data_with_sentiment.csv"
    
    # Check for the record threshold once
    if ingest_data(csv_file):
        print("Ingestion complete. Exiting pipeline.")
    else:
        print("CSV does not meet the required threshold. Exiting pipeline.")

if __name__ == "__main__":
    main()
