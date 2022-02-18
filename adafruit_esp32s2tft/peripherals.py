# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_esp32s2tft.peripherals`
================================================================================

Helper library for the Adafruit ESP32-S2 TFT Feather.


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Adafruit ESP32-S2 TFT Feather <https://www.adafruit.com/product/5300>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's PortalBase library: https://github.com/adafruit/Adafruit_CircuitPython_PortalBase

"""

import board
from digitalio import DigitalInOut, Direction, Pull
import neopixel


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_ESP32S2TFT.git"


class Peripherals:
    """Peripherals Helper Class for the ESP32S2TFT Library


    Attributes:
        neopixel (Neopixel): The on-board NeoPixel.
            See https://circuitpython.readthedocs.io/projects/neopixel/en/latest/api.html
    """

    # pylint: disable=too-many-instance-attributes, too-many-locals, too-many-branches, too-many-statements
    def __init__(self) -> None:
        # Neopixel
        self.neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3)

        # Button
        self._button = None
        if hasattr(board, "BUTTON"):
            # Only CircuitPython 7.2 or later has Button
            self._button = DigitalInOut(board.BUTTON)
            self._button.direction = Direction.INPUT
            self._button.pull = Pull.UP

        # LED
        self._led = DigitalInOut(board.LED)
        self._led.switch_to_output()

    def deinit(self) -> None:
        """Call deinit on all resources to free them"""
        self.neopixel.deinit()
        self._button.deinit()
        self._led.deinit()

    @property
    def button(self) -> bool:
        """
        Return whether Down Button is pressed
        """
        if self._button:
            return not self._button.value
        return False

    @property
    def led(self) -> bool:
        """
        Return or set the value of the LED
        """
        return self._led.value

    @led.setter
    def led(self, value: bool) -> None:
        self._led.value = bool(value)
