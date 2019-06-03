#Autostart Section
sxhkd &
nitrogen --restore &
xinput set-prop 11 283 1

#Statusbar loop

dte(){
  dte="$(date +"%a, %b %d | 🕒 %H:%M")"
  echo "$dte"
}

mem(){
  mem=`free | awk '/Mem/ {printf "%d MiB/%d MiB\n", $3 / 1024.0, $2 / 1024.0 }'`
  echo "🖪 $mem"
}

cpu(){
  read cpu a b c previdle rest < /proc/stat
  prevtotal=$((a+b+c+previdle))
  sleep 0.5
  read cpu a b c idle rest < /proc/stat
  total=$((a+b+c+idle))
  cpu=$((100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) ))
  echo "💻 $cpu% cpu"
}

Bat(){
  Bat="$(acpi -b | awk '{print "🔋 " $4}' | sed "s/\,//g")"
  echo "$Bat"
}

Vol(){
  Vol="$(amixer get Master | awk -F'[][]' 'END{ print "🔊 " $2 }')"
  echo "$Vol"
}

BL(){
  BL="$(light | awk '{print "💡 " $1}')"
  echo "$BL"
}

KBL(){
  KBL="$(setxkbmap -query | awk 'FNR>2 {print $2}')"
  echo "$KBL"
}

while true; do
     xsetroot -name "$(Vol) | $(BL) | $(Bat) | $(dte) | $(KBL)"
     sleep 1s    # Update time every one seconds
done &

# start WM

exec dwm
