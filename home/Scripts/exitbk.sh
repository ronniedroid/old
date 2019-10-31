#!/bin/bash

MENU="rofi -dmenu -i -location 3 -width 15 -lines 2 -xoffset -10 -yoffset 35 -eh 1 -p "-Exit?""
C=$(echo -e "YES\nNO\n" | $MENU)

case "$C" in
  YES) killall berry & ;;
  NO) exit 0;;
esac

