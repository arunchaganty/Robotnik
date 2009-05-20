#!/usr/bin/env python
from twisted.internet import reactor, protocol
from bot import BotFactory
import conf

if __name__ == "__main__":
    # create factory protocol and application
    factory = BotFactory(conf.channels[0])

    # connect factory to this host and port
    reactor.connectTCP(conf.SERVER, conf.PORT, factory)

    # run bot
    reactor.run()

