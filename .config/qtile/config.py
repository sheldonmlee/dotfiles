# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile import layout, bar, widget

from typing import List  # noqa: F401

from libqtile import hook
import os
import subprocess

mod = "mod4"

up = "k"
down = "j"
left = "h"
right = "l"

terminal="alacritty"
browser="firefox"

print("hi")

# hooks
path = os.path.expanduser("~/.config/qtile/")
dumpfile = path+"dumpfile.txt"
def filedump(string):
    file_handle = open(dumpfile, "a")
    file_handle.write(string)
    file_handle.close()

@hook.subscribe.startup
def startup():
    file_handle = open(dumpfile, "w")
    file_handle.write("")
    file_handle.close()

@hook.subscribe.client_new
def newClient(window):
    filedump(window.name+'\n')

@hook.subscribe.client_focus
def layoutChange(window):
    filedump("focused: "+window.name+"\n")

def customFunction(qtile):
    filedump("customFunction called.\n")
    # below words if using f_scrot fullscreen screenshot
    subprocess.call([path+"screenshot.sh"])

keys = [
    # Switch between windows in current stack pane (also up or down a stack pane)
    Key([mod], up, lazy.layout.up()),
    Key([mod], down, lazy.layout.down()),
    Key([mod], left, lazy.layout.left()),
    Key([mod], right, lazy.layout.right()),
    # Grow 
    Key([mod, "shift"], up, lazy.layout.grow()),
    Key([mod, "shift"], down, lazy.layout.shrink()),
    Key([mod, "shift"], left, lazy.layout.shrink_main()),
    Key([mod, "shift"], right, lazy.layout.grow_main()),
    # Move windows up or down in current stack
    Key([mod, "control"], up, lazy.layout.shuffle_up()),
    Key([mod, "control"], down, lazy.layout.shuffle_down()),
    # Move windows left or right in current stack
    Key([mod, "control"], left, lazy.layout.shuffle_left()),
    Key([mod, "control"], right, lazy.layout.shuffle_right()),

    # Switch window focus to other pane(s) of stack
    Key(["mod1"], "Tab", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "b", lazy.spawn(browser)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),

    Key([mod], "r", lazy.spawncmd()),

    Key(["mod1"], "l", lazy.spawn("xlock")),
    Key([mod], "x", lazy.function(customFunction)),
]
# theme
import color_themes
theme_colors = color_themes.solarized()

layout_theme = {
        "border_width": 1,
        "margin": 5,
        "border_focus": theme_colors["r"],
        "border_normal": theme_colors["g"],
        }

#arrays for group parameters
groups = [
    Group("a", label="term", spawn=terminal),
    Group("s", label="media", spawn=browser),
    Group("d", label="social", spawn="discord"),
    Group("f", label="misc", layouts=[layout.Floating(**layout_theme), layout.Max(**layout_theme)])
    ]

for group in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], group.name, lazy.group[group.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])
# scratchpad dropdown menu thing
groups.extend([
    ScratchPad( "scratchpad", [
        DropDown("term", "xterm", opacity=0.8),
        ])
    ])

keys.extend([
        Key([mod], "space", lazy.group["scratchpad"].dropdown_toggle("term")),
    ])


layouts = [
     layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(margin=4),
    # layout.Columns(),
    # layout.Matrix(),
     layout.MonadTall(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="couriernew",
    fontsize=16,
    padding=5,
    background=theme_colors["bg"],
    foreground=theme_colors["fg"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=theme_colors["g"],
                    inactive=theme_colors["fg"],
                    highlight_method="block",
                    this_current_screen_border=theme_colors["g"],
                    block_highlight_text_color=theme_colors["bg"],
                    urgent_border=theme_colors["r"],
                    urgent_text=theme_colors["bg"],
                    ),
                widget.Sep(),
                widget.CurrentLayout(padding=10, foreground=theme_colors["r"]),
                widget.Prompt(),
                #widget.WindowName(),
                widget.Spacer(),
                #widget.TextBox("oof config", name="default"),
                widget.Systray(),
                widget.Sep(linewidth=0, padding=10),
                widget.Volume(foreground=theme_colors["b"]),
                widget.Clock(format='%d-%m-%y %a %H:%M:%S'),
                #widget.QuickExit(),
            ],
            32,
            margin=[5,5,5,5],
            #opacity=0.8,
        ),
        bottom=bar.Gap(5),
        left=bar.Gap(5),
        right=bar.Gap(5),
        wallpaper='~/wallpaper/ff.jpg',
        wallpaper_mode='fill',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Click([mod, "control"], "Button1", lazy.window.toggle_floating()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
