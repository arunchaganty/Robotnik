"""
PluginRedirector.
Matches regex patterns in incoming text and redirects them
to registered plugins
"""

import re

class IRCDispatcher:
    EVT_CONNNECTION_MADE = "connection:made"
    EVT_CONNNECTION_LOST = "connnection:lost" 
    EVT_SIGNED_ON = "irc:signed_on"
    EVT_JOINED = "irc:joined"
    EVT_PRIVMSG = "irc;privmsg"
    EVT_ACTION = "irc:action"
    EVT_IRC_NICK = "irc:nick"

    dispatches = {}
    """
    Maintains a table of (event,regex)-method
    """

    def dispatch (self, event, data):
       for events in self.dispatches:
            if events.match (event):
               self.dispatches[events](*data)

    def add_dispatches (self, dispatches):
        for dispatch in dispatches:
            mod_name, func = dispatch[1].rsplit('.',1)
            try: 
                func = getattr(reload(__import__(mod_name, {}, {}, [''])), func)
                self.dispatches[(re.compile(dispatch[0]))] = func
            except:
                raise
        print "Dispatch installed: ", dispatches


