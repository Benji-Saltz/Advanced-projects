###################
## Tomer Zibman
## OOP Ball Class
###################

import random

class Ball(object):
    def __init__(self,ball_x=0,ball_y=0,change_x=1,change_y=1):
        self.ball_x=ball_x
        self.ball_y=ball_y
        self.change_x=change_x
        self.change_y=change_y
        self.size=random.randint(1,50)
        self.color=(random.randint(0,256),random.randint(0,256),random.randint(0,256))

    def move(self):
        self.ball_x+=self.change_x
        self.ball_y+=self.change_y

    def bounce(self):
        self.ball_y-=self.change_y
        self.ball_y+=self.change_y

    def __str__(self):
        return "The ball's new x position is x="+str(self.ball_x)+" and the ball's new y positon is y="+str(self.ball_y)

class Basketball(Ball):
    def __init__(self,jump=15):
        Ball.__init__(self)
        self.jump=jump
        self.size=30
        self.color=(165,42,42) #brown

    def move(self):
        self.ball_y+=self.jump
        self.ball_x+=self.change_x

class Golf(Ball):
    def __init__(self,roll=20,fly=100):
        Ball.__init__(self)
        self.size=5
        self.roll=roll
        self.fly=fly
        self.color=(255,255,255) #white

    def move(self):
        self.ball_x+=self.roll
        self.ball_y+=self.fly
        
ball_list=[]
print("The ball's start at x = 0 and y = 0")
print()

for i in range(4):
    randX = random.randint(-100,100)
    randY = random.randint(-100,100)
    ball_list.append(Ball(change_x = randX, change_y = randY))
    ball_list[i].move()
    ball_list[i].bounce()
    print(ball_list[i])
print()
gameBalls=[]
for i in range(2):
    gameBalls.append(Basketball(60))
    gameBalls[2*i].move()
    gameBalls[2*i].bounce()
    print(gameBalls[2*i])
    gameBalls.append(Golf(30,90))
    gameBalls[2*i+1].move()
    gameBalls[2*i+1].bounce()
    print(gameBalls[2*i+1])

        
