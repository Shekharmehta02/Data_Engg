import os

def get_mysql_config_path():
    return os.path.join(os.getcwd(), 'mysql_config.json')

def get_mssql_config_path():
    return os.path.join(os.getcwd(), 'mssql_config.json')

