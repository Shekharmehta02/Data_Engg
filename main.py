import logging
from migration_pac.mysql_db import load_mysql_config, connect_mysql
from migration_pac.mssql_db import load_mssql_config, connect_mssql
from migration_pac.logger import setup_logging
from migration_pac.migration import migrate_data

def main():
    # Setup logging
    setup_logging()

    # Load configurations
    mysql_config = load_mysql_config()
    mssql_config = load_mssql_config()

    # Connect to MySQL and MSSQL
    mysql_conn = connect_mysql(mysql_config)
    mssql_conn = connect_mssql(mssql_config)

    logging.info("MySQL and MSSQL connections established successfully.")

    source_tables = ['product_data', 'customer_data']
    target_tables = ['product_data_up', 'customer_data_up']

    # Migrate data for each table pair
    for source_table, target_table in zip(source_tables, target_tables):
        migrate_data(mysql_conn, mssql_conn, source_table, target_table)

    # Close connections
    mysql_conn.close()
    mssql_conn.close()

    logging.info("Migration completed and database connections closed successfully.")

if __name__ == "__main__":
    main()
