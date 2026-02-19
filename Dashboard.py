#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import psycopg2
import pandas as pd
import os

# 1. Setup Page
st.set_page_config(page_title="CEO Real-Time Radar", layout="wide")
st.title("📈 CEO Executive Radar")
st.write("Live data feed from Neon PostgreSQL")

# 2. Connect to Data
def get_data():
    conn = psycopg2.connect(os.getenv("NEON_URI"))
    query = "SELECT * FROM ceo_sales_data ORDER BY id DESC LIMIT 100"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

try:
    df = get_data()

    # 3. Create Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${df['revenue'].sum():,.2f}")
    col2.metric("Avg Transaction", f"${df['revenue'].mean():,.2f}")
    col3.metric("Total Units", int(df['units_sold'].sum()))

    # 4. Create a Chart
    st.subheader("Revenue Trend (Latest Transactions)")
    st.line_chart(df.set_index('id')['revenue'])

    # 5. Show Raw Data
    st.subheader("Recent Logs")
    st.dataframe(df)

except Exception as e:
    st.error(f"Waiting for database connection... {e}")


# In[ ]:




