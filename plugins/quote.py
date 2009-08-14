"""
Quote: Quote things from a database

"""

import db
import re
from random import randint

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

def kstar (data = None):
    """Random Chuck Norris -> KStar quote"""
    # Multiplex between Chuck Norris and Kstar

    option = randint(0,1)
    if option == 0:
        regex = re.compile("([Cc]huck ([Nn]orris)?)|(([Cc]huck)? ([Nn]orris))")
        quote = quote_fn ("bot_quotes_chuck", data)
        quote = regex.sub("kstar", quote)
    else:
        quote = quote_fn ("bot_quotes_kstar", data)
        
    return quote

def kstar_insert (data = None):
    if (data == None or data.strip() == '' ):
        return "I understand that kstar's godliness surpasses all words, but please do your best"
    else:
        quote = data.strip()
        quote = quote.replace ("\"","\\\"")
        quote = "(\"%s\")"%quote
        db.insert ("bot_quotes_kstar", (quote), "`quote`")
        return "Factoid saved"

def starwars (data = None):
    """Random Star Wars quote"""
    return quote_fn ("bot_quotes_starwars", data)

def close ():
    file.close()

