import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

#CREATING A DATAFRAME
df = pd.DataFrame(data)
print(df)

"""ACCESSING THE ROWS AND COLUMNS"""
#Single column
print(df['Name'])
#Multiple columns
print(df[['Name','Age']])

#SPECIFIC ROWS 
print(df.iloc[1,2])

#FILTERED DATA
filtered_data = df[df['Age']>25]
print(filtered_data)

data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [24, 27, None, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

dafa = pd.DataFrame(data_with_nan)

#CLEAN DATA WITH NAN VALUES
cleaned_df = dafa.dropna()
print(cleaned_df)

#FILL THE MISSING VALUES WITH SOME VALUES 
filled_data = dafa.fillna({"Age":20})
print(filtered_data)

#we can also drop duplicates 
drop_duplicate = dafa.drop_duplicates()
print(drop_duplicate)

"""DESCRIPTIVE STATISTICS"""

#describe
print(df.describe())
print(df['Age'].mean())

#group all of that
grouped = df.groupby('City')['Age'].mean()
print(grouped)

"""Merge the dataframes"""
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
})

df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'David'],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
#to merge
merged_df = pd.merge(df1,df2,on="Name")
print(merged_df)

#TO READ AND WRITE THE DATA
df_from_csv = pd.read_csv('file.csv')
df.to_csv('output.csv', index=False)
