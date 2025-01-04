import streamlit as st
import db  # Your custom db module
import time


def fetch_all():
    conn = db.return_connection()  # Fetches connection using environment variables
    st.write("Connected to the database!")
    query = """
    SELECT * FROM processed_data;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()



def fetch_new_data(last_id):
    conn = db.return_connection()
    cursor = conn.cursor()

    # Query to fetch all new rows with id > last_fetched_id
    query = """
    SELECT *
    FROM processed_data
    WHERE id > %s
    ORDER BY id DESC;
    """
    cursor.execute(query, (last_id,))
    new_data = cursor.fetchall()
    
    if new_data:
        latest_id = new_data[0][0]
    else:
        latest_id = last_id
        
    db.close_connection(conn, cursor)
    return new_data, latest_id



     
st.title("Reddit Sentiment Analysis")
st.write("Testing live connection to the database...")


# Connect to the database
try:
    st.session_state
    if "last_fetched_id" not in st.session_state:
        st.session_state["last_fetched_id"] = 0
        base = fetch_all()
        st.session_state['base'] = [base]
    else:
        latest, latest_id = fetch_new_data(st.session_state["last_fetched_id"])
        st.session_state["last_fetched_id"] = latest_id
        if latest:
            st.session_state['latest_data'] = latest
            st.session_state['base'].append(latest)
        
    if 'base' in st.session_state:
        st.session_state['base']
    if 'latest_data' in st.session_state:
        st.session_state['latest_data']
    
    #live data
    
    
    
    
    # time.sleep(5)  # Wait for 5 seconds
    # st.rerun()  # Refresh the Streamlit app to fetch new data
    
except Exception as e:
    st.error(f"Failed to connect to the database: {e}")
    