#import pandas library
import pandas as pd

#read data from csv file
df = pd.read_csv('top_50_films.csv')

#clean the empty data
new_df = df.dropna()

#print result
print(new_df.to_string())
