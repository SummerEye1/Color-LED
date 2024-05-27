import time
import board
import neopixel_spi as neopixel

NUM_PIXELS = 24
PIXEL_ORDER = neopixel.GRB
DELAY = 10

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, brightness=0.1, auto_write=False, pixel_order=PIXEL_ORDER, bit0=0b1000000
)

r = int(input('赤要素を指定してください(0~255):'))
g = int(input('緑要素を指定してください(0~255):'))
b = int(input('青要素を指定してください(0~255):'))


print("色を表示します")
pixels.fill((r,g,b))
pixels.show()
time.sleep(DELAY)



print("End")
