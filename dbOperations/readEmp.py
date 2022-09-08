import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Drakan9135')

if conn.is_connected():
    print("Connected to mysql db")

# Create a cursor object to fetch the data from database table
cursor = conn.cursor()

# Execute mysql query and select all info from emp table
cursor.execute('select * from emp')


# Fetch one info into row
#row = cursor.fetchone()

# Fetch all
rows = cursor.fetchall()
print("Total number of records", cursor.rowcount)

# While row is not empty, print row and fetch the next info
# After the last value, fetch none and close
'''while row is not None:
    print(row)
    row = cursor.fetchone()'''

# Print all rows
for row in rows:
    print(row)

cursor.close()
conn.close()