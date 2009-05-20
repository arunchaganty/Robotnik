# Server
SERVER = "irc.freenode.net"
PORT = 6667

auth = ("Rob0tnik", "")
channels = ["#iitm-linux"]
cmd_char = "!"

db_host = "localhost"
db_user = "root"
db_pass = "teju"
db_name = "arunchaganty"

dispatches = [
        ('.*', 'plugins.logger.log'),
]

commands = [
        ('log.toggle', 'plugins.logger.toggle'),
        ('google', 'plugins.search.google'),
        ('urban', 'plugins.search.urban'),
        ('mlist', 'plugins.search.mlist'),
        ('wiki', 'plugins.search.wiki'),
        ('wiki!', 'plugins.search.wiki_auto'),
        ('chuck', 'plugins.quote.chuck_norris'),
        ('linus', 'plugins.quote.linus'),
        ('rms', 'plugins.quote.rms'),
        ('starwars', 'plugins.quote.starwars'),
        ('takeoverworld', 'plugins.wit.take_over_world'),
        ('rkk', 'plugins.wit.rkk'),
        ('cpr', 'plugins.wit.cpr'),
        ('give.intro', 'plugins.intros.save'),
        ('put.intro', 'plugins.intros.get'),
        ('fortunes', 'plugins.fortunes.fortunes'),
        ('help', 'plugins.help.help'),
        ('slap.save', 'plugins.yap.slap_save'),
        ('slap', 'plugins.yap.slap'),
]

