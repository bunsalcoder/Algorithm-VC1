#___import______________________________________________________________________________________

from tkinter import *
import time
import random


#___Root_Set_Up_________________________________________________________________________________

root = Tk()
root.geometry("1200x1000")
root.title("Shoot 'Em Up")

#___Top_________________________________________________________________________________________

top = Canvas(root, width = 1200, height = 50, bg = "black")
top.grid(column = 0, row = 0)

playground = Canvas(root, width = 1200, height = 1000, bg = "white")
playground.grid(column = 0, row = 1)


#___Score & Live________________________________________________________________________________

# Score!!

score = 0
scoreLabel = Label(top, text = "Score: " + str(score), bg = "green", fg = "white", font = (50))
scoreLabel.place(x = 50, y = 15)


# Lives!!

lives = 3
livesLabel = Label(top, text = "Lives Left: " + str(lives), bg = "red", fg = "white", font = (50))
livesLabel.place(x = 1040, y = 15)


#___Images______________________________________________________________________________________

# Background

backgroundImage = PhotoImage(file = "background.png")
myBackground = playground.create_image(598, 500, image = backgroundImage)


# Spaceship image!!

spaceShipImage = PhotoImage(file = "spaceInvader.png")
myShip = playground.create_image(600, 750, image = spaceShipImage)

# Monster image!!

monsterImage = PhotoImage(file = "monster.png")
theMonster1 = playground.create_image(50, 50, image = monsterImage)
theMonster2 = playground.create_image(600, 50, image = monsterImage)
theMonster3 = playground.create_image(1150, 50, image = monsterImage)

# Bullet image!!

bulletImage = PhotoImage(file = "bullet.png")


#___Monster Movement_____________________________________________________________________________

    

#___Bullet Function_______________________________________________________________________________

def shootEnemy():
    global leftBullet, rightBullet
    myLeftBullet = playground.move(leftBullet, 0, -15)
    myRightBullet = playground.move(rightBullet, 0, -15)

    myY = playground.coords(leftBullet)[1]
    beyondShooting = myY <= 0
    
    if not beyondShooting:
        playground.after(10, lambda: shootEnemy())
    else:
        playground.delete(leftBullet)
        playground.delete(rightBullet)
        toShoot()


def toShoot():
    global myShip, leftBullet, rightBullet
    X1 = playground.coords(myShip)[0]
    Y1 = playground.coords(myShip)[1]
    leftBullet = playground.create_image(X1 - 40, Y1 + 35, image = bulletImage)
    rightBullet = playground.create_image(X1 + 40, Y1 + 35, image = bulletImage)
    shootEnemy()



#___Ship Movement_________________________________________________________________________________

# Move left!!

def moveLeft(event):
    if playground.coords(myShip)[0] > 60:
        playground.move(myShip, -20, 0)


# Move right!!

def moveRight(event):
    if playground.coords(myShip)[0] < 1140:
        playground.move(myShip, 20, 0)


# Move up!!

def moveUp(event):
    playground.move(myShip, 0, -20)


# Move down!!

def moveDown(event):
    if playground.coords(myShip)[1] < 880:
        playground.move(myShip, 0, 20)



#___Function Call_______________________________________________________________________________

toShoot()


#___Key event___________________________________________________________________________________

playground.bind_all("<a>", moveLeft)
playground.bind_all("<d>", moveRight)
playground.bind_all("<w>", moveUp)
playground.bind_all("<s>", moveDown)


#___At the very bottom__________________________________________________________________________

root.mainloop()
