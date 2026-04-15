MODE = "live"  # or "synthetic"
import requests
import psycopg2
import time
import os
from dotenv import load_dotenv

load_dotenv()
DB_URI = os.getenv("NEON_URI")

conn = psycopg2.connect(DB_URI)
cur = conn.cursor()

def fetch_crypto():
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_24hr_vol": "true"
    }
    
    data = requests.get(url, params=params).json()
    
    price = data["bitcoin"]["usd"]
    volume = data["bitcoin"]["usd_24h_vol"]
    
    return price, volume

def insert_live_data():
    try:
        price, volume = fetch_crypto()
        
        # Convert to "business metrics"
        revenue = price * 0.01  # simulate trading revenue
        costs = revenue * 0.6
        
        cur.execute("""
            INSERT INTO ceo_sales_data 
            (revenue, customer_segment, operating_costs, units_sold)
            VALUES (%s, %s, %s, %s)
        """, (revenue, "Crypto", costs, int(volume % 50)))
        
        conn.commit()
        print("Live data inserted")

    except Exception as e:
        print("Error:", e)

while True:
    insert_live_data()
    time.sleep(60)  # avoid rate limits




