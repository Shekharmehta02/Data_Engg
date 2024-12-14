import pymysql
import pyodbc
import logging

# Fetch data from MySQL
def fetch_mysql_data(mysql_conn, source_table):
    cursor = mysql_conn.cursor()
    query = f"SELECT * FROM {source_table}"
    cursor.execute(query)
    data = cursor.fetchall()  # This returns a list of tuples
    cursor.close()
    return data

# Dump data into MSSQL
def dump_to_mssql(mssql_conn, target_table, data):
    cursor = mssql_conn.cursor()
    for row in data:
        placeholders = ', '.join(['?' for _ in range(len(row))])
        insert_query = f"INSERT INTO {target_table} VALUES ({placeholders})"
        cursor.execute(insert_query, row)  # Row is passed as a tuple
    mssql_conn.commit()
    cursor.close()

# Migrate data from MySQL to MSSQL for a specific table
def migrate_data(mysql_conn, mssql_conn, source_table, target_table):
    # Fetch data from MySQL
    data = fetch_mysql_data(mysql_conn, source_table)

    # Dump data into MSSQL
    dump_to_mssql(mssql_conn, target_table, data)

