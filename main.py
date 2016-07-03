
import unicornhat as UH
import time
import characterLibrary

for coords in characterLibrary.A:
    x, y = coords
    UH.set_pixel(x,y,255,0,0)
UH.show()

time.sleep(5)











