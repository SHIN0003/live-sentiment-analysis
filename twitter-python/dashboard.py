import streamlit as st
import db  # Your custom db module

st.title("Reddit Sentiment Analysis")
st.write("Testing live connection to the database...")

# Connect to the database
try:
    conn = db.return_connection()  # Fetches connection using environment variables
    st.write("Connected to the database!")
    
    cursor = conn.cursor()
    
    # Example query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    st.write("PostgreSQL version:", db_version)
    
except Exception as e:
    st.error(f"Failed to connect to the database: {e}")
    
finally:
    # Ensure the connection and cursor are closed properly
    db.close_connection(conn, cursor)
    st.write("Database connection closed.")
