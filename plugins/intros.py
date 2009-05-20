"""
Intros: Save and retrieve user information
"""

import db

def init ():
    pass

def get (data=None):
    """Prints a person's introduction"""
    if data == None:
        name = "Rob0tnik"
    else:
        name = data.strip()

    if db.select ("bot_people", "`name` = \"%s\""%name):
        details = db.select ("bot_people", "`name` = \"%s\""%name)[0][2]
    else:
        return "Person does not exist in database."

    return "%s: %s"%(name, details) 

def save (data = None):
    """Saves a person's introduction"""
    if data == None:
        return "Nothing to save"

    args = data.split (" ", 1)
    if len(args) == 1:
        name = args[0]
        details = "Umm... what, you expected more?" # Pull from insults
    else:
        name = args[0]
        details = args[1]
        details = details.replace ("\"","\\\"")

    if db.select ("bot_people", "`name` = \"%s\""%name):
        db.update ("bot_people", "`details` = \"%s\""%details, "`name` = \"%s\""%name)
    else:
        db.insert ("bot_people", (name,details), "`name`, `details`")

    return "%s's Details Saved"%name

def close ():
    pass


