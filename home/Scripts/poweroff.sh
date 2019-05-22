#!/bin/bash

MENU="$(rofi -sep "|" -dmenu -i -p ' Power Off?' -location 3 -xoffset -10 -yoffset 50 -width 12 -hide-scrollbar -line-padding 3 -padding 20 -lines 2 <<< " YES| NO")"
            case "$MENU" in
		 *YES) systemctl poweroff ;;
                 *NO) exit 0;;
esac

