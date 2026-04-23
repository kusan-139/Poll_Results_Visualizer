
import os
import pandas as pd

# Resolve paths relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, 'data', 'poll_data.csv')
CLEAN_PATH = os.path.join(BASE_DIR, 'data', 'cleaned_poll_data.csv')


def main():
    # Check if raw data exists
    if not os.path.exists(RAW_PATH):
        print(f"[ERROR] Raw data not found at: {RAW_PATH}")
        return

    df = pd.read_csv(RAW_PATH)
    print(f"[INFO] Loaded {len(df)} rows from poll_data.csv")

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    print(f"[INFO] Removed {before - len(df)} duplicate rows")

    # Handle missing values
    df = df.dropna(subset=['Preferred Tool', 'Satisfaction (1-5)'])

    # Standardize categorical responses
    df['Preferred Tool'] = df['Preferred Tool'].str.strip().str.title()
    # Fix known title-case issues
    df['Preferred Tool'] = df['Preferred Tool'].replace({'Power Bi': 'Power BI'})

    # Convert data types
    df['Satisfaction (1-5)'] = pd.to_numeric(df['Satisfaction (1-5)'], errors='coerce')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Feature engineering
    df['Date'] = df['Timestamp'].dt.strftime('%d-%m-%Y')
    df['Feedback Length'] = df['Feedback'].astype(str).apply(len)

    df.to_csv(CLEAN_PATH, index=False)
    print(f"[OK] Cleaned dataset saved to {CLEAN_PATH} ({len(df)} rows)")


if __name__ == "__main__":
    main()
