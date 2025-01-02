import json
import time 
import nltk
from datetime import datetime
import db
from consumer import return_consume_obj
from producer import return_producer_obj
from sentiment import analyze


def main():
    # print("Waiting for messages...")
    # conn = db.return_connection()
    # print("Connected to the database!")
    # cursor = conn.cursor()
    # # Example query
    # cursor.execute("SELECT version();")
    # db_version = cursor.fetchone()
    # print("PostgreSQL version:", db_version)
    # db.close_connection(conn, cursor)

    consumer = return_consume_obj()
    producer = return_producer_obj()


    for message in consumer:
        try:
            resmsg = message.value.decode("utf-8")
            # reskey = message.key.decode("utf-8")
            sentiment = analyze(resmsg)
            print(sentiment)
            timestamp = datetime.fromtimestamp(message.timestamp)
            #Now I can figure out a way to set up the schema in order to send the data in
            res_obj = {
                resmsg,
                sentiment,
                timestamp
            }
            # producer.send(
            #     "processed-data",
            #     value=json.dumps(res_obj, indent=2).encode("utf-8"),
            #     key=message.key,
            # )
        except Exception as e:
            print(f"Error sending message: {e}")
            time.sleep(5)


if __name__ == "__main__":
    nltk.download("vader_lexicon")
    main()
