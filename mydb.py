import MySQLdb  # For mysqlclient

# Establish a connection to the database
database = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Jodongo123#",
    port=3306  # Optional if your MySQL server is using default port
)

# Prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

# Commit changes and close the connection
database.commit()
print("Database 'elderco' created successfully!")

# Close the cursor and database connection
cursorObject.close()
database.close()
