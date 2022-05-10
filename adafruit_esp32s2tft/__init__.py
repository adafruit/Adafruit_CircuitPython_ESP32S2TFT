# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_esp32s2tft`
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

import gc
from adafruit_portalbase import PortalBase
from .network import Network
from .graphics import Graphics
from .peripherals import Peripherals

try:
    from typing import Optional, Dict, Union, Callable, Sequence, List
    from neopixel import NeoPixel
except ImportError:
    pass

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_ESP32S2TFT.git"


class ESP32S2TFT(PortalBase):
    """Class representing the Adafruit ESP32-S2 TFT Feather.

    :param url: The URL of your data source. Defaults to ``None``.
    :param headers: The headers for authentication, typically used by Azure API's.
    :param json_path: The list of json traversal to get data out of. Can be list of lists for
                      multiple data points. Defaults to ``None`` to not use json.
    :param regexp_path: The list of regexp strings to get data out (use a single regexp group). Can
                        be list of regexps for multiple data points. Defaults to ``None`` to not
                        use regexp.
    :param default_bg: The path to your default background image file or a hex color.
                       Defaults to 0x000000.
    :param status_dotstar: The initialized object for status DotStar. Defaults to ``None``,
                           to not use the status LED
    :param json_transform: A function or a list of functions to call with the parsed JSON.
                           Changes and additions are permitted for the ``dict`` object.
    :param rotation: Default rotation is landscape (270) but can be 0, 90, or 180 for
                     portrait/rotated
    :param scale: Default scale is 1, but can be an integer of 1 or greater
    :param debug: Turn on debug print outs. Defaults to False.
    :param use_network: Enable network initialization. Defaults to True.
                        Setting to False will allow you to use the library without a secrets.py
                        file with wifi configuration in it.

    """

    # pylint: disable=too-many-instance-attributes, too-many-locals, too-many-branches, too-many-statements
    def __init__(
        self,
        *,
        url: Optional[str] = None,
        headers: Dict[str, str] = None,
        json_path: Optional[Union[List[str], List[List[str]]]] = None,
        regexp_path: Optional[Sequence[str]] = None,
        default_bg: int = 0,
        status_neopixel: Optional[NeoPixel] = None,
        json_transform: Optional[Union[Callable, List[Callable]]] = None,
        rotation: int = 0,
        scale: int = 1,
        debug: bool = False,
        use_network: bool = True
    ) -> None:

        if use_network:
            network = Network(
                status_neopixel=status_neopixel,
                extract_values=False,
                debug=debug,
            )
        else:
            network = None

        graphics = Graphics(
            default_bg=default_bg,
            rotation=rotation,
            scale=scale,
            debug=debug,
        )

        super().__init__(
            network,
            graphics,
            url=url,
            headers=headers,
            json_path=json_path,
            regexp_path=regexp_path,
            json_transform=json_transform,
            debug=debug,
        )

        self.peripherals = Peripherals()

        gc.collect()

    def enter_light_sleep(self, sleep_time: float) -> None:
        """
        Enter light sleep and resume the program after a certain period of time.

        See https://circuitpython.readthedocs.io/en/latest/shared-bindings/alarm/index.html for more
        details.

        :param float sleep_time: The amount of time to sleep in seconds

        """
        if self._alarm:
            neopixel_value = self.peripherals.neopixel
            super().enter_light_sleep(sleep_time)
            self.peripherals.neopixel = neopixel_value
            gc.collect()
