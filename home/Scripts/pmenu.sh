#!/bin/bash

## Created By Aditya Shakya

#MENU="$(rofi -sep "|" -dmenu -i -p 'System' -location 5 -xoffset -14 -yoffset -52 -width 10 -hide-scrollbar -line-padding 4 -padding 20 -lines 4 <<< " Lock| Logout| Reboot| Shutdown")"
MENU="$(rofi -sep "|" -dmenu -i -p ' Power Menu' -location 3 -xoffset -10 -yoffset 50 -width 12 -hide-scrollbar -line-padding 4 -padding 20 -lines 4 <<< " Lock| Logout| Reboot| Shutdown")"
            case "$MENU" in
                *Lock) i3lock-fancy ;;
                *Logout) ~/Scripts/exit.sh;;
                *Reboot) ~/Scripts/reboot.sh  ;;
                *Shutdown) ~/Scripts/poweroff.sh
esac
