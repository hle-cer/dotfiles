
#                                           #                               
##     █▀▀ █▀█ █▄░█ █▀▀ █ █▀▀ ░ █▀█ █▄█    ##
##     █▄▄ █▄█ █░▀█ █▀░ █ █▄█ ▄ █▀▀ ░█░    ##
#                                           #

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

decoration_group = {
    "decorations": [
        RectDecoration(colour="#232831", radius=10, filled=True, padding_y=2, padding_x=0, group=True)
    ],
    "padding": 10,
}

mod = "mod4"
terminal = guess_terminal()

keys = [
    # rofi #
    Key([mod,], "m", lazy.spawn(os.path.expanduser("~/.config/rofi/rofi.sh")), desc="rofi"),
    # scrot #
    Key([mod, "shift"], "t", lazy.spawn(os.path.expanduser("~/screenshot")), desc="scrot"),
    # qemu #
    Key([mod, "shift"], "b", lazy.spawn(os.path.expanduser("~/win10.sh")), desc="WindowsVM"),
    # mouse accel #
    Key([mod], "[", lazy.spawn(os.path.expanduser("mouse.sh")), desc="remove mouse accel"),
    # Switch between window
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawcmd(), desc="Spawn a command using a prompt widget"),
]

#groups = [Group(i) for i in "asdfuiop"]

groups = [
    Group('a', label = "1"),
    Group('s', label = "2"),
    Group('d', label = "3"),
    Group('f', label = "4"),
    Group('u', label = "5"),
    Group('i', label = "6"),
    Group('o', label = "7"),
    Group('p', label = "8"),

    ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
           ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            #Key(
            #    [mod, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(i.name),
            #),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                 desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_width=2,
                   font = "Inconsolata LGC Nerd Font",
                   margin = 3,
                   border_focus = '#cba6f7',
                   border_normal = '494949',
                   border_on_single=True,
                   ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    #layout.RatioTile(margin = 8),
    #layout.Max(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Inconsolata LGC Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(        bottom=bar.Gap(3),
                   left=bar.Gap(3),
                   right=bar.Gap(3),
        top=bar.Bar(
            [

                            ## Widgets ##

                widget.GroupBox(highlight_method='text',
                                rounded = False,
                                disable_drag = True,
                                active = "#979797",
                                inactive="#494949",
                                this_current_screen_border="#cba6f7",
                                #block_highlight_text_color="#a6e3a1",
                                #highlight_color=['1e1e2e', '1e1e2e'],
                                margin_y = 2,
                                margin_x = 0,
                                padding_y = 5,
                                padding_x = 5,
                                fontsize = 18,
                                font = "Inconsolata LGC Nerd Font",
                                ),
                widget.Spacer(20),
                widget.WindowTabs(),

                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    ),
                
                
                #widget.Pomodoro(color_active = '#ffffff',
                #                color_break = '#ffffff',
                #                color_inactive = '#ffffff',
                #                length_pomodori = 45,
                #                length_short_break = 10,
                #                length_long_break = 20),
                #widget.CPUGraph(border_width = 0, type='line', line_width=1, graph_color = '#ffffff', margin_y = 6),
                #widget.MemoryGraph(border_width = 0, type='line', line_width=1, graph_color = '#ffffff', margin_y = 6),
                widget.Sep(),
                widget.Spacer(length=10),
                widget.CPU(),
                widget.Spacer(length=5),
                widget.Memory(),
                widget.Spacer(length=10),
                widget.NvidiaSensors(),
                widget.Spacer(length=10),
                widget.Sep(),
                widget.Spacer(length=5),
                widget.Systray(),
                widget.Spacer(length=10),
                widget.Volume(),
                widget.Spacer(length=10),
                widget.Clock(format="%I:%M %p  %d-%m"),
                widget.Spacer(length=10),
                widget.CurrentLayoutIcon(scale=0.7, background = "#cba6f7"),
            ],
            28,
            background = '#1e1e2e',
            margin = [6,6,3,6],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "qtile"

    ## autostart ##

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
