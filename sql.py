#import sqlite3
import sqlite3

#define connection and cursor

conn = sqlite3.connect('Movies.db')

cursor = conn.cursor()

#define commands and execute commands
command1 = 'SELECT * FROM Top_50'
command2 = 'SELECT COUNT(*) FROM Top_50'


cursor.execute(command1)

# # Query statement	                            Purpose
# # SELECT * FROM table_name	                Retrieve all entries of the table.
# # SELECT COUNT(*) FROM table_name	            Retrieve total number of entries in the table.
# # SELECT Column_name FROM table_name	        Retrieve all entries of a specific column in the table.
# # SELECT * FROM table_name WHERE <condition>	Retrieve all entries of the table that meet the specified condition.

#store results in a variable and print the result
results = cursor.fetchall()

#cursor.fethcall() is an iterable object.
print(results[0])

#close the connection
conn.close()
