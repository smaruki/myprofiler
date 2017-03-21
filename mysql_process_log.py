#!/usr/bin/env python
# coding: utf-8

"""mysql_process_log - MySQL Processlist Log

https://github.com/smaruki/mysq_process_log
"""

import os
import sys
import re
from time import sleep
from datetime import datetime
from collections import defaultdict
from ConfigParser import SafeConfigParser
from optparse import OptionParser

try:
    import pymysql as MySQLdb  # PyMySQL
    from pymysql.cursors import DictCursor
except ImportError:
    print "Please install pymysql"
    sys.exit(1)

CMD_PROCESSLIST = "show full processlist"


def connect(conf='~/.my.cnf', section='DEFAULT'):
    """
    connect to MySQL from conf file.
    """
    parser = SafeConfigParser()
    parser.read([os.path.expanduser(conf)])

    args = {}

    args['host'] = parser.get(section, 'host')
    args['user'] = parser.get(section, 'user')
    args['passwd'] = parser.get(section, 'password')
    args['charset'] = 'utf8'
    if parser.has_option(section, 'port'):
        args['port'] = int(parser.get(section, 'port'))
    return MySQLdb.connect(**args)


def processlist(con):
    cur = con.cursor(DictCursor)
    cur.execute(CMD_PROCESSLIST)
    for row in cur.fetchall():
        if row['Info']:
            yield row


def normalize_query(row):
    row = ' '.join(row.split())
    return row


def build_option_parser():
    parser = OptionParser()
    parser.add_option(
            '-o', '--out',
            help="write raw queries to this file.",
            )
    parser.add_option(
            '-c', '--config',
            help="read MySQL configuration from. (default: '~/.my.cnf'",
            default='~/.my.cnf'
            )
    parser.add_option(
            '-s', '--section',
            help="read MySQL configuration from this section. (default: '[DEFAULT]')",
            default="DEFAULT"
            )
    parser.add_option(
            '-n', '--num-summary', 
            metavar="K",
            help="show most K common queries. (default: 10)",
            type="int", 
            default=10
            )
    parser.add_option(
            '-i', '--interval',
            help="Interval of executing show processlist [sec] (default: 2.0)",
            type="float", 
            default=2.0
            )
    parser.add_option(
            '-m', '--mintime',
            help="Minimum time run query (default: 10)",
            type="int", 
            default=15
            )
    return parser


def show_summary(counter, limit, file=sys.stdout):
    items = counter.items()
    items.sort(key=lambda x: x[1], reverse=True)
    for id, result in items[:limit]:
        print >>file, "%s" % (result)


def main():
    parser = build_option_parser()
    opts, args = parser.parse_args()

    try:
        outfile = None
        if opts.out:
            outfile = open(opts.out, "w")
        con = connect(opts.config, opts.section)
    except Exception, e:
        parser.error(e)

    counter = defaultdict(int)
    try:
        while True:
            for row in processlist(con):
                if row['Info'] == CMD_PROCESSLIST or row['Time'] < opts.mintime: 
                    continue

                query = normalize_query(row['Info'])
                result = ('%s - Execution Time: %s - Id: %s -  User: %s - DB: %s - Info: %s' % (
                    datetime.now(),
                    row['Time'],
                    row['Id'],
                    row['User'],
                    row['db'],
                    query
                    ))
                result += '\n------------------------------------------------------------' 
                counter[row['Id']] = result
                if outfile:
                    print >>outfile, result

            show_summary(counter, opts.num_summary)
            sleep(opts.interval)
    finally:
        if outfile:
            print >>outfile, "\nSummary"
            show_summary(counter, opts.num_summary, outfile)


if __name__ == '__main__':
    main()