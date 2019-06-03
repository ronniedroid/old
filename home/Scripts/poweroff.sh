#!/bin/bash

MENU="dmenu -i -p "-PowerOff?""
C=$(echo -e "YES\nNO\n" | $MENU)

case "$C" in
  YES) systemctl poweroff ;;
  NO) exit 0;;
esac

