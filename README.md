# ESP32-C3 Configs

Scripts for _my_ ESP32-C3 board with 0.42" OLED display.

> [!NOTE]
> Given the variety of hardware even among the ESP32-C3 boards, the scripts here may or may not work for your board. Please proceed with caution.

<img src="https://github.com/user-attachments/assets/d23b6038-c374-4c32-9ec8-977612186967" width="360" alt="ESP32-C3 displaying Hello World on integrated screen" title="ESP32-C3" />

## Credits

- [robert-hh/SH1106](https://github.com/robert-hh/SH1106) for the [`sh1106`](./lib/sh1106.py) display driver
- [easytarget/microPyEZfonts](https://github.com/easytarget/microPyEZfonts) for the [`ezFBfont`](./lib/ezFBfont.py) font writer class, and the [`amstrad_cpc_extended`](./lib/ezFBfont_amstrad_cpc_extended_ascii_08.py) font

> [!IMPORTANT]
> The above modules have their own licenses. Check the linked repositories for more information.
