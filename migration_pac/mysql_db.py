import pymysql
import json
import logging

from data_migration.migration_pac.path_calculator import get_mysql_config_path

# Fetch mysql db config from respective config file
def load_mysql_config():
    config_file = get_mysql_config_path()
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        logging.info("MySQL configuration loaded successfully.")
        return config
    except Exception as e:
        logging.error(f"Error loading MySQL configuration: {e}")
        raise

# Connect with mysql db
def connect_mysql(config):
    try:
        connection = pymysql.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        logging.info("MySQL DB connection made successfully.")
        return connection
    except Exception as e:
        logging.error(f"Error connecting to MySQL: {e}")
        raise
