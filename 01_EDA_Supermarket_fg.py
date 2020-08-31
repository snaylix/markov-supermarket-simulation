import pandas as pd

df = pd.read_csv('08_Supermarket_Analysis/_RES/monday.csv', sep=';')
df.shape
df.head()
df.tail()
# Calculate the total number of customers in each section
df['location'].value_counts()
# Calculate the total number of customers in each section over time
