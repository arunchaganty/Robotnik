"""
Command module. Parses any strings like !module.command, or even just !command;
"""

import re

class CommandCenter:
    commands = {}
    def execute_cmd (self, phrase, data):
       replies = [] 
       for key in self.commands:
            if key == phrase:
                reply = self.commands[key](data)
                if type (reply) == type([]):
                    for str in reply: replies.append(str)
                elif type (reply) == type(""):
                    replies.append(reply)
                else:
                    print "Error in %s. Data: %s\n"%(key,data)
                break
       else:
           replies.append("And I think _all_ the world's problems can be solved if you *read the manual*. Pfft...")
       return replies
    def add_cmd (self, commands):
        for command in commands:
            mod_name, func = command[1].rsplit('.',1)
            try: 
                func = getattr(__import__(mod_name, {}, {}, ['']), func)
                self.commands[command[0]] = func
            except:
                raise
        print "Command installed: ", commands

