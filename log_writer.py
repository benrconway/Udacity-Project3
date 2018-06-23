import psycopg2

######################################################################
# SQL setup here


# Connect to an existing database
conn = psycopg2.connect("dbname=news")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute(sql)

# Query the database and obtain data as Python objects
results = cur.fetchall()

# Make the changes to the database persistent
conn.commit()
print("The Top Three Articles of All Time")
print("'%s' -- %d views" % (results[0][0], results[0][1]))
print("'%s' -- %d views" % (results[1][0], results[1][1]))
print("'%s' -- %d views" % (results[2][0], results[2][1]))
# Close communication with the database
cur.close()
conn.close()


# SQL querying code here

# SQL query to answer question 1 without views
sql = "select title, num from articles, (select substring(path from 10) as short, count(*) as num from log where path <> '/' and status = '200 OK' group by path order by num desc limit 3) as favs where articles.slug = favs.short order by num desc;"
# SQL query to answer question 2 without views

sql2 = "select authors.name, favs.num from authors, articles,(select substring(path from 10) as short, count(*) as num from log where path <> '/' and status = '200 OK' group by path order by num desc) as favs where articles.slug = favs.short and articles.author = authors.id order by num desc;"

# SQL query to answer question 3 without views

sql3 = "select a.date, round(a.num*100/b.num::numeric, 2) as percent from (select date, count(date) as num from (select time::timestamp::date as date from log where status <> '404 NOT FOUND') as a group by date order by date desc) as a, (select date, count(date) as num from (select time::timestamp::date as date from log where status = '200 OK') as a group by date order by date desc) as b where a.date = b.date;"




# SQL query to answer question 1 with views

# SQL query to answer question 2 with views

# SQL query to answer question 3 with views





#######################################################################
# Log Printing code here


# Formatting the answer code here

# Printing the code here

# Printing to a text file code here

# Commands to trigger output, one version commented out
