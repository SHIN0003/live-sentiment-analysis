import nltk

import db
from consumer import return_consume_obj
from sentiment import analyze
from producer import return_producer_obj
import time
import json

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
    producer = return_producer_obj()
    
    
    print(consumer)
    for message in consumer:
        try:
            resmessage = message.value.decode("utf-8")
            reskey = message.key.decode("utf-8")
            print(reskey, resmessage)
            res = analyze(resmessage)
            producer.send("processed-data",value=json.dumps(res, indent=2).encode('utf-8'), key=message.key)
        except Exception as e:
            print(f"Error sending message: {e}")
            time.sleep(5)


if __name__ == "__main__":
    nltk.download("vader_lexicon")
    main()
