Introduction
============


.. image:: https://readthedocs.org/projects/adafruit-circuitpython-esp32s2tft/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/esp32s2tft/en/latest/
    :alt: Documentation Status


.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/adafruit/Adafruit_CircuitPython_ESP32S2TFT/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_ESP32S2TFT/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Helper library for the Adafruit ESP32-S2 TFT Feather.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Adafruit ESP32-S2 TFT Feather

`Purchase one from the Adafruit shop <http://www.adafruit.com/products/5300>`_


Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install adafruit_esp32s2tft

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code:: python

    import random
    from rainbowio import colorwheel
    from adafruit_esp32s2tft import ESP32S2TFT

    esp32s2tft = ESP32S2TFT(
        default_bg=0xFFFF00,
        scale=2,
    )

    # Create the labels
    esp32s2tft.add_text(
        text="ESP32-S2", text_position=(10, 10), text_scale=2, text_color=0xFF00FF
    )
    esp32s2tft.add_text(
        text="TFT Feather",
        text_position=(60, 30),
        text_anchor_point=(0.5, 0.5),
        text_color=0xFF00FF,
    )
    button_label = esp32s2tft.add_text(
        text="Press BOOT0 Button",
        line_spacing=1.0,
        text_position=(60, 50),
        text_anchor_point=(0.5, 0.5),
        text_color=0x606060,
    )
    esp32s2tft.display.show(esp32s2tft.splash)

    while True:
        esp32s2tft.set_text_color(
            0xFF0000 if esp32s2tft.peripherals.button else 0x606060, button_label
        )
        esp32s2tft.peripherals.led = esp32s2tft.peripherals.button
        if esp32s2tft.peripherals.button:
            esp32s2tft.peripherals.neopixel[0] = colorwheel(random.randint(0, 255))


Documentation
=============
API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/esp32s2tft/en/latest/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_ESP32S2TFT/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
