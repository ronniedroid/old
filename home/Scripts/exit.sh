#!/bin/bash

MENU="dmenu -i -l 2 -p "-Exit?""
C=$(echo -e "YES\nNO\n" | $MENU)

case "$C" in
  YES) killall dwm & ;;
  NO) exit 0;;
esac

