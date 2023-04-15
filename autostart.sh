#!/bin/sh

nitrogen --restore &
xrandr --output HDMI-0 --mode 1920x1080 --rate 144.01 &
./mouse.sh &
