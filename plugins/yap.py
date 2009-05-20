"""
Yap: Provides common "yap" features

"""
import db

# TODO call on all plugins
def init ():
    pass

def slap (data = None):
    """Slap someone with something"""
    try:
        quote = db.query ("SELECT `slap` FROM `%s` ORDER BY RAND() LIMIT 1"%("bot_slaps"))
        return "%s %s"%(data, quote[0][0])
    except db.mdb.ProgrammingError:
        return "Error retrieving slap"

def slap_save (data = None):
    """Save a new slap"""
    slap = data.strip()
    slap = slap.replace ("\"","\\\"")
    slap = "(\"%s\")"%slap
    db.insert ("bot_slaps", slap, "`slap`")
    return "Slap Saved"

