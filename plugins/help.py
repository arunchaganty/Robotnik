"""
Help: Help
"""
import conf

def init(data = None):
    pass

def help(data = None):
    """Options [function]: Help"""

    if (not data):
        rep = []
        rep.append("Rob0tnick Commands:")
        str = ""
        for item in conf.commands:
            lib = (item[1])[:item[1].rfind('.')]
            func= (item[1])[item[1].rfind('.')+1:]
            desc = (getattr(__import__(lib, {}, {}, ['']), func)).__doc__
            str += "!%s| "%item[0]
        rep.append (str[:-2])
        return rep
    else:
        rep = ""
        for item in conf.commands:
            if item[0] == data:
                lib = (item[1])[:item[1].rfind('.')]
                func= (item[1])[item[1].rfind('.')+1:]
                desc = (getattr(__import__(lib, {}, {}, ['']), func)).__doc__
                rep = "!%s: %s"%(item[0], desc)
                break
        else:
            rep = "Command not found"
        return rep



