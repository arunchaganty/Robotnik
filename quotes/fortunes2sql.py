# Converts fortune formatted files into SQL
#
# fortune files are quotes separated by '%' marks.
# SQL requires input in the form of (NULL,"val",NULL) (in my case)

import sys

f_file = open (sys.argv[1], "r")
t_name = sys.argv[2]
f_string = "(NULL, \"%s\", NULL),\n"
ft_string = "(NULL, \"%s\", NULL)"

# Header
print """
DROP TABLE IF EXISTS `%s`;
CREATE TABLE `%s` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `quote` text NOT NULL,
  `props` int(10) NOT NULL default 0,
  PRIMARY KEY  (`id`)
); 

INSERT INTO `%s` VALUES"""%(t_name,t_name,t_name)

buffer = ""
for line in f_file:
    if line[0] == "%":
        print f_string%(buffer),
        buffer = ""
    else:
        buffer = buffer + (line.replace('"','\\\"')).replace ("\n","")
print ft_string%(buffer),


