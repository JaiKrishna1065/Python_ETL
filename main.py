from extract import extract_data
from transform import transform_data
from load import load_data
from logger import get_logger

logger = get_logger()

FILE_PATH = r"D:\Python-Learning\Python_ETL\SHORTLISTED TEAMS_Copy.xlsx"

if __name__ == "__main__":
    logger.info("ETL pipeline started")
    raw_df = extract_data(FILE_PATH)
    clean_df = transform_data(raw_df)
    load_data(clean_df)

    print("ETL pipeline completed successfully")
    print("Before Cleaning : ",raw_df.shape)
    print("After Cleaning : ",clean_df.shape)

    logger.info("ETL pipeline completed")
    print(clean_df.head())

