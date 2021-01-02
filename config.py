# Specify these with launch args in spice.
SPICEAPI_HOST = "localhost"
SPICEAPI_PORT = 4444
SPICEAPI_PASS = "changeme"

# Light IDs for the lights you want to reflect. Check the spice monitor in-game or with the mobile app.
SPICEAPI_LIGHT_R = 0
SPICEAPI_LIGHT_G = 1
SPICEAPI_LIGHT_B = 2

# Specify how many lights your strip has.
NUM_LIGHTS = 150
# Specify the period used for fading - this value seems to work fine for me
FADE_PERIOD_MS = 20