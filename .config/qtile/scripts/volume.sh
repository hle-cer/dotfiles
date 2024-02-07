#!/bin/sh
set -eu
# You can call this script like this:
# $./volume.sh up
# $./volume.sh down
# $./volume.sh mute

# icons
audio_icon_high="~/.config/qtile/icons/volume_on.png"
audio_icon_medium="~/.config/qtile/icons/volume_med.png"
audio_icon_low="~/.config/qtile/icons/volume_low.png"
mute_icon="~/.config/qtile/icons/volume_off.png"
icon_capture_on="~/.config/qtile/icons/mic_on.png"
icon_capture_off="~/.config/qtile/icons/mic_off.png"
icon_capture_unk="~/.config/qtile/icons/mic_unk.png"


# output
# use the following option for pulseaudio
#output_name="pulse"
# use the following option for alsa
output_name="default"



get_volume () {
    amixer get Master | grep '%' | head -n 1 | cut -d '[' -f 2 | cut -d '%' -f 1
}

is_mute () {
    amixer get Master | grep '%' | grep -oE '[^ ]+$' | grep off > /dev/null
}

function get_mic_toggle {
    # Send the notification for the current micrphone status
    # Get the mic status
    micstatus=$(amixer get Capture|grep '%' | grep -oE '[^ ]+$')
    # The capture will probably have more than one channel, so we need to get the number of channels
    channels=$(wc -l <<< "$micstatus")
    # Now we are going to count the number that are "on"
    num_on=$(grep -o 'on' <<< "$micstatus"|wc -l)
    # And count the number that are "off"
    num_off=$(grep -o 'off' <<< "$micstatus"|wc -l)
    # If the number of on match the number of channels, weknow the mic is on
    if [ "$channels" -eq "$num_on" ];then
        dunstify -t 1600 -i "$icon_capture_on" -r 2593 -u normal "Microphone: On"
    # If the number of off match the number of channels, we know the mic is off
    elif [ "$channels" -eq "$num_off" ];then
        dunstify -t 1600 -i "$icon_capture_off" -r 2593 -u normal "Microphone: Off"
    # If the number of on and off don't match the number of channels, we don't really know the status
    else
        dunstify -t 1600 -i "$icon_capture_unk" -r 2593 -u normal "Unknown"
    fi
}

send_notification () {
    # Send the notification
    dunstify -i "$audio_icon" -t 1600 -h string:x-dunst-stack-tag:volume -u normal "Volume" -h int:value:"$(get_volume)"
}

if [ "$(get_volume)" -ge 70 ]; then
    audio_icon="$audio_icon_high"
elif [ "$(get_volume)" -ge 30 ]; then
    audio_icon="$audio_icon_medium"
else
    audio_icon="$audio_icon_low"
fi

case $1 in
    up)
	# Set the volume on (if it was muted)
	amixer -q -D "$output_name" set Master on > /dev/null
	# Up the volume (+ 5%)
	amixer -q -D "$output_name" sset Master 5%+ > /dev/null
	send_notification
	;;
    down)
	amixer -q -D "$output_name" set Master on > /dev/null
	amixer -q -D "$output_name" sset Master 5%- > /dev/null
	send_notification
	;;
    mute)
    	# Toggle mute
	amixer -q -D "$output_name" set Master 1+ toggle > /dev/null
	if is_mute ; then
	    dunstify -i "$mute_icon" -t 1600 -h string:x-dunst-stack-tag:volume -u normal "Mute"
	else
	    send_notification
	fi
	;;
    mic)
        # Toggle mic
    amixer set Capture toggle > /dev/null
    get_mic_toggle
    ;;
esac

