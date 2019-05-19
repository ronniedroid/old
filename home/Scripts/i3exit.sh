#!/bin/bash

## Created By Aditya Shakya
#MENU="$(rofi -sep "|" -dmenu -i -p 'System' -location 3 -xoffset -10 -yoffset 50 -width 10 -hide-scrollbar -line-padding 4 -padding 20 -lines 4 <<< " Lock| Logout| Reboot| Shutdown")"
MENU="$(rofi -sep "|" -dmenu -i -p ' Exit i3?' -location 3 -xoffset -10 -yoffset 50 -width 12 -hide-scrollbar -line-padding 3 -padding 20 -lines 2 <<< " YES| NO")"
            case "$MENU" in
		 *YES) i3-msg exit ;;
                 *NO) exit 0;;
esac

