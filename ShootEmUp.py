#___import______________________________________________________________________________________

from tkinter import *
import random


#___Root_Set_Up_________________________________________________________________________________

root = Tk()
root.geometry("1200x1000")
root.title("Shoot 'Em Up")

#___Top_________________________________________________________________________________________

top = Canvas(root, width = 1200, height = 50, bg = "black")
top.grid(column = 0, row = 0)


#___Playground__________________________________________________________________________________

playground = Canvas(root, width = 1200, height = 1000, bg = "white")
playground.grid(column = 0, row = 1)


#___Score & Live________________________________________________________________________________

# Score!!

score = 0
scoreLabel = Label(top, text = "Score: " + str(score), bg = "black", fg = "blue", font = ("Sans",  25))
scoreLabel.place(x = 50, y = 5)


# Lives!!

spaceLiveImage = PhotoImage(file = "heart.png")
myLives1 = Label(top, image = spaceLiveImage, bg = "black")
myLives1.place(x = 1050, y = 5)
myLives2 = Label(top, image = spaceLiveImage, bg = "black")
myLives2.place(x = 1100, y = 5)
myLives3 = Label(top, image = spaceLiveImage, bg = "black")
myLives3.place(x = 1150, y = 5)


#___Images______________________________________________________________________________________

# Background

backgroundImage = PhotoImage(file = "background.png")
myBackground = playground.create_image(598, 500, image = backgroundImage)

# Spaceship image!!

spaceShipImage = PhotoImage(file = "spaceInvader.png")
myShip = playground.create_image(600, 750, image = spaceShipImage)

# Monster image!!

monsterImage = PhotoImage(file = "monster.png")

# Bullet image!!

bulletImage = PhotoImage(file = "bullet.png")


#___Monster Movement_____________________________________________________________________________

monsterList = []
numberOfLife = 0

def createMonster():
    X = random.randrange(80, 1120)
    Y = -80
    monsters = playground.create_image(X, Y, image = monsterImage)
    monsterList.append(monsters)
    playground.after(1000, createMonster)

def moveMonster():
    for monster in range(len(monsterList)):
        axeY = playground.coords(monsterList[monster])[1]
        monsters = monsterList[monster]
        playground.move(monsters, 0, 50)
        if playground.coords(monsters)[1] + 40 == playground.coords(myShip)[1] - 75:
            numberOfLife += 1
            lifeLess()
            
    playground.after(320, lambda: moveMonster())


def lifeLess():
    if numberOfLife == 1:
        playground.delete(myLives1)
    elif numberOfLife == 2:
        playground.delete(myLives2)
    elif numberOfLife == 3:
        playground.delete(myLives3)


#___Bullet Movement_______________________________________________________________________________

bulletList = []

def shootMonster():
    global bulletList
    myLeftBullet = playground.move(leftBullet, 0, -20)
    myMidBullet = playground.move(midBullet, 0, -20)
    myRightBullet = playground.move(rightBullet, 0, -20)

    myY = playground.coords(leftBullet)[1]
    beyondShooting = myY <= 0
    monsterBulletToDelete = monsterBullet()
    if len(monsterBulletToDelete) == 0:    
        if not beyondShooting:
            playground.after(10, lambda:shootMonster())
        else:
            playground.delete(leftBullet)
            playground.delete(midBullet)
            playground.delete(rightBullet)
            toShoot()


 

def toShoot():
    global myShip, leftBullet, rightBullet, midBullet, bulletList
    X1 = playground.coords(myShip)[0]
    Y1 = playground.coords(myShip)[1]
    leftBullet = playground.create_image(X1 - 40, Y1 + 35, image = bulletImage)
    midBullet = playground.create_image(X1, Y1 - 20, image = bulletImage)
    rightBullet = playground.create_image(X1 + 40, Y1 + 35, image = bulletImage)
    bulletList = [leftBullet, midBullet, rightBullet]
    shootMonster()


#___ImpactMonsterBullet____________________________________________________________________________

def monsterBullet():           # Function use to check the collision of bullet and the monster
    deleteMonsterBullet = []
    for bullet in bulletList:
        bulletPosition = playground.coords(bullet)
        for theMonster in monsterList:
            monsterPosition = playground.coords(theMonster)
            if (bulletPosition[1] <= monsterPosition[1] + 80) and (((bulletPosition[0] >= monsterPosition[0]) and (bulletPosition[0] <= monsterPosition[0] + 80)) or ((bulletPosition[0] + 50 >= monsterPosition[0]) and (bulletPosition[0]+50 <= monsterPosition[0] + 80))):
                deleteMonsterBullet.append(bullet) 
                deleteMonsterBullet.append(theMonster)
    return deleteMonsterBullet


def eraseBulletMonster():      # Function to remove bullet and the monster from the list
    monsterBulletToDelete = monsterBullet()
    if len(monsterBulletToDelete) > 0:
        bulletList.remove(monsterBulletToDelete[0])
        monsterList.remove(monsterBulletToDelete[1])
        playground.delete(monsterBulletToDelete[0])
        playground.delete(monsterBulletToDelete[1])
        
    playground.after(10, eraseBulletMonster)


#___Ship Movement_________________________________________________________________________________

def shipMove(event):
    if  playground.coords(myShip)[0] <= 1125 and event.char == "d":
        playground.move(myShip, 30, 0)
    elif playground.coords(myShip)[0] >= 75 and event.char == "a":
        playground.move(myShip, -30, 0)
    elif playground.coords(myShip)[1] > 100 and event.char == "w":
        playground.move(myShip, 0, -30)
    elif playground.coords(myShip)[1] < 830 and event.char == "s":
        playground.move(myShip, 0, 30)
    

#___Function Call_______________________________________________________________________________

createMonster()         # This is to create monster
moveMonster()           # This is to move the monster
toShoot()               # This is to shoot the monster
eraseBulletMonster()    # This is to delete bullet and monster from the list
lifeLess()              # This is to decrease the life


#___Key event___________________________________________________________________________________

root.bind("<Key>", shipMove)


#___At the very bottom__________________________________________________________________________

root.mainloop()
