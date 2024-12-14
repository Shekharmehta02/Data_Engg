import pyodbc
import json
import logging
from data_migration.migration_pac.path_calculator import get_mssql_config_path


# Connect with mssql db
def load_mssql_config():
    config_file = get_mssql_config_path()
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        logging.info("MSSQL configuration loaded successfully.")
        return config
    except Exception as e:
        logging.error(f"Error loading MSSQL configuration: {e}")
        raise

# Connect with mssql db
def connect_mssql(config):
    try:
        connection = pyodbc.connect(
            driver='{ODBC Driver 17 for SQL Server}',
            server=config['server'],
            trusted_connection='yes',  # Using Windows Authentication
            database=config['database']
        )
        logging.info("MSSQL DB connection made successfully.")
        return connection
    except Exception as e:
        logging.error(f"Error connecting to MSSQL: {e}")
        raise
