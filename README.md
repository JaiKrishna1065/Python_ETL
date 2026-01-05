Python ETL Pipeline (Excel → MySQL)

📌 Overview
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Python and MySQL.
The pipeline processes messy Excel data, cleans and standardizes it, and loads analytics-ready data into MySQL.

🔧 Tech Stack
- Python
- Pandas
- MySQL
- Git & GitHub

📂 Project Structure
Python_ETL/
- extract.py      → Reads Excel data
- transform.py   → Cleans, validates, and deduplicates data
- load.py        → Loads cleaned data into MySQL
- logger.py      → Logs ETL metrics
- main.py        → Pipeline orchestration
- .gitignore     → Prevents secrets & data leaks

🔄 ETL Flow
Excel File → Python (Extract & Transform) → MySQL (Load)

✅ Key Features
- Handles non-standard Excel headers
- Dynamic schema detection
- Null value handling
- Duplicate removal using primary keys
- Idempotent ETL (safe to re-run)
- Logging for monitoring

▶️ How to Run
1. Configure MySQL credentials in `db_config.py`
2. Create table in MySQL
3. Run:
   python main.py

📊 Sample SQL Queries
- Total teams
- Duplicate validation
- Team lead analytics

🚀 Outcome
Clean, reliable, and reusable data ready for analytics.
