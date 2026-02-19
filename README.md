# 🚀 CEO Dashboard Bot: Automated KPI Alert System

An end-to-end data pipeline that monitors business-critical KPIs in real-time and proactively alerts stakeholders via Slack when anomalies occur.

---

## 📈 Business Case
In many organizations, decision-makers rely on static dashboards that require manual checking. This project shifts from **reactive** to **proactive** analysis. Instead of waiting for a human to find a revenue drop, this bot identifies statistical anomalies and pushes the insight directly into the executive's workflow.

## 🛠️ Tech Stack
- **Database:** Neon PostgreSQL (Serverless Cloud)
- **Language:** Python (Psycopg2, Pandas, Requests)
- **CI/CD / Automation:** GitHub Actions
- **Infrastructure:** GitHub Secrets (Security/Environment Variables)
- **Communication:** Slack API (Block Kit)

## 🏗️ Architecture
1. **Data Ingestion:** A Python feeder script simulates live transactional data flowing into the Neon cloud database.
2. **Analytical Logic:** An hourly monitor script performs a batch-comparison SQL query to measure "Revenue Velocity."
3. **Threshold Engine:** If the current batch revenue shows a drop of **>20%** compared to the previous period, an alert is triggered.
4. **Professional Alerting:** High-priority alerts are delivered via Slack using formatted "Block Kit" cards for readability.



## 🛡️ Security Features
- **Secret Management:** Sensitive credentials (DB URIs, Webhooks) are stored in GitHub Secrets and injected at runtime via Environment Variables.
- **Defensive Programming:** Implementation of `try-except` blocks and zero-division handling to ensure 100% pipeline uptime.

## 🚀 Key Technical Challenges Solved
- **Timezone Synchronization:** Resolved DNS and timezone drift issues between local environments and cloud instances by refactoring SQL logic to use ID-based batching.
- **API Reliability:** Implemented status-code verification for Slack Webhooks to ensure message delivery.

## 📂 Project Structure
- `monitor.py`: The "Brain" - connects to DB, runs SQL, and sends Slack alerts.
- `test_crash.py`: Stress-test script to simulate revenue anomalies.
- `data_feeder.py`: Simulates live business activity.
- `.github/workflows/`: Automation recipes for 24/7 monitoring.
