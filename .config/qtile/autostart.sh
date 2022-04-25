#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &


xrandr --output Virtual1 --primary --mode 1440x900 --pos 0x0 --rotate normal --output Virtual2 --off --output Virtual3 --off --output Virtual4 --off --output Virtual5 --off --output Virtual6 --off --output Virtual7 --off --output Virtual8 --off


nitrogen --restore &
#exec --no-startup-id picom -CGb
#exec picom -CGb
exec picom &
