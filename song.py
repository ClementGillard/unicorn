#!/usr/bin/python
# displays the song and artist currently playing on twitch.tv/monstercat
# relies on an homemade script accessible at cigix.noip.me/update.php

from scrolldisp import Display
import unicornhat, urllib2

unicornhat.brightness(0.5)
Display("~R" + urllib2.urlopen("http://cigix.noip.me/update.php").read() + " ~R", delay=0.03)
