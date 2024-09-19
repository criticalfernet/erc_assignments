import pandas as pd
import matplotlib.pyplot as plt

# QUESTION 1
data = {
    'Name': ['Aryan', 'Bablu', 'Chaman', 'Dhruv', 'Eklavya'],
    'Age': [15, 16, 17, 18, 19],
    'Score': [75, 80, 85, 90, 95]
}
df = pd.DataFrame(data)
csv_file = './tmp.csv'
df.to_csv(csv_file,index=False)

# QUESTION 2
housing_df = pd.read_csv('./Housing.csv')
housing_stats = housing_df.describe(include='all')
print(housing_stats)

# QUESTION 3
print(housing_df.shape)
missing_values = housing_df.fillna(0, inplace=True)

# QUESTION 4
bedrooms_sum = housing_df['bedrooms'].sum()
print(bedrooms_sum)

# QUESTION 5
housing_df['Total room count'] = housing_df['bedrooms'] + housing_df['bathrooms']
print(housing_df[['bedrooms', 'bathrooms', 'Total room count']])

# QUESTION 6
plt.scatter(housing_df['Total room count'], housing_df['price'])
plt.xlabel('Total rooms')
plt.ylabel('Price')
plt.show()
