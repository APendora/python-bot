from PIL import ImageGrab
import win32api, win32con
from PIL import Image, ImageOps
from numpy import *
import os
import time

"""
 
All coordinates assume a screen resolution of 1980x1080, and Chrome 
half screened with the Bookmarks Toolbar enabled.

x_pad = 20
y_pad = 260
Play area =  x_pad+1, y_pad+1, 650, 482
"""

#Globals
#----------

x_pad = 20
y_pad = 260

def screenGrab():
    im = ImageGrab.grab(bbox = (x_pad+1,y_pad+1,x_pad+650,y_pad+482))
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def grab():
    box = (x_pad + 1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    return a

def main():
    screenGrab()

if __name__ == '__main__':
    main()

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ('Click.')

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('Left Down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('Left Release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0],y_pad + cord[1]))
                          
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)

def startGame():
    #location of first menu
    mousePos((308, 206))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((314, 395))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((252, 456))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((318, 375))
    leftClick()
    time.sleep(.1)

class Cord:
    f_shrimp = (35,333)
    f_rice = (92, 338)
    f_nori = (33, 394)
    f_roe = (92, 392)
    f_salmon = (38, 448)
    f_unagi = (91, 446)

#---------------------------------------
    phone = (586,381)

    menu_toppings = (567, 638)
     
    t_shrimp = (492, 226)
    t_nori = (494, 276)
    t_roe = (575, 280)
    t_salmon = (489, 338)
    t_unagi = (574, 226)
    t_exit = (596, 339)
 
    menu_rice = (550, 330)
    buy_rice = (542, 286)
     
    delivery_norm = (558, 338) # will need to fix

def clear_tables():
    mousePos((76, 211))
    leftClick()

    mousePos((178, 211))
    leftClick()
 
    mousePos((286, 211))
    leftClick()
 
    mousePos((395, 213))
    leftClick()
 
    mousePos((489, 209))
    leftClick()
 
    mousePos((587, 208))
    leftClick()
    time.sleep(1)

"""
Receipes:
    Onigiri: 2 rice, 1 nori

    California roll: 1 rice, 1 nori, 1 roe

    Gunkan: 1 rice, 1 nori, 2 roe

"""
def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
    leftClick()
    time.sleep(.1)

def makeFood(food):
    if food == 'caliroll':
        print ('Making a caliroll')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print ('Making a onigiri')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.05)
         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print ('Making a gunkan')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (204, 172, 89):
            print ('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('rice is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
             
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print ('test')
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (62, 61, 60):
            print ('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('nori is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (238, 219, 169):
            print ('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('roe is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
            
    if food == 'salmon':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_salmon) != (238, 130, 200):
            print ('salmon is available')
            mousePos(Cord.t_salmon)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['salmon'] += 5
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('salmon is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

    if food == 'shrimp':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_shrimp) != (238, 219, 169):
            print ('shrimp is available')
            mousePos(Cord.t_shrimp)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['shrimp'] += 5
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('shrimp is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
    if food == 'unagi':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_unagi) != (238, 219, 169):
            print ('unagi is available')
            mousePos(Cord.t_unagi)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['unagi'] += 5
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print ('unagi is NOT available')
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe' or i == 'salmon' or i == 'shrimp' or i == 'unagi':
            if j <= 4:
                print ('%s is low and needs to be replenished' % i)
                buyFood(i)

def get_seat_one():
    box = (30,20,25+63,62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_two():
    box = (125,62,125+63,62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_three():
    box = (0,62,225,62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_four():
    box = (325,62,325+63,62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_five():
    box = (425,62,425+63,62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_seat_six():
    box = (531,63,531+63,62+16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()
