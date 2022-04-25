
# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers








#groups = [Group(i) for i in [
##    "   ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", "   ",
#   "   ", " ﲵ  ", "   ", "   ", "  ", " 華  ", "   ", "  ", "  ", 
#]]
#for i, group in enumerate(groups):
#    actual_key = str(i + 1)
#    keys.extend([
#        # Switch to workspace N
#        Key([mod], actual_key, lazy.group[group.name].toscreen()),
#        # Send window to workspace N
#        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
#    ])



#--------------------- OTRO PAPA PROBAR

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

group_labels = ["  ", " ﲵ ", "  ", "  ", "  ", " 華", "  ", "  ", "  ", "  ",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "treetab", "floating",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])
