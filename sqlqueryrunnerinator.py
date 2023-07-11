# Import the mysql-connector-python module
import mysql.connector

# Create a connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute a query to create a database
mycursor.execute("CREATE DATABASE IF NOT EXISTS exampledb")

# Execute a query to use the database
mycursor.execute("USE exampledb")

# # Execute a query to create a table
# mycursor.execute(
#     "CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# # Execute a query to insert some data
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ('John', 'Highway 21'),
#     ('Mary', 'Lowstreet 4'),
#     ('Peter', 'Park Lane 38'),
#     ('Amy', 'Apple st 652')
# ]
# mycursor.executemany(sql, val)

# # Commit the changes to the database
# mydb.commit()

# # Print the number of rows inserted
# print(mycursor.rowcount, "records inserted.")

# Execute a query to select all data
mycursor.execute("SELECT * FROM customers")

# Fetch all the rows from the result set
myresult = mycursor.fetchall()

# Print the result
for x in myresult:
    print(x)

# Close the cursor and connection objects
mycursor.close()
mydb.close()
