# Reddit Sentiment Analysis Pipeline

## Overview
This project extracts Reddit posts from specified subreddits, performs sentiment analysis using NLTK's VADER, and ingests data into a PostgreSQL database. The pipeline is designed to run automatically once certain data thresholds (50,000 records) are met, ensuring we only process and ingest significant batches of data.

## Project Structure
```bash
reddit-sentiment-analysis/
├── analysis/
│   ├── sentiment_analysis.py      # Script for performing sentiment analysis on extracted data
├── config/
│   ├── config.py                  # Python module to load credentials from config.ini
│   ├── config.ini  # Excluded from version control
├── data/
│   ├── raw/
│   │   ├── live_data.csv          # Raw data extracted from Reddit
│   ├── processed/
│   │   ├── live_data_with_sentiment.csv  # Data after sentiment analysis
├── db/
│   ├── conditional_ingest.py      # Script to ingest data into PostgreSQL only after a threshold is reached
├── etl/
│   ├── reddit_extraction.py       # Script for extracting Reddit data (e.g., using PRAW)
├── visualization/                 # Dashboards visualizations
├── project-setup.ps1              # PowerShell script to create folder structure
├── etl_pipeline.py                # Main pipeline script orchestrating extraction → analysis → ingestion
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation and usage instructions
```


## Prerequisites
1. **Python 3.9+**
2. **PostgreSQL** (local or hosted, e.g., Azure Database for PostgreSQL)
3. **Reddit API Credentials** (client_id, client_secret, user_agent, etc.)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/YourUsername/reddit-sentiment-analysis.git
   cd reddit-sentiment-analysis

2. **Install Dependencies:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt

3. **Configure Credentials:**
   - Open `config/config.ini` (excluded from Git by default).
   - Add your Reddit API keys and PostgreSQL details under `[reddit]` and `[postgres]`.
   - Example:
     ```ini
     [reddit]
     client_id = YOUR_REDDIT_CLIENT_ID
     client_secret = YOUR_REDDIT_CLIENT_SECRET
     user_agent = YOUR_APP_NAME
     username = YOUR_REDDIT_USERNAME
     password = YOUR_REDDIT_PASSWORD

     [postgres]
     db_user = YOUR_DB_USER
     db_password = YOUR_DB_PASSWORD
     db_host = localhost
     db_port = 5432
     db_name = reddit_sentiment
     ```

## Usage

### One-Shot Pipeline (Threshold-Based)
This project includes three scripts that collectively form a pipeline:

1. **reddit_extraction.py**  
   - Extracts Reddit posts in batches (e.g., 100 at a time) until 50,000 total records are reached (or however you configure it).
   - Saves them to `data/raw/live_data.csv`.

2. **sentiment_analysis.py**  
   - Checks if `live_data.csv` meets a threshold (e.g., 50,000 records).
   - If so, performs sentiment analysis using VADER and saves the result to `data/processed/live_data_with_sentiment.csv`.

3. **conditional_ingest.py**  
   - Checks if `live_data_with_sentiment.csv` has at least the threshold number of records.
   - If so, ingests data into the `posts` table in PostgreSQL.

#### Running the Pipeline
- **Manual (step-by-step)**:
  ```bash
  python etl/reddit_extraction.py
  python analysis/sentiment_analysis.py
  python db/conditional_ingest.py

### Automated
You can create a single script (e.g., `etl_pipeline.py`) that runs these in sequence, or schedule them via cron, Task Scheduler, or Azure Pipelines to run automatically.

### Visualization
Once data is in PostgreSQL, connect Tableau, Power BI, or any BI tool to your database for interactive dashboards.

**Common visuals:**
- Time Series of sentiment scores
- Distribution of sentiment (positive/negative/neutral)
- Correlation between sentiment and engagement (scores/comments)

### Scheduling
You can schedule the scripts or the combined pipeline in various ways:

- **Azure Pipelines / Data Factory**: Ideal if your infrastructure is already in Azure.
- **Cron (Linux/macOS)**:
  ```bash
  crontab -e
  # Example: run every day at 1 AM
  0 1 * * * /usr/bin/python /path/to/etl_pipeline.py >> /path/to/pipeline.log 2>&1

