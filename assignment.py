import pyautogui as p 
import time as t

p.mouseInfo()

# game: https://www.crazygames.com/game/poop-clicker-2

while True:
    p.moveTo(1421,410 )
    p.click()

    if p.getpixel( 1169,233 ) == ( 147,217 ,64 ):
        p.moveTo(1169,233)
        p.click()
        t.sleep(1)

    if p.getpixel(1183,337) == ( 146,217 ,63 ):
        p.moveTo(1183,337)
        p.click()
        t.sleep(1)

    if p.getpixel( 1176,439) == ( 146,217,63):
        p.moveTo(1176,439)
        p.click()   
        t.sleep(1) 

    if p.getpixel(1191,550) == ( 135,211 ,53 ):
        p.moveTo(1191,550)
        p.click()
        t.sleep(1)

    if p.getpixel(1645,233) == (147,217,65):
        p.moveTo(1645,233)
        p.click()
        t.sleep(1)

    if p.getpixel(1632,336) == (147,217,64):
        p.moveTo(1632,336)
        p.click()
        t.sleep(1)

    if p.getpixel(1671,430) == (155,221,75):
        p.moveTo(1671,430)
        p.click()
        t.sleep(1)

    if p.getpixel(1637,546) == ( 140,314,57 ):
        p.moveTo(1637,546)
        p.click()
        t.sleep(1)




