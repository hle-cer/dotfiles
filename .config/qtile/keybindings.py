# Imports
import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"
browser = "firefox"


keys = [

    # Rofi
    Key([mod], "m", lazy.spawn(os.path.expanduser("rofi -show drun")), desc="rofi"),
    Key([mod, "control"], "m", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/powermenu")), desc="rofi power menu"),
    Key([mod, "shift"], "m", lazy.spawn(os.path.expanduser("rofi -show calc")), desc="rofi calc"),
    Key(["mod1"], "Tab", lazy.spawn(os.path.expanduser("rofi -show window")), desc="rofi window"),

    # Player
    Key([mod], "down", lazy.spawn(os.path.expanduser("playerctl play-pause")), desc="play/pause"),
    Key([mod], "right", lazy.spawn(os.path.expanduser("playerctl next")), desc="next"),
    Key([mod], "left", lazy.spawn(os.path.expanduser("playerctl previous")), desc="prev"),
    Key([mod], "up", lazy.spawn(os.path.expanduser("playerctl open")), desc="open"),    

    # Volume
    Key([], "XF86AudioMicMute", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/volume.sh mic")), desc="mute/unmute mic"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/volume.sh up")), desc="vol up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/volume.sh down")), desc="vol down"),
    Key([], "XF86AudioMute", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/volume.sh mute")), desc="mute/unmute"),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/brightness.sh up")), desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/brightness.sh down")), desc="Brightness down"),

    # Scrot
    Key([], "Print", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/screenshot.sh ")), desc="normal screenshot"),
    Key(["shift"], "Print", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/screenshot.sh select")), desc="selection screenshot"),
    Key(["control"], "Print", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/screenshot.sh window")), desc="window screenshot"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn(browser), desc="Launch browser"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Layouts
    Key([mod], "1", lazy.window.toggle_floating(), desc="Toggle floating layout"),
    Key([mod], "2", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen layout"),
    Key([mod], "3", lazy.window.toggle_minimize(), desc="Toggle minimization on focused window"),

    Key([], "XF86LaunchA", lazy.spawn(os.path.expanduser("unclutter -idle 0")), desc="rofi"),
]
