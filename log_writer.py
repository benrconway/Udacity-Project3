import psycopg2
import calendar

######################################################################
# SQL setup here
def query(sql_query):
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    cur.execute(sql_query)
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results

def topThree(results):
    print("The top three articles of all time:")
    for result in results:
        print("'{}' -- {} views".format(result[0], result[1]))

def topAuthors(results):
    print("The most popular authors of all time:")
    for result in results:
        print("{} -- {} views".format(result[0], result[1]))

def topErrors(results):
    # needs the answer string to be broken into parts and re-presented.
    print("The days on which more than 1% of requests lead to errors:")
    for result in results:
        print("{} -- {}% errors".format(result[0], result[1]))


# SQL query to answer question 1
sql = "select title, num from articles, (select substring(path from 10) as short, count(*) as num from log where path <> '/' and status = '200 OK' group by path order by num desc limit 3) as favs where articles.slug = favs.short order by num desc;"
# SQL query to answer question 2, needs fixing to put the it all back together and not have duplicate names.
sql2 = "select authors.name, favs.num from authors, articles,(select substring(path from 10) as short, count(*) as num from log where path <> '/' and status = '200 OK' group by path order by num desc) as favs where articles.slug = favs.short and articles.author = authors.id order by num desc;"
# SQL query to answer question 3
sql3 = "select * from (select a.date, round(a.num*100/b.num::numeric, 2) as percent from (select date, count(date) as num from (select time::timestamp::date as date from log where status = '404 NOT FOUND') as a group by date order by date desc) as a, (select date, count(date) as num from (select time::timestamp::date as date from log where status = '200 OK') as a group by date order by date desc) as b where a.date = b.date order by percent desc) as errors where percent > 1;"

results1 = query(sql)
topThree(results1)
print("\n")

results2 = query(sql2)
# topAuthors(results2)


results3 = query(sql3)
topErrors(results3)


#######################################################################
# Log Printing code here


# Formatting the answer code here

# Printing the code here

# Printing to a text file code here

# Commands to trigger output, one version commented out
