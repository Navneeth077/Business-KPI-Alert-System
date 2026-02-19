#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install psycopg2-binary pandas python-dotenv


# In[3]:


import psycopg2
import random
import time
from datetime import datetime

# Connection setup 
DB_URI = os.getenv("NEON_URI")
def insert_mock_transaction():
    conn = psycopg2.connect(DB_URI)
    cur = conn.cursor()
    
    # Generate random business data
    revenue = round(random.uniform(100, 5000), 2)
    costs = revenue * random.uniform(0.4, 0.7) # 40-70% margin
    segments = ['Enterprise', 'SMB', 'Startup']
    
    cur.execute("""
        INSERT INTO ceo_sales_data (revenue, customer_segment, operating_costs, units_sold)
        VALUES (%s, %s, %s, %s)
    """, (revenue, random.choice(segments), costs, random.randint(1, 50)))
    
    conn.commit()
    cur.close()
    conn.close()
    print(f"Transaction injected at {datetime.now()}")

# Run this every 10 seconds to simulate a live business
while True:
    insert_mock_transaction()
    time.sleep(10)


# In[ ]:




