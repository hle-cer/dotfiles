#!/bin/bash
set -eu

# ./hotspot.sh on
# ./hotspot.sh off

ssid="sos-hotspot"
password="basosed1"

case $1 in
    on)
        nmcli device wifi hotspot password $password ssid $ssid
        dunstify -i ~/.config/qtile/icons/hotspot.png "Hotspot: ON"
        ;;
    off)
        nmcli radio wwan off
        dunstify -i ~/.config/qtile/icons/hotspot.png "Hotspot: OFF"
        ;;
esac
