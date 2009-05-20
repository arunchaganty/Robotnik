"""
Search: Provides search facilites of common sources

"""

no_results = 3

# TODO call on all plugins
def init ():
    pass

def simple_search_fn (get_url, query):
    if query:
        query = query.strip().replace (" ", "+")
        # TODO: Query sanitize
        return get_url%query
    else:
        return "No query asked"
    return
def google (query=None):
    """Prints a convinient Google search URL"""
    return simple_search_fn ("http://www.google.com/search?q=%s", query)

def urban (query=None):
    """Prints a convinient Urban Dictionary search URL"""
    return simple_search_fn ("http://www.urbandictionary.com/define.php?term=%s", query)

def mlist (query=None):
    """Prints a convinient "linuxusers_iitm" mailing list search URL"""
    return simple_search_fn ("http://groups.google.com/group/linuxusers_iitm/search?group=linuxusers_iitm&q=%s", query)

def wiki (query=None):
    """Prints a convinient Wikipedia search URL"""
    simple_search_fn ("http://en.wikipedia.org/w/index.php?title=Special%%3ASearch&ns0=1&search=%s&fulltext=Advanced+search", query)

def wiki_auto (query=None):
    """Prints a Wikipedia URL"""
    if query:
        query = query.strip()
        query_ = ""
        set_cap = True
        for chr in query:
            if chr != " ":
                if set_cap:
                    query_ += chr.capitalize()
                    set_cap = False
                else:
                    query_ += chr.capitalize()
            else:
                set_cap = True
        query = query_
        # TODO: Query sanitize
        return "http://en.wikipedia.org/w/index.php?title=Special%%3ASearch&ns0=1&search=%s&fulltext=Advanced+search"%query
    else:
        return "No query asked"

def close ():
    pass

