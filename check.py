import pyautogui as p 
import time as t

hand = p.locateCenterOnScreen('butHand.png')
baby = p.locateCenterOnScreen('butBaby.png')
toilet = p.locateCenterOnScreen('butToilet.png')
cow = p.locateCenterOnScreen('butCow.png')
farm = p.locateCenterOnScreen('butFarm.png')
factory = p.locateCenterOnScreen('butFactory.png')
city = p.locateCenterOnScreen('butCity.png')
earth = p.locateCenterOnScreen('butEarth.png')
poop = p.locateCenterOnScreen('butPoop.png')


#p.click(hand)
#t.sleep(0.4)
#p.click(baby)
#t.sleep(0.4)
#p.click(toilet)
#t.sleep(0.4)
#p.click(cow)
#t.sleep(0.4)
#p.click(farm)
#t.sleep(0.4)
#p.click(factory)
#t.sleep(0.4)
#p.click(city)
#t.sleep(0.4)
#p.click(earth)
#t.sleep(0.4)

if p.pixel(poop) == (186,151,101):
    print(poop)