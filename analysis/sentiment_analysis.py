import sys
import os
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure the project root is in the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def perform_sentiment_analysis(df):
    """
    Uses NLTK's VADER to compute sentiment scores for each record.
    Combines 'title' and 'selftext' for analysis, and assigns a sentiment label.
    """
    # Ensure the VADER lexicon is available
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
    
    def analyze_text(row):
        # Combine title and selftext (if selftext is not null)
        text = f"{row['title']} {row['selftext']}" if pd.notnull(row['selftext']) else row['title']
        score = sia.polarity_scores(text)['compound']
        if score >= 0.05:
            sentiment = "positive"
        elif score <= -0.05:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        return pd.Series([score, sentiment])
    
    df[['sentiment_score', 'sentiment_label']] = df.apply(analyze_text, axis=1)
    return df

def main():
    input_file = os.path.join("data", "raw", "live_data.csv")
    output_file = os.path.join("data", "processed", "live_data_with_sentiment.csv")
    
    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist. Exiting.")
        return
    
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    total_records = len(df)
    print(f"Current raw CSV record count: {total_records}")
    
    if total_records >= 50000:
        print("Threshold reached (50,000 records). Performing sentiment analysis...")
        df = perform_sentiment_analysis(df)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df.to_csv(output_file, index=False)
        print(f"Processed data with sentiment scores saved to {output_file}")
    else:
        print("Not enough records to process. Exiting without changes.")

if __name__ == "__main__":
    main()
