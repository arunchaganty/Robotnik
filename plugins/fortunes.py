"""
Fortune: Fortunes

"""

import random as rnd
import db

dataset = ("computers","cookie","definition","dubya","education","goedel", "linux", "linuxcookie", "paradoxum", "riddles", "startrek",)

def init ():
    pass

def fortunes (data = None):
    """Options [dataset]| Retrieves a fortune at random from the following datasets"""
    global dataset
    if not data or data not in dataset:
        data = dataset[rnd.randint(0,len(dataset))-1]
    table = "bot_fortunes_%s"%data
    try:
        quote = db.query ("SELECT `quote` FROM `%s` ORDER BY RAND() LIMIT 1"%table)
        return "%s: %s"%(data,quote[0][0])
    except db.mdb.ProgrammingError:
        return "Error retrieving quote"

def close ():
    file.close()

