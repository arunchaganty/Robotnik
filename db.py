"""
DB: General purpose wrapper around DB features

"""

import MySQLdb as mdb
import conf

db = mdb.connect(conf.db_host, conf.db_user, conf.db_pass, conf.db_name)
cur = db.cursor()

def query (query_str):
    global cur
    print query_str
    cur.execute (query_str)
    return cur.fetchall()

def select (table, params = None):
    if params:
        query_str = "SELECT * FROM `%s` WHERE %s"%(table, params)
    else:
        query_str = "SELECT * FROM `%s`"%(table)
    return query (query_str)

# Simple way of getting the previous results
def reselect ():
    global cur
    return cur.fetchall()

def insert (table, values, fields = ""):
    ins_str = "INSERT INTO `%s` (%s) VALUES %s"%(table, fields, values)
    return query (ins_str)

def update (table, values, params=None):
    up_str = "UPDATE `%s` SET %s WHERE %s"%(table, values, params)
    return query (up_str)

def count (table, param = None):
    if param:
        query_str = "SELECT COUNT(*) FROM %s WHERE %s"%(table, param)
    else:
        query_str = "SELECT COUNT(*) FROM %s"%(table)
    return query(query_str)[0]
    
