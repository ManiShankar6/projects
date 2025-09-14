import subprocess


def run_extraction():
    print("Starting Reddit extraction...")
    subprocess.run(["python", "etl/reddit_extraction.py"], check=True)
    print("Reddit extraction completed.\n")

def run_sentiment():
    print("Starting sentiment analysis...")
    subprocess.run(["python", "analysis/sentiment_analysis.py"], check=True)
    print("Sentiment analysis completed.\n")

def run_ingestion():
    print("Starting conditional ingestion...")
    subprocess.run(["python", "db/conditional_ingest.py"], check=True)
    print("Conditional ingestion completed.\n")

def main():
    try:
        print("Pipeline execution started.\n")
        run_extraction()
        print("Extraction stage finished. Proceeding to sentiment analysis...\n")
        run_sentiment()
        print("Sentiment analysis stage finished. Proceeding to data ingestion...\n")
        run_ingestion()
        print("Pipeline completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during pipeline execution: {e}")

if __name__ == "__main__":
    main()
