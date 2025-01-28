class Text:
    def __init__(self, screen):
        self._screen = screen
        self._screen.clr()
        self._W, self._H, self._X0, self._Y0 = self._screen.info()

    def writelines(self, lines, border=False, X_offset=0, Y_offset=0):
        self._screen.clr()

        if border:
            self._screen.rect(self._X0, self._Y0, self._W, self._H, 1)
            X_offset += 2

        numlines = len(lines)
        if numlines == 1:
            self._screen.writer.write(lines[0], self._X0 + X_offset, self._Y0 + 18 + Y_offset)
        elif numlines == 2:
            self._screen.writer.write(lines[0], self._X0 + X_offset, self._Y0 + 8 + Y_offset)
            self._screen.writer.write(lines[1], self._X0 + X_offset, self._Y0 + 24 + Y_offset)
        elif numlines == 3 and not border:
            self._screen.writer.write(lines[0], self._X0 + X_offset, self._Y0)
            self._screen.writer.write(lines[1], self._X0 + X_offset, self._Y0 + 16)
            self._screen.writer.write(lines[2], self._X0 + X_offset, self._Y0 + 32)
        else:
            self._screen.writer.write("ERROR", self._X0 + 16, self._Y0 + 17)

        self._screen.show()
