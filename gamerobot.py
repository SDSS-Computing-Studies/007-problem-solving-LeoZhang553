import pyautogui as p 
import time as t


# game: https://www.crazygames.com/game/poop-clicker-2

# this is the work for submission

# all locations will be grey buttons
# locate those locations at the begining of the program
# in while loop, check the color of the center of the picture(button)
# use if...else to decide if click it

poop = p.locateCenterOnScreen('butPoop.png')
tools = p.locateCenterOnScreen('butTools.png')
hand = p.locateCenterOnScreen('butHand.png')
baby = p.locateCenterOnScreen('butBaby.png')
toilet = p.locateCenterOnScreen('butToilet.png')
cow = p.locateCenterOnScreen('butCow.png')
farm = p.locateCenterOnScreen('butFarm.png')
factory = p.locateCenterOnScreen('butFactory.png')
city = p.locateCenterOnScreen('butCity.png')
earth = p.locateCenterOnScreen('butEarth.png')
while True:

    p.moveTo(poop)
    p.click()
    t.sleep(0.1)

    x1,y1=hand
    x1=int(x1)
    y1=int(y1)

    print(p.pixel(x1,y1))

    if p.pixel(x1,y1) == (184, 209, 104):
        p.moveTo(hand)
        p.click()
        t.sleep(0.2)


    
