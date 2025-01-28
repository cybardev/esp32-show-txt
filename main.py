from lib.oled import Screen

screen = Screen()
W, H, X0, Y0 = screen.info()

screen.rect(X0, Y0, W, H, 1)
screen.writer.write("Henlo,", X0 + 4, Y0 + 8)
screen.writer.write("Wrold~ :3", X0 + 4, Y0 + 24)
screen.show()
