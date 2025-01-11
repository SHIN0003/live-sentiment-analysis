import psycopg2
from utils import config
# Connection details


def return_connection():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=config.DATABASE,
            user=config.USER,
            password=config.PASSWORD,
            host=config.DB_HOST,
            port=config.DB_PORT
        )
        return conn

    except Exception as e:
        print("Error connecting to the database:", e)

def close_connection(conn, cursor):
    cursor.close()
    conn.close()