from libqtile import widget
from .theme import colors
#import battery



import subprocess
from libqtile.widget import base


import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal




#------------------------------
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg],
        #        'foregeound_alert': color[af],
#	'background':["#000000.00"]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=10)


def icon(fg='rojo', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=1
    )


def powerline(fg="azul", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=42,
        padding=-3
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='azul'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=18, padding=5,font='iosevka regular'),
        separator(),
    ]


def workspaces_b():
    return [
        separator(),
        separator(),
        widget.WindowName(**base(fg='azul'), padding=5,
        font='iosevka regular',
        fontsize=20,
        ),
        separator(),
    ]

primary_widgets = [
    *workspaces(),

    separator(),
    powerline('temp5','dark'),

    widget.Wttr(**base(bg='temp5',fg='blanco'),
    lang='es',
    location={
	'Reus': 'Reus',
#	'41.15883703110864, 1.1074393937575309': 'Reus',
#        '64.127146,-21.873472': 'Reykjavik',
#        '~Vostok Station': 'Nice place',
	},
	format='%m %M',
	units='m',
	update_interval=30,
	fontsize=16, font='iosevka regular',
    ),

    powerline('temp4','temp5'),
    widget.Wttr(**base(bg='temp4',fg='blanco'),
	lang='es',
	location={'Reus':'Reus', },
	format='%w %c  ',
	units='m',
	update_interval=30,
	fontsize=16, font='iosevka regular',
	),

	powerline('temp3','temp4'),
	widget.Wttr(**base(bg='temp3',fg='blanco'),
	lang='es',
	location={'Reus':'Reus',},
	format='T: %t Rf: %f  ',
	units='m',
	update_interval=15,
	fontsize=16, font='iosevka regular',
	),

    powerline('temp2','temp3'),
    widget.Wttr(**base(bg='temp2',fg='blanco'),
        lang='es',
	location={'Reus':'Reus', },
	format=' %P  ',
	units='m',
	update_interval=30,
	fontsize=16, font='iosevka regular',
    ),
    powerline('temp1','temp2'),
    widget.Wttr(**base(bg='temp1',fg='blanco'),
        lang='es',
	location={'Reus':'Reus', },
	format=' H: %h  ',
	units='m',
	update_interval=30,
	fontsize=16, font='iosevka regular',
	),

# hay que dublicar el codigo de weather

    powerline('oceano', 'temp1'),
    widget.CurrentLayoutIcon(**base(bg='oceano',fg='blanco'), scale=0.65),
    powerline('rosa', 'oceano'),
    icon(bg="rosa",fg="blanco", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='rosa',fg='blanco'), format='%d/%m-%H:%M:%S ', fontsize=16, font='iosevka regular'),
    powerline('dark', 'rosa'),


]

secondary_widgets = [
	*workspaces_b(),

	separator(),
	powerline('color4', 'dark'),
	widget.Net(**base(bg='color4', fg='blanco'), scale=20.65, padding=25,
	font='iosevka regular',
	fontsize=14,
	margin_y=3,
	margin_x=0,
	padding_y=8,
	padding_x=5),


	powerline('verde', 'color4'),
	widget.CPU(**base(bg='verde', fg='blanco'), scale=0.65, padding=5,font='iosevka regular',
		fontsize=14,margin_y=3,margin_x=0,padding_y=8,padding_x=5,

	),


	powerline('rojo', 'verde'),
	widget.Memory(**base(bg='rojo', fg='blanco'), 
		format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}/{MemPercent: .0f}% /{Buffers: .0f}{mm}' ,font='iosevka regular',
		fontsize=14,margin_y=3,margin_x=0,padding_y=8,padding_x=5
	),

	powerline('naranja', 'rojo'),
	icon(bg="naranja", fg="blanco", text=' '), # Icon: nf-fa-download  --UPDATES SYS
	widget.CheckUpdates(
		font='iosevka regular',
		scale=10.65,
		padding=5,
		background=colors['naranja'],
		colour_have_updates=colors['blanco'],
		colour_no_updates=colors['azul'],
		no_update_string='0',
		display_format='{updates}',
		update_interval=1800,
		custom_command='checkupdates',
	),


]



widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

