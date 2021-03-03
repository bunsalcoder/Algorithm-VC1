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
scoreLabel = Label(top, text = "Score: " + str(score), bg = "black", fg = "blue", font = ("Sans",  20))
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

def createMonster():
    X = random.randrange(80, 1120)
    Y = -80
    monsters = playground.create_image(X, Y, image = monsterImage)
    monsterList.append(monsters)
    playground.after(1000, createMonster)

def moveMonster():
    for monster in range(len(monsterList)):
        playground.coords(monsterList[monster])[1]
        monsters = monsterList[monster]
        playground.move(monsters, 0, 50)
    playground.after(320, lambda: moveMonster())


#___Bullet Movement_______________________________________________________________________________

bulletList = []

def shootMonster():
    global bulletList
    playground.move(midBullet, 0, -20)

    myY = playground.coords(midBullet)[1]
    beyondShooting = myY <= 0

    if not beyondShooting:
        playground.after(10, lambda:shootMonster())
    else:
        playground.delete(midBullet)
        toShoot()


def toShoot():
    global myShip, midBullet 
    X1 = playground.coords(myShip)[0]
    Y1 = playground.coords(myShip)[1]
    midBullet = playground.create_image(X1, Y1 - 20, image = bulletImage)

    shootMonster()


#___ImpactMonsterBullet____________________________________________________________________________

deleteMonsterBullet = []

def monsterBullet():           # Function use to check the collision of bullet and the monster
    global deleteMonsterBullet 

    bulletPosition = playground.coords(midBullet)
    for monster in range (len(monsterList)):
        theMonster = monsterList[monster]
        monsterPosition = playground.coords(theMonster)
        if (bulletPosition[1] <= monsterPosition[1] + 60) and (((bulletPosition[0] >= monsterPosition[0]) and (bulletPosition[0] <= monsterPosition[0] + 60)) or ((bulletPosition[0] + 50 >= monsterPosition[0]) and (bulletPosition[0]+50 <= monsterPosition[0] + 60))):
            deleteMonsterBullet.append(midBullet) 
            deleteMonsterBullet.append(monsterList[monster])
    return deleteMonsterBullet


def eraseBulletMonster():      # Function to remove bullet and the monster from the list
    global deleteMonsterBullet  
    monsterBulletToDelete = monsterBullet()
    if len(monsterBulletToDelete) > 0:
        deleteMonsterBullet.remove(monsterBulletToDelete[1])
        playground.delete(monsterBulletToDelete[0])
        playground.delete(monsterBulletToDelete[1])
        
    playground.after(10, eraseBulletMonster)


#___Ship Movement________________________________________________________________________________

def shipMove(event):
    if  playground.coords(myShip)[0] <= 1125 and event.char == "d":
        playground.move(myShip, 30, 0)
    elif playground.coords(myShip)[0] >= 75 and event.char == "a":
        playground.move(myShip, -30, 0)
    elif playground.coords(myShip)[1] > 100 and event.char == "w":
        playground.move(myShip, 0, -30)
    elif playground.coords(myShip)[1] < 870 and event.char == "s":
        playground.move(myShip, 0, 30)
    

#___Function Call_______________________________________________________________________________

createMonster()         # This is to create monster
moveMonster()           # This is to move the monster
toShoot()               # This is to shoot the monster
eraseBulletMonster()    # This is to delete bullet and monster from the list


#___Key event___________________________________________________________________________________

root.bind("<Key>", shipMove)


#___At the very bottom__________________________________________________________________________

root.mainloop()