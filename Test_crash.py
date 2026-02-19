#!/usr/bin/env python
# coding: utf-8

# In[3]:


import psycopg2
from datetime import datetime, timedelta

NEON_URI = os.getenv("NEON_URI")
def simulate_crisis():
    conn = psycopg2.connect(NEON_URI)
    cur = conn.cursor()
    
    # 1. Insert "Healthy" data for 90 minutes ago (Previous Hour)
    # We'll insert 10 rows of $1,000 each = $10,000
    prev_hour = datetime.now() - timedelta(minutes=90)
    for _ in range(10):
        cur.execute("""
            INSERT INTO ceo_sales_data (transaction_date, revenue, units_sold) 
            VALUES (%s, %s, %s)
        """, (prev_hour, 1000.00, 10))

    # 2. Insert "Crash" data for right now (Current Hour)
    # We'll insert only $50 total revenue
    current_hour = datetime.now()
    cur.execute("""
        INSERT INTO ceo_sales_data (transaction_date, revenue, units_sold) 
        VALUES (%s, %s, %s)
    """, (current_hour, 50.00, 1))

    conn.commit()
    cur.close()
    conn.close()
    print("Crisis data injected: Previous Hour ($10,000) vs Current Hour ($50)")

if __name__ == "__main__":
    simulate_crisis()


# In[ ]:




