import board
import neopixel_spi as neopixel
import time
NUM_PIXELS = 10
PIXEL_ORDER = neopixel.GRB
DELAY = 1

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, brightness=0.1, auto_write=False, pixel_order=PIXEL_ORDER, bit0=0b1000000
)

pixels.fill((0,255,0))
pixels.show()
time.sleep(DELAY)

pixels.fill((0,0,0))
pixels.show()
time.sleep(DELAY)

pixels.fill((255,0,0))
pixels.show()
time.sleep(DELAY)
