import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Drakan9135')

if conn.is_connected():
    print("Connected to mysql db")

# Create a cursor object to fetch the data from database table
cursor = conn.cursor()

# Execute mysql query, insert a new row to emp table
try: # The try block lets you test a block of code for errors.
    cursor.execute("insert into emp values(3, 'Jack', 30000)")
    conn.commit() # Use Commit once for all above code
    print("Employee Added")
except: # The except block lets you handle the error.
    conn.rollback() # If there is error above, then roll back


cursor.close()
conn.close()