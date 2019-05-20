#!/bin/bash

## Created By Aditya Shakya
#MENU="$(rofi -sep "|" -dmenu -i -p 'System' -location 3 -xoffset -10 -yoffset 50 -width 10 -hide-scrollbar -line-padding 4 -padding 20 -lines 4 <<< " Lock| Logout| Reboot| Shutdown")"
MENU="$(rofi -sep "|" -dmenu -i -p '  Layouts' -location 3 -xoffset -10 -yoffset 50 -width 12 -hide-scrollbar -line-padding 3 -padding 20 -lines 3 <<< " us| ar| dvorak")"
            case "$MENU" in
		 *us) setxkbdmap us ;;
                 *ar) setxkbdmap ar;;
                 *dvorak) setxkbdmap dvorak ;;
esac

