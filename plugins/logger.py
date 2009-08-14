"""
Logger: Keeps log

Using single text file
"""

import os, datetime
import conf

should_log = True
files = {}
date_current = datetime.date.today()

# TODO call on all plugins
def init ():
    global files
    files = {}

# Store one log file per 
def log (channel=None, user=None, msg=""):
    global should_log,files
    if channel == None or channel == "AUTH":
        channel = "Server"


    if not files.has_key(channel):
        date_current = datetime.date.today()
        fname = os.path.join(conf.logdir,"%s-%s.log"%(channel,date_current.isoformat()))
        files[channel] = open(fname, "a")
    elif datetime.date.today() > date_current:
            date_current = datetime.date.today()
            files[channel].close()
            fname = os.path.join(conf.logdir,"%s-%s.log"%(channel,date_current.isoformat()))
            files[channel] = open(fname, "a")

    # Auto-buffered
    if should_log:
        time_str = datetime.datetime.now().time.strftime("%H:%M:%S")
        if user:
            files[channel].write("[%s]\t%s: %s\n"%(time_str,user, msg))
        else:
            files[channel].write("[%s]\t%s: %s\n"%(time_str, "Server", msg))

def toggle (data = None):
    """Turn logging on/off"""
    global should_log
    should_log = not should_log
    return "Logging: %s"%str(should_log)

def close ():
    for file in files:
        file.close()

