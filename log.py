# !/usr/bin/env python

import psycopg2

DATABASE_NAME = "news"


LOG_PROBLEM_1 = "*1. What are the most popular three articles of all time?*\n"


# this query execute most popular 3 articles of all
# time from our news postgresql database

LOG_ARTICLES_QUERY_1 = """  SELECT articles.title, COUNT(*) AS views_count
                            FROM articles
                            JOIN log
                            ON log.path LIKE concat
                            ('%/article/%', articles.slug)
                            GROUP BY articles.title
                            ORDER BY views_count DESC
                            LIMIT 3; """

LOG_PROBLEM_2 = "*2. Who are the most popular article authors of all time?*\n"


# this query execute most popular article authors of all
# time from news postgresql database

LOG_AUTHORS_QUERY_2 = """ SELECT authors.name,
                          count(*) as view_count
                         FROM articles JOIN authors ON
                         articles.author = authors.id JOIN
                         log ON articles.slug = substring(log.path, 10)
                         WHERE log.status LIKE '200 %' GROUP BY
                         authors.name ORDER BY view_count DESC;"""


LOG_PROBLEM_3 = """*3. On which days did more than 1%
of requests lead to errors?*\n"""


# this query execute getting the date on which day we got the more
# than 1% of requests lead to errors from news postgresql database

LOG_ERROR_QUERY_3 = """select day, round((errors*100.0)/requests,3)
                                                as error_rate from log_err_view
                                                where errors > requests/100;"""

# Connect to the database to extract query results
db = psycopg2.connect(dbname=DATABASE_NAME)
c = db.cursor()


def get_results(sql_query):
    try:
        # we are handling errors with try /except
        c.execute(sql_query)
    except Exception as exception:
        print("Exception\t:", exception)
    else:
        results = c.fetchall()
        return results


def print_reports(data):
    """printing reports from given data object
    """
    for i in range(len(data)):
        title, views = data[i]
        print("\t" + "%s ===> %d" % (title, views) + " views")
    print('\n')


def print_last_query(data):
    """printing nice format for last given problem
    """
    for i in range(len(data)):
        date, percentage = data[i]
        print("\t" + "{} % ===> {}".format(percentage, date))


# executing queries from defined strings
result_1 = get_results(LOG_ARTICLES_QUERY_1)
result_2 = get_results(LOG_AUTHORS_QUERY_2)
result_3 = get_results(LOG_ERROR_QUERY_3)


# print the reports for given questions in nice format
print(LOG_PROBLEM_1)
print_reports(result_1)
print(LOG_PROBLEM_2)
print_reports(result_2)
print(LOG_PROBLEM_3)
print_last_query(result_3)


# finally closing the database connection
db.close()
