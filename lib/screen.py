from machine import Pin, I2C
from sh1106 import SH1106_I2C


class Screen(SH1106_I2C):

  def __init__(self, width, height, x0=0, y0=0):
    self._x0, self._y0 = x0, y0
    self._i2c = I2C(0, scl=Pin(6), sda=Pin(5), freq=400000)
    super().__init__(x0 + width, (y0 + height + 7) & 0xF8, self._i2c, rotate=180)
    print(f"OLED at: {self._i2c}\nAddress: 0x{self._i2c.scan()[0]:02x}")
    self.contrast(255)
    self.fill(0)

  @property
  def origin(self):
    return self._x0, self._y0
