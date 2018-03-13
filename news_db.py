#!/usr/bin/env python3

"""Tool to answer questions on the news database."""

import psycopg2


def popular_articles(n):
    """
    Show the most popular ('n' number of) posts.

    int n: number of posts to show.
    return: None
    """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    c.execute("select title, count(*) as total "
              "from articles join log "
              "on log.path = '/article/' || articles.slug "
              "group by title "
              "order by total "
              "desc limit {}".format(n))
    all_posts = c.fetchall()
    print("{} most popular articles based on number "
          "of views: ".format(n))
    for post, view in all_posts:
        print('"{}" -- {} views'.format(post, view))
    print("\n=================================\n")
    db.close()


def popular_authors():
    """
    Show the most popular authors.

    Print the names of mos popular authors along with the
    respective page views of their articles.

    return: None
    """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    c.execute("select name, sum(total) as views "
              "from authors join "
              "(select author, title, count(*) as total "
              "from articles join log "
              "on log.path = '/article/' "
              "|| articles.slug "
              "group by author, title order by "
              "total desc) as subq "
              "on authors.id=subq.author "
              "group by name order by views desc;")
    all_posts = c.fetchall()
    print("Most popular authors based on number of views:")
    for name, view in all_posts:
        print('{} -- {} views'.format(name, view))
    print("\n================================\n")
    db.close()


def request_errors(n):
    """
    Show dates when more than 'n' % requests were errors.

    int n: Errors of percentage of total requests
           above which the date should be printed.

    return: None
    """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    c.execute("select to_char(dt,'Mon DD, YYYY'), request_total, "
              "request_failure, "
              "(request_failure::float * 100 / "
              "request_total) "
              "as perc from "
              "( select time::date as dt, "
              "count(*) as request_total, "
              "count(case when status <> '200 OK' "
              "then 1 else null end) as request_failure "
              "from log group by dt) as subq")
    req_stats = c.fetchall()
    print("Days when more than {} % requests led to errors".format(n))
    for stat in req_stats:
        if stat[3] > n:
            print("{} -- {}% errors".
                  format(
                      stat[0],
                      stat[3]
                      )
                  )
    print("\n=================================\n")
    db.close()


if __name__ == "__main__":
    print("\n=================================\n")
    popular_articles(3)
    popular_authors()
    request_errors(1)
