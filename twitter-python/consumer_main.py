import json
import time 
import nltk
import datetime
import db
from consumer import return_consume_obj
from producer import return_producer_obj
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
    

    consumer = return_consume_obj()
    producer = return_producer_obj()


    for message in consumer:
        try:
            resmsg = message.value.decode("utf-8")
            reskey = message.key.decode("utf-8")
            sentiment = analyze(resmsg)
            timestamp = datetime.datetime.fromtimestamp(int(message.timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(
                """
                INSERT INTO processed_data (subreddit, analysis_result, original_message, timestamp)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    reskey,
                    json.dumps(sentiment),
                    resmsg,
                    timestamp,
                )
            )
            conn.commit()
        except Exception as e:
            print(f"Error sending message: {e}")
            time.sleep(5)
    db.close_connection(conn, cursor)

if __name__ == "__main__":
    nltk.download("vader_lexicon")
    main()
