###################################################
##################### My qTile ####################
###################################################

# Importing python/qtile libraries:

import os
import re
import socket
import subprocess
import os.path
from libqtile.config import Key, Screen, Group, Match, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer, base
from typing import List  # noqa: F401

# Set Default modkey:
mod = "mod4"

keys = [

    # Cahnge Focus:
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    # Swap places:
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "w", lazy.to_screen(0)),
    Key([mod], "y", lazy.to_screen(1)),
    Key([mod, "shift"], "w", lazy.window.to_screen(0)),
    Key([mod, "shift"], "y", lazy.window.to_screen(1)),


    # Resize keys:
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    # Move the master pane Left/Right:
    Key([mod, "shift"], "space", lazy.layout.flip()),
    # Toggel fullscreen on/off:
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # Change Layout:
    Key([mod], "Tab", lazy.next_layout()),
    # Close focused window:
    Key([mod, "shift"], "q", lazy.window.kill()),

    # Restart qtile in place:
    Key([mod, "control"], "r", lazy.restart()),

    # Open a run prompt:
    Key([mod], "r", lazy.spawncmd()),

    # Applications/Scripts Shortcuts:
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "p", lazy.spawn("./Scripts/pmenu.sh")),
    Key([mod, "shift"], "f", lazy.spawn("firefox")),
    Key([mod, "shift"], "e", lazy.spawn("emacs")),
    Key([mod, "shift"], "t", lazy.spawn("thunderbird")),
    Key([mod, "shift"], "b", lazy.spawn("thunar")),
    Key([mod], "d", lazy.spawn("rofi -show run")),
    Key([mod, "shift"], "p", lazy.spawn("./Scripts/pdfs.sh")),

    # Backlight control:
    Key([mod], "Down", lazy.spawn("light -U 5")),
    Key([mod], "Up", lazy.spawn("light -A 5")),

    # Volume control:
    Key([mod], "Left", lazy.spawn("amixer -c 0 -q set Master 2dB-")),
    Key([mod], "Right", lazy.spawn("amixer -c 0 -q set Master 2dB+")),

    # Change keyboard layout:
    Key([mod], "space", lazy.spawn("./Scripts/kbdlayout.sh")),
]


groups = [
    Group(
        "1",
        label=""
    ),
    Group(
        "2",
        matches=[Match(wm_class=["firefox"])],
        label=""
    ),
    Group(
        "3",
        matches=[Match(wm_class=["Emacs"])],
        label=""
    ),
    Group(
        "4",
        matches=[Match(wm_class=["libreoffice"])],
        label=""
    ),
    Group(
        "5",
        matches=[Match(wm_class=["Thunderbird"])],
        label=""
    ),
    Group(
        "6",
        matches=[Match(wm_class=["code-oss"])],
        label=""
    ),
    Group(
        "7",
        label=""
    ),
    ]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(
        border_focus = "5e81ac",
        border_normal = "b48ead",
        border_width = 3,
        margin = 5,
    ),
    layout.MonadWide(
        border_focus = "5e81ac",
        border_normal = "b48ead",
        border_width = 3,
        margin = 5,
    ),
]

widget_defaults = dict(
    font='Cascadia Code',
    fontsize=14,
    padding=4,
    background="2e3440",
    foreground="5e81ac",
)
extension_defaults = widget_defaults.copy()

def get_bar():
    return bar.Bar([
       widget.GroupBox(
           active = "5e81ac",
           inactive = "b48ead",
           this_current_screen_border = "bf616a",
           highlight_method = "line",
           highlight_color=["2e3440", "2e3440"],
           center_aligned=True,
       ),
       widget.Prompt(
           prompt='Run:',
       ),
       widget.TextBox(
           text='|',
           foreground="bf6a6a"
       ),
       widget.TaskList(
           foreground = "2e3440",
           border = "5e81ac",
           fontsize = 11,
           unfocused_border = "b48ead",
           highlight_method = "block",
           max_title_width=100,
           title_width_method="uniform",
           icon_size = 13,
           rounded=False,
       ),
       widget.Systray(
       ),
       widget.TextBox(
           text='|',
           foreground="8fbcbb",
       ),
       widget.TextBox(
           text='',
           foreground="8fbcbb",
       ),
       widget.KeyboardLayout(
           foreground="8fbcbb",
       ),
       widget.TextBox(
           text='|',
           foreground="ebcb8b",
       ),
       widget.TextBox(
           text='',
           foreground="ebcb8b",
       ),
       widget.Volume(
           foreground="ebcb8b",
       ),
       widget.TextBox(
           text='|',
           foreground="88c0d0",
       ),
       widget.TextBox(
           text='',
           foreground="88c0d0",
       ),
       widget.Backlight(
           foreground="88c0d0",
           backlight_name="intel_backlight",
       ),
       widget.TextBox(
           text='|',
           foreground="a3be8c",
       ),
       widget.TextBox(
           text='',
           foreground="a3be8c",
       ),
       widget.Clock(
           format='%a %I:%M',
           foreground = "a3be8c",
       ),
       widget.TextBox(
           text='|',
           foreground="bf6a6a",
       ),
       widget.TextBox(
           text='',
           foreground="bf6a6a",
       ),
       widget.Wlan(
           foreground="bf6a6a",
           interface="wlp3s0",
           format="{essid}",
       ),
    ], 26)


screens = [
    Screen(top=get_bar()),
    Screen(),
]
            
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
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

wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])



