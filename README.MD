# SpicyLights

Python scripts to reflect cab lights on a neopixel-compatible LED device via Spice API. Interpolates the received light data to allow for smooth animations.

## Setup

This is tested on a Raspberry Pi Zero W. The Neopixel data line should be connected to GPIO 18, this however can be changed in ``start.py``.

Set up your IP and credentials for SpiceAPI, as well as the amount of LEDs, in ``config.py``.

Place the ``api/python/spiceapi`` folder from a distributed spice zip in the same folder as ``start.py``. Install ``requirements.txt``.

<br>

It is recommended to create a systemd service for this script.