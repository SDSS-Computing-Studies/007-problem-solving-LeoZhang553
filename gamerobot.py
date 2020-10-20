import pyautogui as p 
import time as t

p.mouseInfo()

# game: https://www.crazygames.com/game/poop-clicker-2

# this is the work for submission
hand = p.locateCenterOnScreen('butHand.png')
baby = p.locateCenterOnScreen('butBaby.png')
toilet = p.locateCenterOnScreen('butToilet.png')
cow = p.locateCenterOnScreen('butCow.png')
farm = p.locateCenterOnScreen('butFarm.png')
factory = p.locateCenterOnScreen('butFactory.png')
city = p.locateCenterOnScreen('butCity.png')
earth = p.locateCenterOnScreen('butEarth.png')
poop = p.locateCenterOnScreen('butPoop.png')
tools = p.locateCenterOnScreen('butTools.png')

while True:
    if p.pixel(poop) == (186,151,101):
        p.click(poop)  

        if p.pixel(1637,546) == ( 140,314,57 ):
            p.moveTo()
            p.moveTo(1637,546)
            p.click()
            t.sleep(0.3)

        if p.pixel(1671,430) == (155,221,75):
            p.moveTo(1671,430)
            p.click()
            t.sleep(0.3)

        if p.pixel(1632,336) == (147,217,64):
            p.moveTo(1632,336)
            p.click()
            t.sleep(0.3)

        if p.pixel(1645,233) == (147,217,65):
            p.moveTo(1645,233)
            p.click()
            t.sleep(0.3)

        if p.pixel(1191,550) == ( 135,211 ,53 ):
            p.moveTo(1191,550)
            p.click()
            t.sleep(0.3)

        if p.pixel( 1176,439) == ( 146,217,63):
            p.moveTo(1176,439)
            p.click()   
            t.sleep(0.3) 

        if p.pixel(1183,337) == ( 146,217 ,63 ):
            p.moveTo(1183,337)
            p.click()
            t.sleep(0.2)

        if p.pixel( 1169,233 ) == ( 147,217 ,64 ):
            p.moveTo(1169,233)
            p.click()
            t.sleep(0.1)
        
    else:
        break