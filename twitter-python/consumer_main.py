import nltk

import db
from consumer import return_consume_obj
from sentiment import analyze


def main():
    print("Waiting for messages...")
    conn = db.return_connection()
    print("Connected to the database!")
    cursor = conn.cursor()
    # Example query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("PostgreSQL version:", db_version)
    db.close_connection(conn, cursor)

    consumer = return_consume_obj()
    print(consumer)
    for message in consumer:
        print(message.key.decode("utf-8"))
        print(analyze(message.value.decode("utf-8")))


if __name__ == "__main__":
    nltk.download("vader_lexicon")
    main()
