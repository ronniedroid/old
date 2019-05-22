#!/bin/bash

MENU="$(rofi -sep "|" -dmenu -i -p '  Layouts' -location 3 -xoffset -10 -yoffset 50 -width 12 -hide-scrollbar -line-padding 3 -padding 20 -lines 3 <<< " us| ar| dvorak")"
            case "$MENU" in
		 *us) setxkbmap us ;;
                 *ar) setxkbmap ar;;
                 *dvorak) setxkbmap dvorak ;;
esac

