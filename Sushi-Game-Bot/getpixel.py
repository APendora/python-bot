from PIL import ImageGrab
import os
import time

"""
 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 156
y_pad = 345
Play area =  x_pad+1, y_pad+1, 796, 825
"""

#Globals
#----------

x_pad = 20
y_pad = 260

def screenGrab():
    im = ImageGrab.grab(bbox = (x_pad+1,y_pad+1,x_pad+650,y_pad+482))
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((1, 1))

    print(r, g, b)

def main():
    screenGrab()

if __name__ == '__main__':
    main()
