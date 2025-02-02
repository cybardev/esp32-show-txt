import lib.ezFBfont_amstrad_cpc_extended_ascii_08 as font
from lib.screen import Screen
from lib.text import Text

scrn = Screen(72, 40, x0=28, y0=12)
txt = Text(scrn, font)
txt.writelines(["Henlo,", "Wrold~ :3"], border=True, x_offset=1)
