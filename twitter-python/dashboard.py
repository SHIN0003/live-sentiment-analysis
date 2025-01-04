import streamlit as st
import pandas as pd
import numpy as np
import psycopg2
import db

st.title("Reddit Sentiment Analysis")
st.title("testing live")

st.write("Waiting for messages...")
conn = db.return_connection()
st.write("Connected to the database!")
cursor = conn.cursor()
# Example query
cursor.execute("SELECT version();")
db_version = cursor.fetchone()
st.write("PostgreSQL version:", db_version)
db.close_connection(conn, cursor)
