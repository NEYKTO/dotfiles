
# Multimonitor support

from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 28, opacity=1.0)

def status_bar_b(widgets):
    return bar.Bar(widgets, 28, opacity=1.0, padding=50)

screens = [
#	Screen(top=status_bar(primary_widgets)),
#         Screen(bottom=status_bar(primary_widgets))
#]
        Screen(top=status_bar(primary_widgets),

               bottom=status_bar_b(secondary_widgets))
]












xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(bottom=status_bar(secondary_widgets)))
