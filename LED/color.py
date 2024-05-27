import board
import neopixel
import time
pixels=neopixel.NeoPixel(board.D18,12)
DELAY = 1

 

print("All neopixels OFF")
pixels.fill((0,0,0))
pixels.show()
time.sleep(DELAY)

 

while True :
	print(" Mode1 ")
	pixels.fill((255,0,0))
	#pixels[4] = (255,0,0)
	pixels.show()
	time.sleep(DELAY)
