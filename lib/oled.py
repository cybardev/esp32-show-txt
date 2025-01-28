from machine import Pin, I2C
from sh1106 import SH1106_I2C
from ezFBfont import ezFBfont
import ezFBfont_amstrad_cpc_extended_ascii_08 as ascii_font


class Screen(SH1106_I2C):
    W, H = 72, 40
    X0, Y0 = 28, 12

    def __init__(self):
        i2c = I2C(0, scl=Pin(6), sda=Pin(5), freq=400000)
        print(f"OLED at: {i2c}")
        print(f"Address: 0x{i2c.scan()[0]:02x}")

        super().__init__(
            self.X0 + self.W, (self.Y0 + self.H + 7) & 0xF8, i2c, rotate=180
        )
        self.clr()

        self.writer = ezFBfont(self, ascii_font)

    def clr(self):
        self.contrast(255)
        self.fill(0)

    def info(self):
        return self.W, self.H, self.X0, self.Y0
