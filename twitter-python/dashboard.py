import streamlit as st
import db  # Your custom db module
import pandas as pd

# -------------------------------------------------------------------
# 1. Database helpers
# -------------------------------------------------------------------
def fetch_all():
    """
    Fetch all rows from the processed_data table.
    Returns a list of tuples.
    """
    conn = db.return_connection()
    st.write("Connected to the database!")
    query = "SELECT * FROM processed_data;"
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close_connection(conn, cursor)
    return data


def fetch_new_data(last_id):
    """
    Fetch new rows from the processed_data table, where id > last_id,
    returning both the new rows and the latest row ID found.
    """
    conn = db.return_connection()
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM processed_data
    WHERE id > %s
    ORDER BY id ASC;
    """  
    cursor.execute(query, (last_id,))
    new_data = cursor.fetchall()
    
    if new_data:
        # Since results are ordered by id ASC, the last item is the max ID
        latest_id = new_data[-1][0]
    else:
        latest_id = last_id

    db.close_connection(conn, cursor)
    return new_data, latest_id


# -------------------------------------------------------------------
# 2. DataFrame helpers
# -------------------------------------------------------------------
def rows_to_df(rows):
    """
    Convert rows (list of tuples) from the DB into a flattened DataFrame.
    Assumes each tuple structure is: 
        (id, category, sentiment_dict, text, timestamp)
    where sentiment_dict is a Python dict with neg, neu, pos, compound.
    """
    flattened_data = []
    for row in rows:
        # row[2] is presumably the sentiment dict: {"neg": x, "neu": y, ... }
        sentiment_dict = row[2] if isinstance(row[2], dict) else {}
        flattened_data.append({
            "id": row[0],
            "category": row[1],
            "neg": sentiment_dict.get("neg", None),
            "neu": sentiment_dict.get("neu", None),
            "pos": sentiment_dict.get("pos", None),
            "compound": sentiment_dict.get("compound", None),
            "text": row[3],
            "timestamp": row[4]
        })
    return pd.DataFrame(flattened_data)


# -------------------------------------------------------------------
# 3. Main Streamlit app logic
# -------------------------------------------------------------------
st.title("Reddit Sentiment Analysis")
st.write("Testing live connection to the database...")

try:
    # Initialize session_state variables if not present
    if "df" not in st.session_state:
        st.session_state["df"] = pd.DataFrame()        # Will hold all data
    if "last_fetched_id" not in st.session_state:
        st.session_state["last_fetched_id"] = 0
    
    # If no data in the session yet, fetch everything from scratch
    if st.session_state["df"].empty:
        all_rows = fetch_all()
        st.session_state["df"] = rows_to_df(all_rows)
        # Update the last_fetched_id to the max ID we got
        if not st.session_state["df"].empty:
            st.session_state["last_fetched_id"] = st.session_state["df"]["id"].max()
    else:
        # Fetch only new data
        new_rows, latest_id = fetch_new_data(st.session_state["last_fetched_id"])
        if new_rows:
            new_df = rows_to_df(new_rows)
            # Append to our existing DataFrame
            st.session_state["df"] = pd.concat([st.session_state["df"], new_df], ignore_index=True)
            st.session_state["last_fetched_id"] = latest_id

    # Display the entire DataFrame stored in session_state
    st.write(st.session_state["df"])

    # If you want periodic refresh:
    # import time
    # time.sleep(5)  # Wait 5 seconds
    # st.rerun()  # Refresh the Streamlit app

except Exception as e:
    st.error(f"Failed to connect to the database: {e}")
