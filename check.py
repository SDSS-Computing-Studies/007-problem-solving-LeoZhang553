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

x1,y1=earth
x1=int(x1)
y1=int(y1)

print(p.pixel(x1,y1))

x2,y2=city
x2=int(x2)
y2=int(y2)

print(p.pixel(x2,y2))

x3,y3=factory
x3=int(x3)
y3=int(y3)

print(p.pixel(x3,y3))

x4,y4=farm
x4=int(x4)
y4=int(y4)

print(p.pixel(x4,y4))

x5,y5=cow
x5=int(x5)
y5=int(y5)

print(p.pixel(x5,y5))

x6,y6=toilet
x6=int(x6)
y6=int(y6)

print(p.pixel(x6,y6))

x7,y7=baby
x7=int(x7)
y7=int(y7)

print(p.pixel(x7,y7))

x8,y8=hand
x8=int(x8)
y8=int(y8)

print(p.pixel(x8,y8))
