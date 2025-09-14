# Create the folder structure for the project

# Data folders
New-Item -ItemType Directory -Force -Path "data\raw"
New-Item -ItemType Directory -Force -Path "data\processed"

# Database folders and files
New-Item -ItemType Directory -Force -Path "db\migrations"
New-Item -ItemType File -Force -Path "db\schema.sql" | Out-Null

# ETL folder and sample file
New-Item -ItemType Directory -Force -Path "etl"
New-Item -ItemType File -Force -Path "etl\reddit_extraction.py" | Out-Null

# Analysis folder and sample file
New-Item -ItemType Directory -Force -Path "analysis"
New-Item -ItemType File -Force -Path "analysis\sentiment_analysis.py" | Out-Null

# Visualization folder and subfolder
New-Item -ItemType Directory -Force -Path "visualization\dashboard_setup"

# CI/CD folder and sample file
New-Item -ItemType Directory -Force -Path "ci_cd"
New-Item -ItemType File -Force -Path "ci_cd\github_actions.yml" | Out-Null

# Root-level files
New-Item -ItemType File -Force -Path ".gitignore" | Out-Null
New-Item -ItemType File -Force -Path "requirements.txt" | Out-Null
New-Item -ItemType File -Force -Path "README.md" | Out-Null

Write-Output "Project structure created successfully."
