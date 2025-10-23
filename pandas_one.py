import pandas as pd

# Create a simple DataFrame (like an Excel table)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Access a specific column
print("\nNames column:")
print(df['Name'])

# Filter rows where Age > 28
print("\nPeople older than 28:")
print(df[df['Age'] > 28])

# Add a new column
df['Country'] = 'USA'
print("\nDataFrame after adding a new column:")
print(df)
