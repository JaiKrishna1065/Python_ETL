from logger import get_logger

logger = get_logger()

def transform_data(df):
    # Normalize column names
    df.columns = (
        df.columns
        .astype(str)
        .str.replace("\n", " ")
        .str.strip()
        .str.upper()
    )

    print("COLUMNS AFTER NORMALIZATION:", df.columns)

    # Remove unwanted columns
    df = df.loc[:, ~df.columns.str.contains("UNNAMED|S.NO", case=False)]

    # Detect TEAM ID column
    team_id_col = next(
        (col for col in df.columns if "TEAM" in col and "ID" in col),
        None
    )

    if not team_id_col:
        raise ValueError("TEAM ID column not found")

    # Drop NULL team_id
    before = len(df)
    df = df.dropna(subset=[team_id_col])
    logger.info(f"Dropped {before - len(df)} rows due to NULL team_id")

    # Detect TEAM LEAD column
    lead_col = next(
        (col for col in df.columns if "LEAD" in col),
        None
    )

    if lead_col:
        null_leads = df[lead_col].isna().sum()
        df[lead_col] = df[lead_col].fillna("Unknown")
        logger.info(f"Filled {null_leads} NULL team lead names")

    # Detect EMAIL column (THIS WAS MISSING)
    email_col = next(
        (col for col in df.columns if "EMAIL" in col),
        None
    )

    # Remove duplicate team IDs
    before_dup = len(df)
    df = df.drop_duplicates(subset=[team_id_col], keep="first")
    logger.info(f"Removed {before_dup - len(df)} duplicate team_ids")

    # Rename to FINAL enforced schema
    rename_map = {
        team_id_col: "team_id"
    }
    if lead_col:
        rename_map[lead_col] = "team_lead_name"
    if email_col:
        rename_map[email_col] = "email"

    df = df.rename(columns=rename_map)

    logger.info(f"Final row count: {len(df)}")
    logger.info("Transformation completed successfully")

    return df