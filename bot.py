"""
Documenation here.
"""

from twisted.words.protocols import irc
from twisted.internet import reactor, protocol

from dispatcher import IRCDispatcher
from command import CommandCenter

import time, sys
import conf

class Bot(irc.IRCClient):
    """An IRC bot."""
    
    # TODO: Get this information from a config file
    nickname, password = conf.auth

    def __init__ (self):
        self.dispatcher = IRCDispatcher ()
        self.dispatcher.add_dispatches (conf.dispatches)
        self.commander = CommandCenter ()
        self.commander.add_cmd (conf.commands)
    
    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        self.dispatcher.dispatch (self.dispatcher.EVT_CONNNECTION_MADE, [])

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        self.dispatcher.dispatch (self.dispatcher.EVT_CONNNECTION_LOST, [reason,])

    # callbacks for events

    def signedOn(self):
        """Called when bot has succesfully signed on to server."""
        # TODO: >1 channel
        self.join(self.factory.channel)
        self.dispatcher.dispatch (self.dispatcher.EVT_SIGNED_ON, [])

    def joined(self, channel):
        """This will get called when the bot joins the channel."""
        self.dispatcher.dispatch (self.dispatcher.EVT_JOINED, [channel,])

    def privmsg(self, user, channel, msg):
        """This will get called when the bot receives a message."""
        user = user.split('!', 1)[0]
        self.dispatcher.dispatch (self.dispatcher.EVT_PRIVMSG, [channel,user, msg,])
        
        # Check to see if they're sending me a private message
        if channel == self.nickname:
            if user == "vimzard":
                if msg == "reload!":
                    self.dispatcher.dispatches = {}
                    self.dispatcher.add_dispatches (conf.dispatches)
                    self.commander.commands = {}
                    self.commander.add_cmd (conf.commands)
                    msg = "Plugins reloaded"
                elif msg == "quit!":
                    reactor.stop()
                else:
                    msg = "Hello :-)"
            else:
                msg = "I'm sorry, I only listen to my master, Vimzard"

            self.msg(user, msg)
            return

        # Otherwise check to see if it is a message directed at me
        if msg.startswith(self.nickname + ":"):
            msg = "%s: I am an awesome experiment in human-cyborg relations. Worship me!" % user
            self.msg(channel, msg)
            self.dispatcher.dispatch (self.dispatcher.EVT_PRIVMSG, [channel, conf.auth[0], msg,])

        if msg.startswith (conf.cmd_char):
            msg = msg[len(conf.cmd_char):]
            if msg.find (' ') != -1:
                phrase, data = msg.split (' ', 1)
                replies = self.commander.execute_cmd (phrase, data)
            else:
                replies = self.commander.execute_cmd (msg, None)

            for reply in replies:
                self.msg(channel, reply)
                self.dispatcher.dispatch (self.dispatcher.EVT_PRIVMSG, [channel, conf.auth[0], reply,])

    def action(self, user, channel, msg):
        """This will get called when the bot sees someone do an action."""
        user = user.split('!', 1)[0]
        self.dispatcher.dispatch (self.dispatcher.EVT_ACTION, [channel,user, msg,])

    def irc_NICK(self, prefix, params):
        """Called when an IRC user changes their nickname."""
        self.dispatcher.dispatch (self.dispatcher.EVT_ACTION, [prefix,params,])

class BotFactory(protocol.ClientFactory):
    """A factory for Bots.

    A new protocol instance will be created each time we connect to the server.
    """

    # the class of the protocol to build when new connection is made
    protocol = Bot

    def __init__(self, channel):
        self.channel = channel

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()

