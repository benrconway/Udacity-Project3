import psycopg2

######################################################################
# SQL setup here


# Connect to an existing database
conn = psycopg2.connect("dbname=news user=postgres password=password")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("SELECT * FROM authors;")


# Query the database and obtain data as Python objects
results = cur.fetchall()

# Make the changes to the database persistent
conn.commit()
print(results)

# Close communication with the database
cur.close()
conn.close()


# SQL querying code here

# SQL query to answer question 1 without views

# SQL query to answer question 2 without views

# SQL query to answer question 3 without views






# SQL query to answer question 1 with views

# SQL query to answer question 2 with views

# SQL query to answer question 3 with views





#######################################################################
# Log Printing code here


# Formatting the answer code here

# Printing the code here

# Printing to a text file code here

# Commands to trigger output, one version commented out
