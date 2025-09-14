<<<<<<< HEAD
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

=======
# 🧠 Mani Shankar's Project Portfolio

Welcome to my **Data Science & Data Engineering Projects** repository!  
This repo serves as a collection of hands-on projects I’ve worked on across different domains including **cloud computing**, **data analytics**, **data engineering**, **machine learning**, and **software development**.

Each subfolder contains a self-contained project with code, data (if applicable), and documentation.

---

## 📂 Projects Overview

### 🎬 [Movie Analysis Using AWS & Tableau](./movie-analysis-aws-tableau)

A cloud-based data engineering project that leverages **AWS services** (S3, Glue, Athena, IAM) and **Tableau** for real-time movie data visualization.

- **Cloud Tools:** AWS S3, Glue, Athena, IAM
- **Visualization:** Tableau (connected to Athena)
- **Skills:** ETL, PySpark, Cloud Storage, SQL Analytics, Dashboarding

📄 [Project ReadMe](./movie-analysis-aws-tableau/README.md)

---

### 🎵 [Spotify Song Popularity Analysis](./spotify-popularity-analysis)

A data analysis project that investigates the **key audio features** influencing song popularity using **Spotify API** and regression techniques.

- **Tech:** Python, Spotipy, Pandas, Matplotlib, Seaborn
- **Key Analysis:** Correlation, Regression, Data Visualization
- **Dataset:** 18,000 tracks (Jan 2023 – Present)

📄 [Project ReadMe](./spotify-popularity-analysis/README.md)

---

### 🧠 [Parkinson's Disease Prediction System](./parkinsons-disease-prediction)

A machine learning and GUI-based project to predict **Parkinson's disease** using biomedical voice features. Includes a **Tkinter-based desktop app**.

- **Tech:** Python, Scikit-learn, Tkinter, XGBoost, SVM
- **Features:** Real-time predictions, full-screen GUI, CSV input
- **Use Case:** Healthcare and Medical Decision Support

📄 [Project ReadMe](./parkinsons-disease-prediction/README.md)

---

### 🔎 [Reddit Sentiment Analysis Using Python & PostgreSQL](./reddit-sentiment-analysis)

An end-to-end data engineering and analytics project that extracts Reddit posts using the **Reddit API**, performs **VADER sentiment analysis** (NLTK), and ingests the results into **PostgreSQL** for real-time dashboards.

- **Tech Stack:** Python, PRAW (Reddit API), NLTK (VADER), PostgreSQL, Tableau/Power BI
- **Focus Areas:** ETL, Scheduling (cron/Azure), CI/CD, Sentiment Analysis, Data Visualization
- **Dataset:** 50,000+ Reddit posts from chosen subreddits

📄 [Project ReadMe](./reddit-sentiment-analysis/README.md)

---

## 📁 Repo Structure
```bash
Projects:.
├───movie-analysis-aws-tableau
│   ├───data
│   ├───images
│   └───notebooks
├───parkinsons-disease-prediction
│   ├───assets
│   ├───data
│   ├───notebooks
│   └───src
├───reddit-sentiment-analysis
│   ├───analysis
│   ├───config
│   │   └───__pycache__
│   ├───data
│   │   ├───processed
│   │   └───raw
│   ├───db
│   │   └───migrations
│   ├───etl
│   └───visualization
│       └───dashboard_setup
└───spotify-popularity-analysis
```

---

## 🚀 How to Use This Repo

**1. Clone this repository:**
```bash
git clone https://github.com/ManiShankar6/Projects.git
cd Projects
```

**2. Navigate into any project folder to explore its content:**

```bash
cd movie-analysis-aws-tableau
```

**3. Follow the instructions in each project's README.md.**
>>>>>>> e2124ab212b41166b3a94bd3dee012c7cfe8e5e9
