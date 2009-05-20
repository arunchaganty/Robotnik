DROP TABLE IF EXISTS `bot_slaps`;
CREATE TABLE `bot_slaps` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `slap` text NOT NULL,
  `props` int(10) NOT NULL default 0,
  PRIMARY KEY  (`id`)
); 

