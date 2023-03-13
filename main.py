import pandas as pd

# reading csv file
df = pd.read_csv('venv/resource/DataSet.csv')

# read a specific location
print(df.iloc[2, 3])

# read each row
# print(df.iloc[1])
# print(df.iloc[1:4])

# read each column
# print(df['Calories'])
# print(df['Calories'][0:5])
# print(df[['Calories', 'Duration']])

# # read headers
# print(df.columns)

# # convert data into a correct format
# df['Date'] = pd.to_datetime(df['Date'])
#
# # removing the row with empty/null value
# df.dropna(subset=['Date'], inplace=True)
#
# # replacing wrong value
# df.loc[7, 'Duration'] = 45
#
# print(df.to_string())
