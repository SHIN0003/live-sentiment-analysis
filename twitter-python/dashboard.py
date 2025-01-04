import streamlit as st
import pandas as pd
import numpy as np
import psycopg2
import db

st.title("Reddit Sentiment Analysis")
st.title("testing live")

conn = st.connection("postgresql", type="sql")

