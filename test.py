import dispatcher
dispatches = [
        ('.*', '.*', 'plugins.logger.log'),
]
dep = dispatcher.IRCDispatcher ()
dep.add_dispatches (dispatches)

for key, func in dep.dispatches:
    print key, func


