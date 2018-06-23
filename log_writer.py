import psycopg2

######################################################################
# SQL setup here


# Connect to an existing database
conn = psycopg2.connect("dbname=news")

# Open a cursor to perform database operations
cur = conn.cursor()
sql = "select title, num from articles, (select substring(path from 10) as short, count(*) as num from log where path <> '/' and status = '200 OK' group by path order by num desc limit 3) as favs where articles.slug = favs.short order by num desc;"
# Execute a command: this creates a new table
cur.execute(sql)


# Query the database and obtain data as Python objects
results = cur.fetchall()

# Make the changes to the database persistent
conn.commit()
print("The Top Three Articles of All Time")
print("'{results[0][0]}' -- {results[0][1]}views")
print("'%s' -- %dviews" % (results[1][0], results[1][1]))
print("'%s' -- %dviews" % (results[2][0], results[2][1]))
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
