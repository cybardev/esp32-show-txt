from machine import Pin, I2C
from sh1106 import SH1106_I2C
from ezFBfont import ezFBfont
import ezFBfont_amstrad_cpc_extended_ascii_08 as ascii_font


class Screen(SH1106_I2C):
    def __init__(self, W=72, H=40, X0=28, Y0=12, font=ascii_font):
        self._W, self._H, self._X0, self._Y0 = W, H, X0, Y0
        self._i2c = I2C(0, scl=Pin(6), sda=Pin(5), freq=400000)
        super().__init__(self._X0 + self._W, (self._Y0 + self._H + 7) & 0xF8, self._i2c, rotate=180)
        self.writer = font
        self.clr()
        print(self)

    @property
    def writer(self):
        return self._writer

    @writer.setter
    def writer(self, font):
        self._writer = ezFBfont(self, font)

    def clr(self):
        self.contrast(255)
        self.fill(0)

    def info(self):
        return self._W, self._H, self._X0, self._Y0

    def __str__(self):
        return f"OLED at: {self._i2c}\nAddress: 0x{self._i2c.scan()[0]:02x}"
