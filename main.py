from lib.oled import Screen

screen = Screen()
W, H, X0, Y0 = screen.info()

screen.rect(X0, Y0, W, H, 1)
screen.text("Henlo,", X0 + 4, Y0 + 8)
screen.text("Wrold~:3", X0 + 4, Y0 + 24)
screen.show()
