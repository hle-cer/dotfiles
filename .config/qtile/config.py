# Importing necessary libraries
import os
import subprocess
import dbus_next
from keybindings import keys
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

# Colors
main = '#7aa2f7'
sec = '#f7768e'
forg = '#9aa5ce'
bg = '#1a1b26'

decoration_group = {
    "decorations": [
        RectDecoration(colour=bg, radius=10, filled=True, padding_y=0, group=True)
    ],
    "padding": 10,
}

# Variables
mod = "mod4"
terminal = "alacritty"
browser = "firefox"

# Groups
groups = [
    Group('a', label=""),
    Group('s', label=""),
    Group('d', label=""),
    Group('f', label="󰙯"),
    Group('u', label=""),
    Group('i', label=""),
    Group('o', label=""),
    Group('p', label=""),
]

# Keybindings for switching between groups
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), desc="Move focused window to group {}".format(i.name)),
    ])

# Layouts
layouts = [
    layout.Columns(
        border_width=2,
        font="JetBrainsMono Nerd Font",
        margin=3,
        border_focus=main,
        border_normal='494949',
        border_on_single=True,
    ),
    layout.Max(),
]

# Default widget settings
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=3,
    foreground=forg
)

extension_defaults = widget_defaults.copy()

# Screens configuration
screens = [
    Screen(
        bottom=bar.Gap(3),
        left=bar.Gap(3),
        right=bar.Gap(3),
        top=bar.Bar(
            [
                # Workspaces
                widget.GroupBox(
                    highlight_method='text',
                    rounded=False,
                    disable_drag=True,
                    active="#979797",
                    inactive="#494949",
                    this_current_screen_border=main,
                    margin_y=2,
                    margin_x=0,
                    padding_y=0,
                    fontsize=20,
                    font="JetBrainsMono Nerd Font",
                    **decoration_group
                ),
                widget.Spacer(10),

                # System tray
                widget.Systray(),
                widget.Spacer(),

                # Clock
                widget.Clock(
                    format=" %H:%M  %b %d",
                    **decoration_group
                ),
                widget.Spacer(),

                # Connection info
                widget.Wlan(
                    format='  {essid}',
                    **decoration_group
                ),
                widget.Spacer(5),

                # Volume
                widget.Volume(
                    fmt='󰕾 {}',
                    **decoration_group
                ),
                widget.Spacer(5),

                # Battery (install upower)
                widget.Spacer(10, **decoration_group),
                widget.UPowerWidget(
                    border_colour=forg,
                    border_critical_colour='#f7768e',
                    border_charge_colour=forg,
                    fill_normal=forg,
                    fill_critical=forg,
                    fill_low=forg,
                    text_charging='({percentage:.0f}%)󰚥 ',
                    text_discharging='{percentage:.0f}% ',
                    **decoration_group
                ),
                widget.Spacer(10, **decoration_group),
            ],
            28,
            background='#00000000',
            margin=[6, 6, 3, 6],
        ),
    ),
]

# Drag floating layouts
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Floating layout rules
floating_layout = layout.Floating(
    font="JetBrainsMono Nerd Font",
    border_focus=main,
    border_normal='494949',
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="feh"), # image viewer
        Match(wm_class="qvidcap"), # QT video capture
        Match(wm_class="blueman-manager"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Other configurations
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "qtile"

# Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
