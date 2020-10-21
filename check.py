import pyautogui as p 
import time as t

hand = p.locateCenterOnScreen('butHand.png', region=(1000,180,900,480))
baby = p.locateCenterOnScreen('butBaby.png', region=(1000,180,900,480))
toilet = p.locateCenterOnScreen('butToilet.png', region=(1000,180,900,480))
cow = p.locateCenterOnScreen('butCow.png', region=(1000,180,900,480))
farm = p.locateCenterOnScreen('butFarm.png', region=(1000,180,900,480))
factory = p.locateCenterOnScreen('butFactory.png', region=(1000,180,900,480))
city = p.locateCenterOnScreen('butCity.png', region=(1000,180,900,480))
earth = p.locateCenterOnScreen('butEarth.png', region=(1000,180,900,480))

x,y = p.locateCenterOnScreen('butPoop.png', confidence=0.8)
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


hand = p.locateCenterOnScreen('butHand.png')
baby = p.locateCenterOnScreen('butBaby.png')
toilet = p.locateCenterOnScreen('butToilet.png')
cow = p.locateCenterOnScreen('butCow.png')
farm = p.locateCenterOnScreen('butFarm.png')
factory = p.locateCenterOnScreen('butFactory.png')
city = p.locateCenterOnScreen('butCity.png')
earth = p.locateCenterOnScreen('butEarth.png')

x1,y1=hand
x1=int(x1)
y1=int(y1)

print(p.pixel(x1,y1))

x2,y2=baby
x2=int(x2)
y2=int(y2)

print(p.pixel(x2,y2))