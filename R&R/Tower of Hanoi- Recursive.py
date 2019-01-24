#By: Benji Saltz
#Date: 30/03/18
#Description: Tower of Hanoi Recursive- This program allows a user to find the most efficient way to  solve a tower of hanoi puzzle
#What is Tower of Hanoi? Towar of Hanoi is a puzzle game in which a user has to move all disks from one pillar to the farthest pillar. The trick is larger disks cannot stack ontop of a smaller disks while sorting.
class Stack: #Stack class
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
############################################
Left = Stack()
Middle = Stack()         #Values are given (Left, Center, Right)
Right = Stack()
num = int(input("enter the number of disks you want: "))
for a in range(num,0,-1): #stack is filled 
    Left.push(a)
#############################################
def printTower():
    printTower.counter += 1 #Adds one to built in counter
    print ("Move", printTower.counter,"\n",Left.items,"\n",Middle.items,'\n',Right.items,'\n')
    
def t(num,beg,end,aux):
    if num==1:
        end.push(beg.pop()) #The function takes the top value from A and moves it to C
        printTower()
    else:
        t(num-1,beg,aux,end)  #The function takes the next value and moves it from stack A moves it to B
        end.push(beg.pop()) #The function takes the top value from A and moves it to C
        printTower()
        t(num-1,aux,end,beg)  #The function takes the next value and moves it from stack B moves it to C
        
printTower.counter = 0
t(num,Left,Right,Middle)              #functions are called
