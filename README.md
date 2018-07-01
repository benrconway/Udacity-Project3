# Udacity Full Stack Web Developer Nanodegree
## Project 3: Log Analysis

In my progress through this course, we have now engaged in taking a dive into
SQL databases, how python connects with them and some of the value in being able
to persist your data. (Which is significant)

For this project, I have been supplied with a database from a 5 star (totally
fictional) rated newspaper website. They have kept track of their authors,
articles and website activity.
From this rather enormous collection of SQL entries, I am tasked with using
a combination of SQL and python to create an output that answers the following
three questions:

1) What are the most popular three articles of all time?

2) Who are the most popular article authors of all time?

3) On which days did more than 1% of requests lead to errors?

I am to use a single SQL query to answer each of these questions and then take
those resulting tables into the world of python and prints them out in plain
text.

### Setup

1) Download and install Virtual Box (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
and Vagrant (https://www.vagrantup.com/downloads.html)

2) Once you have both of those setup in your system, go you can fork and/or clone
 the Full Stack Nanodegree course's VM setup from here (https://github.com/udacity/fullstack-nanodegree-vm).

3) Download the Newsdata information required to build the correct psql database.
(https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

4) Navigate into the cloned repository and then into the subdirectory 'vagrant'.
Inside this directory, run the command 'vagrant up'. This may take a while to
execute as it is downloading and installing a linux operating system.

5) Once it has completed, extract the newsdata.sql file from the zip of the same
name and place it inside the same '/vagrant' subdirectory.

6) Now use the command 'vagrant ssh' to move into the newly created Virtual Machine (VM),
once inside, run the command 'psql -d news -f newsdata.sql' (which will create
  the appropriate database and seed it with the news data).


Now you should be setup and ready to go. You can simply explore the database by using
the command 'psql news', or now clone this repository into the same shared directory and
run *python3 log_writer.py*, to see the answers to the questions above.

If everything is successful it should output the following on the terminal:


*** The Top Three Articles of all Time ***
'Candidate is jerk, alleges rival' -- 338647 views
'Bears love berries, alleges bear' -- 253801 views
'Bad things gone, say good people' -- 170098 views


*** The Most Popular Authors of all Time ***
Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views


*** The days on which more than 1% of requests lead to errors ***
July 17, 2016 -- 2.26% errors


How I came to these answers? (the numbers reference question numbers above)

1) To get the three most popular articles, I needed to access the log table and
find a way to connect which articles were being viewed to the articles on the
articles table.
I did this by taking a substring of the path on all the rows in the log that
did not have a path of '/' and had a status of '200 OK'. This meant that I had
only the successful hits and those that weren't the standard home route.
Once I had this, I took a substring of that path, which I could then match
against the articles column called 'slug'. Having this comparison allowed me to
find the number of successful views and also connect it into a new result table
that showed only the title of the article and how many hits it had.
With those in place, I only needed to limit the number of results to the top
three in descending order.

2) To get the most popular authors followed a similar pattern first answer.
First I created a result table from the log table with the substring that would
match a article slug. I then made another table which was matched the slug to
the provided substring, which was then grouped by the article's author ID and
 a count of how many hits that particular author's articles had been viewed.
Finally these were joined to the authors table to provide a list of author's
names and hits associated with their articles.

3) Finally, providing any dates that had errors above 1% required that I create
a self join, as I would access only the log table for this question. So I
created two result tables I called A and B, one was the collection of all
requests on a given day that ended in a status of '404 NOT FOUND' and the other
a list of dates and all requests made on a given day.
Once I had those two, I needed to understand how to make a percent in PSQL and
do some formatting on the given date format to match the desired output as
defined by the project brief.

While it took me a while to get the SQL queries correct, it was a valuable
lesson in how to think about data and also what is potentially worth storing
to create these metrics.
In future I might opt to create views as running this file takes longer with
the queries being run in their simplicity, however the desired result is
achieved.



If you have any questions, find any bugs or have suggestions, please don't
hesitate to be in contact with myself at *benrconway84@gmail.com*
