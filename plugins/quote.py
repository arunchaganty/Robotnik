"""
Quote: Quote things from a database

"""

import db

def init ():
    pass

def quote_fn (table, data = None):
    max = db.count (table)
    try:
        quote = db.query ("SELECT `quote` FROM `%s` ORDER BY RAND() LIMIT 1"%table)
        return quote[0][0]
    except db.mdb.ProgrammingError:
        return "Error retrieving quote"
        
def linus (data = None):
    """Random Linus Torvalds quote"""
    return quote_fn ("bot_quotes_linus", data)
def rms (data = None):
    """Random Richard Stallman quote"""
    return quote_fn ("bot_quotes_rms", data)
def chuck_norris (data = None):
    """Random Chuck Norris fact"""
    return quote_fn ("bot_quotes_chuck", data)
def starwars (data = None):
    """Random Star Wars quote"""
    return quote_fn ("bot_quotes_starwars", data)

def close ():
    file.close()

