import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 10
PIXEL_ORDER = neopixel.GRB
DELAY = 1

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, brightness=0.1, auto_write=False, pixel_order=PIXEL_ORDER, bit0=0b1000000
)

print("All neopixels OFF")
pixels.fill((0,0,0))
pixels.show()
time.sleep(DELAY)

print("One neopixel red")
pixels[0] = (255,0,0)
pixels.show()
time.sleep(DELAY)

print("All neopixels green")
pixels.fill((0,255,0))
pixels.show()
time.sleep(DELAY)

print("All neopixels OFF")
pixels.fill((0,0,0))
pixels.show()
time.sleep(DELAY)

print("End of test")
