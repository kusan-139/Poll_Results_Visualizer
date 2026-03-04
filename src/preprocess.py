
import pandas as pd

df = pd.read_csv('data/poll_data.csv')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna(subset=['Preferred Tool','Satisfaction (1-5)'])

# Standardize categorical responses
df['Preferred Tool'] = df['Preferred Tool'].str.strip().str.title()

# Convert data types
df['Satisfaction (1-5)'] = pd.to_numeric(df['Satisfaction (1-5)'], errors='coerce')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Feature engineering
df['Date'] = df['Timestamp'].dt.date
df['Feedback Length'] = df['Feedback'].astype(str).apply(len)

df.to_csv('data/cleaned_poll_data.csv', index=False)

print("Cleaned dataset saved to data/cleaned_poll_data.csv")
