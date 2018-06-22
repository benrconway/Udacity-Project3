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

The guidelines have set that *USUALLY* this is inside a single source file,
which I will follow for simplicity, however normally I would probably design
this into two files. The first would be in charge of querying SQL and all that
that would entail, the second would be in charge of the output.
To this end I will indicate in my code where this separation occurs for clarity
of review and simplicity of use.

To find out the answers to these questions, simply run *python3 log_writer.py*,
and watch the magic happen.
If successful it should (I am waiting for a reply to whether this should be
creating a text file or just printing to the console) the answers to these
questions.

How I came to these answers? (the numbers reference question numbers above)
1)

2)

3)

As they have also given us the freedom to create a version of this project
whereby we can use views, I have written in code that will make use of views
created with the following SQL commands.



If you create these views, you will also need to change the commenting on which
commands are being run by the python file. Please check comments to enable
the correct commands to run for the output to be correct.

If you have any questions, find any bugs or have suggestions, please don't
hesitate to be in contact with myself at *benrconway84@gmail.com*
