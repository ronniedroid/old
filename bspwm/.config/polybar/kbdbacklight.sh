#!/bin/zsh

echo "$(light -s sysfs/leds/smc::kbd_backlight | cut -d. -f1)"
