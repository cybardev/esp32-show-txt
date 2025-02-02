from ezFBfont import ezFBfont


class Text:

  def __init__(self, screen, font):
    self.screen = screen
    self.screen.fill(0)
    self.writer = font

  @property
  def screen(self):
    return self._screen

  @screen.setter
  def screen(self, new_screen):
    self._screen = new_screen
    try:
      self._x0, self._y0 = new_screen.origin
    except AttributeError:
      self._x0, self._y0 = 0, 0

  @property
  def writer(self):
    return self._writer

  @writer.setter
  def writer(self, font):
    self._writer = ezFBfont(self.screen, font)

  def writeline(self, line, x_offset=0, y_offset=0):
    self.writer.write(line, self._x0 + x_offset, self._y0 + y_offset)

  def writelines(self, lines, border=False, x_offset=0, y_offset=0):
    self.screen.fill(0)

    if border:
      self.screen.rect(self._x0, self._y0, self.screen.width, self.screen.height, 1)
      x_offset += 2

    numlines = len(lines)
    if numlines == 1:
      self.writeline(lines[0], x_offset, y_offset + 18)
    elif numlines == 2:
      for i in range(2):
        self.writeline(lines[i], x_offset, 8 + (16 * i))
    elif numlines == 3 and not border:
      for i in range(3):
        self.writeline(lines[i], x_offset, 16 * i)
    else:
      self.writeline("ERROR", 16, 17)

    self.screen.show()
