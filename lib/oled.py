from machine import Pin, I2C
from sh1106 import SH1106_I2C
from ezFBfont import ezFBfont
import ezFBfont_amstrad_cpc_extended_ascii_08 as ascii_font


class Screen(SH1106_I2C):

  def __init__(self, width=72, height=40, x0=28, y0=12, font=ascii_font):
    self._width, self._height, self._x0, self._y0 = width, height, x0, y0
    self._i2c = I2C(0, scl=Pin(6), sda=Pin(5), freq=400000)
    super().__init__(self._x0 + self._width, (self._y0 + self._height + 7) & 0xF8, self._i2c, rotate=180)
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
    return self._width, self._height, self._x0, self._y0

  def __str__(self):
    return f"OLED at: {self._i2c}\nAddress: 0x{self._i2c.scan()[0]:02x}"
