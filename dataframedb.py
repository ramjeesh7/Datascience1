import pandas as pd
#import sqlite3
import sqlite3

#define connection and cursor
conn = sqlite3.connect('Movies.db')


#define commands and execute commands
command1 = 'SELECT * FROM Top_50'
command2 = 'SELECT COUNT(*) FROM Top_50'

#store the data from database as a dataframe
df=pd.read_sql(command1, conn)

#print result
print(df['Film'])


#close the connection
conn.close()