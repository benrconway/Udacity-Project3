#!/usr/bin/env python3

import psycopg2


# As the same query is called three times, I thought it prudent to make it
# into a simple function
def query(sql_query):
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()
    cur.execute(sql_query)
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return results


# I would have made a single function to handle all outputs, but each was
# specific enough to merit having individual output functions
def topThree(results):
    print("*** The Top Three Articles of all Time ***")
    for result in results:
        print("'{}' -- {} views".format(result[0], result[1]))


def topAuthors(results):
    print("*** The Most Popular Authors of all Time ***")
    for result in results:
        print("{} -- {} views".format(result[0], result[1]))


def topErrors(results):
    print("*** The days on which more than 1% of requests lead to errors ***")
    for result in results:
        print("{} -- {}% errors".format(result[0], result[1]))


# I could revise the queries as per description in the previous review, however
# I choose to keep it this way at present as this is my current understanding
# and follows what is written in the README file attached.
# SQL query to answer question 1
sql = """select title, num from articles,
        (select substring(path from 10) as short, count(*) as num from log
         where path <> '/' and status = '200 OK' group by path
          order by num desc limit 3) as favs
           where articles.slug = favs.short order by num desc;"""
# SQL query to answer question 2
sql2 = """select authors.name , hits.num from authors,
        (select articles.author, count(*) as num from articles,
        (select substring(path from 10) as short from log
         where path <> '/' and status = '200 OK') as views
          where articles.slug = views.short group by articles.author
           order by num desc) as hits where authors.id = hits.author
            order by hits.num desc;"""
# SQL query to answer question 3
sql3 = """select * from (select a.date, round(a.num*100/b.num::numeric, 2)
        as percent from (select date, count(date) as num
         from (select to_char(time::timestamp::date, 'FMMonth DD, YYYY')
          as date from log where status = '404 NOT FOUND') as a
           group by date order by date desc) as a,
            (select date, count(date) as num from
            (select to_char(time::timestamp::date, 'FMMonth DD, YYYY') as date
             from log where status = '200 OK') as a group by date
              order by date desc) as b where a.date = b.date
               order by percent desc) as errors where percent > 1;"""

# Below is the functions being called and then printing their results.
print("\n")
results1 = query(sql)
topThree(results1)
print("\n")

results2 = query(sql2)
topAuthors(results2)
print("\n")

results3 = query(sql3)
topErrors(results3)
print("\n")
