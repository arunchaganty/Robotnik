"""
Logger: Keeps log

Using single text file
"""

log_file = "irc.log"

should_log = True
file = open (log_file, "a")

# TODO call on all plugins
def init ():
    pass

def log (channel="NotConnected", user="Info", msg=""):
    global file
    global should_log
    # Auto-buffered
    if should_log:
        file.write ("[%s]%s: %s\n"%(channel, user, msg))
def toggle (data = None):
    """Turn logging on/off"""
    global should_log
    should_log = not should_log
    return "Logging: %s"%str(should_log)

def close ():
    file.close()

