#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import psycopg2
import requests
import json

# Pulling from environment variables (Secrets)
NEON_URI = os.getenv("NEON_URI")
SLACK_URL = os.getenv("SLACK_URL")

def send_alert(curr, prev, pct):
    """Sends a professionally formatted Block Kit message to Slack."""
    color = "#ff0000" if pct <= -20 else "#2eb886" # Red for alert, Green for growth
    emoji = "🚨" if pct <= -20 else "📈"
    
    payload = {
        "attachments": [
            {
                "color": color,
                "blocks": [
                    {
                        "type": "header",
                        "text": {"type": "plain_text", "text": f"{emoji} Executive KPI Report"}
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": f"*Current Revenue:*\n${curr:,.2f}"},
                            {"type": "mrkdwn", "text": f"*Previous Revenue:*\n${prev:,.2f}"}
                        ]
                    },
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": f"*Performance Change:* `{pct:.2f}%`"}
                    },
                    {
                        "type": "context",
                        "elements": [{"type": "mrkdwn", "text": "Source: Neon Cloud Live Stream"}]
                    }
                ]
            }
        ]
    }
    requests.post(SLACK_URL, json=payload)

def run_kpi_check():
    try:
        # 1. Connect and Fetch
        conn = psycopg2.connect(NEON_URI)
        cur = conn.cursor()
        cur.execute("SELECT revenue FROM ceo_sales_data ORDER BY id DESC LIMIT 2;")
        rows = cur.fetchall()
        conn.close()

        if len(rows) < 2:
            print("Not enough data to calculate performance.")
            return

        # 2. Calculate Stats
        current_val = float(rows[0][0])
        prev_val = float(rows[1][0])
        
        # Avoid division by zero
        if prev_val == 0: 
            performance = 0
        else:
            performance = ((current_val - prev_val) / prev_val) * 100

        # 3. Decision Logic: Send alert if performance is a drop of 20% or more
        # OR just send it now to see your beautiful new formatting!
        send_alert(current_val, prev_val, performance)
        print(f"Success! Performance ({performance:.2f}%) sent to Slack.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_kpi_check()


# In[ ]:




