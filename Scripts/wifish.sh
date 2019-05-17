#!/bin/sh

wifish list | awk 'FNR>2 {print $1}' | rofi -dmenu i -p '  Available Networks' -location 3 -xoffset -10 -yoffset 50 -width 20 -hide-scrollbar -line-padding 4 -padding 20 -lines 6 | xargs -r wifish connect
