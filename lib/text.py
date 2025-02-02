class Text:

  def __init__(self, screen):
    self._screen = screen
    self._screen.clr()
    self._width, self._height, self._x0, self._y0 = self._screen.info()

  def writeline(self, line, x_offset, y_offset):
    self._screen.writer.write(line, self._x0 + x_offset, self._y0 + y_offset)

  def writelines(self, lines, border=False, x_offset=0, y_offset=0):
    self._screen.clr()

    if border:
      self._screen.rect(self._x0, self._y0, self._width, self._height, 1)
      x_offset += 2

    numlines = len(lines)
    if numlines == 1:
      self.writeline(lines[0], x_offset, y_offset + 18)
    elif numlines == 2:
      self.writeline(lines[0], x_offset, y_offset + 8)
      self.writeline(lines[1], x_offset, y_offset + 24)
    elif numlines == 3 and not border:
      self.writeline(lines[0], x_offset, 0)
      self.writeline(lines[1], x_offset, 16)
      self.writeline(lines[2], x_offset, 32)
    else:
      self.writeline("ERROR", 16, 17)

    self._screen.show()
