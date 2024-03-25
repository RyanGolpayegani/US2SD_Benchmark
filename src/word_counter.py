import pandas as pd

df = pd.read_csv("data/All_US.csv")

# Specify the column to read
col_name = 'User Story'

# Calculate the number of words in each row of the column
df['num_words'] = df[col_name].apply(lambda x: len(x.split()))
total_words = df['num_words'].sum()
# Print the DataFrame
print(total_words)
