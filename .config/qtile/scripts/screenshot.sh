#! /bin/sh
output="$HOME/Pictures/screenshots/%Y-%m-%d-%T-screenshot.png"

case "$1" in
	"select") scrot "$output" --select --line mode=edge || exit ;;
	"window") scrot "$output" --focused --border || exit ;;
	*) scrot "$output" || exit ;;
esac

icon="~/.config/qtile/icons/camera.png"

notify-send -i "$icon" -t 2000 -u normal "Screenshot taken."
