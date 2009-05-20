"""
Wit: Provides witty comebacks

"""
import random

rkk_quotes=["Go home and think about it!",
     "It will fly!",
     "Baaah!",
     "waves his hand around",
     "That stupid thing will not work",
    ]

# TODO call on all plugins
def init ():
    pass

def take_over_world (data=None):
    return "On it..."

def rkk (data=None):
    return rkk_quotes[random.randint(0,len(rkk_quotes)-1)]

def cpr (data=None):
    return "You will die!"

def stupid (data=None):
    return "And I think _all_ the world's problems can be solved if you *read the manual*. Pfft..."

def spam (data=None):
    return "Spam sham, alakazam"

def close (data=None):
    pass

