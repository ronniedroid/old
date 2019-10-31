#!/bin/bash

MENU="rofi -dmenu -i -location 3 -width 15 -lines 2 -xoffset -10 -yoffset 35 -eh 1 -p "-Exit?""
c=$(echo -e "YES\nNO\n" | $MENU)

if [ ${c} == YES ] 
then
	  if [ $(wmctrl -m | awk 'NR==1 {print $2}') == i3 ]
	  then
		  i3-msg exit
	  elif [ $(wmctrl -m | awk 'NR==1 {print $2}') == berry ]
	  then
		  killall berry
	  fi 
elif [ ${c} == NO ]
then
	exit 0
fi
