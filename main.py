from lib.oled import Screen
from lib.text import Text

screen = Screen()
txt = Text(screen)
txt.writelines(["Henlo,", "Wrold~ :3"], border=True, x_offset=1)
