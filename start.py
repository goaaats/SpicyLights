try:
    import spiceapi
except ModuleNotFoundError:
    raise RuntimeError("spiceapi module not installed")

import serial
import time
import math
from fader import Fader
import threading
import board
import neopixel
import config

fader = Fader(config.FADE_PERIOD_MS)

apiR = 255
apiG = 0
apiB = 0

lastR = 0
lastG = 255
lastB = 0

pixels = neopixel.NeoPixel(board.D18, config.NUM_LIGHTS)

while True:
    try:
        connection = spiceapi.Connection(
            host=config.SPICEAPI_HOST, port=config.SPICEAPI_PORT, password=config.SPICEAPI_PASS)

        break
    except OSError as e:
        print("Connection Error", "Failed to connect: " + str(e))
        time.sleep(1.0)

def api_update():
    while True:
        global apiR
        global apiG
        global apiB

        global lastR
        global lastG
        global lastB

        global fader

        # Read lights from spiceapi
        lights = spiceapi.lights_read(connection)
        apiR = math.floor(lights[config.SPICEAPI_LIGHT_R][1] * 255.0)
        apiG = math.floor(lights[config.SPICEAPI_LIGHT_G][1] * 255.0)
        apiB = math.floor(lights[config.SPICEAPI_LIGHT_B][1] * 255.0)

        fader.set_fade(lastR, lastG, lastB, apiR, apiB, apiG)


api_thread = threading.Thread(target=api_update)
api_thread.start()
print("api OK")

while True:
    if fader.ended:
        fader.set_fade(lastR, lastG, lastB, apiR, apiG, apiB)

    next = fader.get_next()

    lastR = next[0]
    lastG = next[1]
    lastB = next[2]

    if not next[0] == -1 and not next[1] == -1 and not next[2] == -1:
        pixels.fill((next[0], next[1], next[2]))