# SpicyLights

Python scripts to reflect cab lights on a neopixel-compatible LED device via Spice API. Interpolates the received light data to allow for smooth animations.

<img src="https://scontent.fscn1-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/34301627_1848528738781629_5969480435170803712_n.jpg?_nc_cat=111&ccb=2&_nc_sid=2d5d41&_nc_ohc=pTj8_qWriR4AX_iigfN&_nc_ht=scontent.fscn1-1.fna&tp=14&oh=e1d07d522c7f40b32ed17eed7abd4468&oe=6014E2C5" width="350"/>

## Setup

This is tested on a Raspberry Pi Zero W. The Neopixel data line should be connected to GPIO 18, this however can be changed in ``start.py``.

Set up your IP and credentials for SpiceAPI, as well as the amount of LEDs, in ``config.py``.

Place the ``api/python/spiceapi`` folder from a distributed spice zip in the same folder as ``start.py``. Install ``requirements.txt``.

<br>

It is recommended to create a systemd service for this script.
