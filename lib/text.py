class Text:
    def __init__(self, screen):
        self._screen = screen
        self._screen.clr()
        self._W, self._H, self._X0, self._Y0 = self._screen.info()

    def writeline(self, line, X_offset, Y_offset):
        self._screen.writer.write(line, self._X0 + X_offset, self._Y0 + Y_offset)

    def writelines(self, lines, border=False, X_offset=0, Y_offset=0):
        self._screen.clr()

        if border:
            self._screen.rect(self._X0, self._Y0, self._W, self._H, 1)
            X_offset += 2

        numlines = len(lines)
        if numlines == 1:
            self.writeline(lines[0], X_offset, Y_offset + 18)
        elif numlines == 2:
            self.writeline(lines[0], X_offset, Y_offset + 8)
            self.writeline(lines[1], X_offset, Y_offset + 24)
        elif numlines == 3 and not border:
            self.writeline(lines[0], X_offset, 0)
            self.writeline(lines[1], X_offset, 16)
            self.writeline(lines[2], X_offset, 32)
        else:
            self.writeline("ERROR", 16, 17)

        self._screen.show()
