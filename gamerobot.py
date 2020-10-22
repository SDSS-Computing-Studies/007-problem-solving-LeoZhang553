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

a=0 

x1,y1=earth
x1=int(x1)
y1=int(y1)
px1=p.pixel(x1,y1)

x2,y2=city
x2=int(x2)
y2=int(y2)
px2=p.pixel(x2,y2)

x3,y3=factory
x3=int(x3)
y3=int(y3)
px3=p.pixel(x3,y3)

x4,y4=farm
x4=int(x4)
y4=int(y4)
px4=p.pixel(x4,y4)

x5,y5=cow
x5=int(x5)
y5=int(y5)
px5=p.pixel(x5,y5)

x6,y6=toilet
x6=int(x6)
y6=int(y6)
px6=p.pixel(x6,y6)

x7,y7=baby
x7=int(x7)
y7=int(y7)
px7=p.pixel(x7,y7)

x8,y8=hand
x8=int(x8)
y8=int(y8)
px8=p.pixel(x8,y8)

x9,y9=poop
x9 = int(x9)
y9 = int(y9)
px9=p.pixel(x9,y9)


while True:
    if p.pixel(x9,y9) == px9:
        p.moveTo(poop)
        p.click()
        a+=1
    if p.pixel(x1,y1) != px1:
        p.moveTo(earth)
        p.click()
        t.sleep(0.1)

    if p.pixel(x2,y2) != px2:
        p.moveTo(city)
        p.click()
        t.sleep(0.1)

    if p.pixel(x3,y3) != px3:
        p.moveTo(factory)
        p.click()
        t.sleep(0.1)

    if p.pixel(x4,y4) != px4:
        p.moveTo(farm)
        p.click()
        t.sleep(0.1)

    if p.pixel(x5,y5) != px5:
        p.moveTo(cow)
        p.click()
        t.sleep(0.1)

    if p.pixel(x6,y6) != px6:
        p.moveTo(toilet)
        p.click()
        t.sleep(0.1)

    if p.pixel(x7,y7) != px7:
        p.moveTo(baby)
        p.click()
        t.sleep(0.1)

    if p.pixel(x8,y8) != px8:
        p.moveTo(hand)
        p.click()
        t.sleep(0.1)
    
    if a%100 == 0:
        p.click(tools)
        Close = p.locateCenterOnScreen('butClose.png')

        upHand = p.locateCenterOnScreen('but_UpHand.png')
        upBaby = p.locateCenterOnScreen('but_UpBaby.png')
        upTolt = p.locateCenterOnScreen('but_UpTolt.png')
        upCow = p.locateCenterOnScreen('but_UpCow.png')
        upFarm = p.locateCenterOnScreen('but_UpFarm.png')
        upFac = p.locateCenterOnScreen('but_UpFac.png')
        upCity = p.locateCenterOnScreen('but_UpCity.png')
        upEarth = p.locateCenterOnScreen('but_UpEarth.png')

        xa,ya=upHand
        xa = int(xa)
        ya = int(ya)
        pxa=p.pixel(xa,ya)

        xb,yb=upBaby
        xb = int(xb)
        yb = int(yb)
        pxb=p.pixel(xb,yb)

        xc,yc=upTolt
        xc = int(xc)
        yc = int(yc)
        pxc=p.pixel(xc,yc)

        xd,yd=upCow
        xd = int(xd)
        yd = int(yd)
        pxd=p.pixel(xd,yd)

        xe,ye=upFarm
        xe = int(xe)
        ye = int(ye)
        pxe=p.pixel(xe,ye)

        xf,yf=upFac
        xf = int(xf)
        yf = int(yf)
        pxf=p.pixel(xf,yf)

        xg,yg=upCity
        xg = int(xg)
        yg = int(yg)
        pxg=p.pixel(xg,yg)

        xh,yh=upEarth
        xh = int(xh)
        yh = int(yh)
        pxh=p.pixel(xh,yh)

        if p.pixel(xa,ya) != pxa:
            p.click(upHand)
        elif p.pixel(xb,yb) != pxb:
            p.click(upBaby)
        elif p.pixel(xc,yc) != pxc:
            p.click(upTolt)
        elif p.pixel(xd,yd) != pxd:
            p.click(upCow)
        elif p.pixel(xe,ye) != pxe:
            p.click(upFarm)
        elif p.pixel(xf,yf) != pxf:
            p.click(upFac)
        elif p.pixel(xg,yg) != pxg:
            p.click(upCity)
        elif p.pixel(xh,yh) != pxh:
            p.click(upEarth)
        p.click(Close)




    
