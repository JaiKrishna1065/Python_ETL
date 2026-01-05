import mysql.connector
from db_config import DB_CONFIG
from logger import get_logger

logger = get_logger()

def load_data(df):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    insert_query = """
        INSERT INTO cleaned_data (team_id, email, team_lead_name)
        VALUES (%s, %s, %s) AS new
        ON DUPLICATE KEY UPDATE
            email = new.email,
            team_lead_name = new.team_lead_name
    """

    rows_loaded = 0
    for _, row in df.iterrows():
        cursor.execute(
            insert_query,
            (row["team_id"], row["email"], row["team_lead_name"])
        )
        rows_loaded += 1

    conn.commit()
    cursor.close()
    conn.close()

    logger.info(f"Loaded {rows_loaded} rows into cleaned_data")
    print(f"Loaded {rows_loaded} rows into cleaned_data successfully")
