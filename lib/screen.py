from machine import Pin, I2C
from sh1106 import SH1106_I2C


class Screen(SH1106_I2C):

  def __init__(self, width, height, x0=0, y0=0):
    self._w, self._h, self._x0, self._y0 = width, height, x0, y0
    self._i2c = I2C(0, scl=Pin(6), sda=Pin(5), freq=400000)
    super().__init__(x0 + width, (y0 + height + 7) & 0xF8, self._i2c, rotate=180)
    print(f"OLED at: {self._i2c}\nAddress: 0x{self._i2c.scan()[0]:02x}")
    self.brightness = 255
    self.fill(0)

  @property
  def W(self):
    return self._w

  @property
  def H(self):
    return self._h

  @property
  def origin(self):
    return self._x0, self._y0

  @property
  def brightness(self):
    return self._brightness

  @brightness.setter
  def brightness(self, value):
    if 0 <= value <= 255:
      self._brightness = value
      self.contrast(value)
    else:
      raise ValueError("Brightness out of range.")
