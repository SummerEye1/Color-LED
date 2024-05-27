import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 24
PIXEL_ORDER = neopixel.GRB
DELAY = 1

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, brightness=0.1, auto_write=False, pixel_order=PIXEL_ORDER
)

print("All neopixels OFF")
pixels.fill((0,0,0))
pixels.show()
time.sleep(DELAY)

print("1 floor neopixel red")
pixels[0] = (255,0,0)
pixels[1] = (255,0,0)
pixels[2] = (255,0,0)
pixels[3] = (255,0,0)
pixels[4] = (255,0,0)
pixels[5] = (255,0,0)
pixels[6] = (255,0,0)
pixels[7] = (255,0,0)
pixels[8] = (255,0,0)
pixels[9] = (255,0,0)
pixels[10] = (255,0,0)
pixels[11] = (255,0,0)

pixels[12] = (255,69,0)
pixels[13] = (255,215,0)
pixels[14] = (255,255,0)

pixels[15] = (154,205,50)
pixels[16] = (124,252,0)
pixels[17] = (0,128,0)

pixels[18] = (32,178,170)
pixels[19] = (0,206,209)
pixels[20] = (0,255,255)

pixels[21] = (30,144,255)
pixels[22] = (0,0,255)
pixels[23] = (148,0,211)
pixels.show()
time.sleep(DELAY)



print("All neopixels OFF")
pixels.fill((0,0,0))
pixels.show()
time.sleep(DELAY)

print("End of test")
