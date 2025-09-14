import configparser
import os

def load_config(config_file='config/config.ini'):
    config = configparser.ConfigParser()
    
    # Check if config file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found. Please create it with your Reddit credentials.")
    
    config.read(config_file)
    return config

# Load configuration on module import if desired
config = load_config()

# Access credentials
reddit_config = config['reddit']
CLIENT_ID = reddit_config.get('client_id')
CLIENT_SECRET = reddit_config.get('client_secret')
USER_AGENT = reddit_config.get('user_agent')
USERNAME = reddit_config.get('username')
PASSWORD = reddit_config.get('password')

# PostgreSQL credentials
postgres_config = config['postgresql']
DB_USER = postgres_config.get('db_user')
DB_PASSWORD = postgres_config.get('db_password')
DB_HOST = postgres_config.get('db_host')
DB_PORT = postgres_config.get('db_port')
DB_NAME = postgres_config.get('db_name')