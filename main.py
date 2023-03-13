import pandas as pd

# reading csv file
df = pd.read_csv('venv/resource/DataSet.csv')

# convert data into a correct format
df['Date'] = pd.to_datetime(df['Date'])

# removing the row with empty/null value
df.dropna(subset=['Date'], inplace=True)

print(df.to_string())
