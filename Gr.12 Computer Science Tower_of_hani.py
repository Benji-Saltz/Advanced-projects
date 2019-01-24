#By: Benji Saltz
#Benji Saltz 15/03/18
#Description: Tower of Hanoi- This program allows a user to find the most efficient way to  solve a tower of hanoi puzzle
#What is Tower of Hanoi? Towar of Hanoi is a puzzle game in which a user has to move all disks from one pillar to the farthest pillar. The trick is larger disks cannot stack ontop of a smaller disks while sorting.
class Stack: #Stack class
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def validMove(self,other): #checks to see if a disk could stack, and then stacks the didsk. Essentially checks if disk could perform a valid move
        if self.items != [] and (other.items == [] or self.peek() < other.peek()): #Checks if the top item of one stack is less than another stack (applies to elif statement too)
            other.push(self.pop())#Moves disk (not visually)
        elif other.items != [] and (self.items == [] or other.peek() < self.peek()):
            self.push(other.pop())
            
    def PrintTower(self,other,another): #Shows the visual tower movement
        print ("Move", moves,"\n",source.items,"\n",temp.items,'\n',dest.items,'\n')#Displays move counter, 1st pillar, 2nd pillar, and 3rd pillar

source = Stack() #1st row
temp = Stack() #2nd row
dest = Stack() #3rd row
moves = 0
num = int(input("Enter the number of disks you want: "))#allows user to input how many disks they want to sort 
for a in range(num,0,-1):
    source.push(a)
    
source.PrintTower(temp,dest)#This sequence is movement from start to finish and drawing 
if num%2 == 1:#From this point, this sequence will check with valid move where the disks could go, and will move them around if they fit the parameters.
    while True: #While true, if the disk stack is from smallest to largest essentially. If the move is valid, it moves the disk, adds a move to the counter, and visually shows the movement
        source.validMove(dest)
        moves +=1        
        source.PrintTower(temp,dest)
        if dest.size() == num: #If the destination stack is full with all disks, the program ends
            break
        source.validMove(temp)
        moves +=1        
        source.PrintTower(temp,dest)
        dest.validMove(temp)
        moves +=1        
        source.PrintTower(temp,dest)

else:
    while True:        
        source.validMove(temp)
        moves +=1        
        source.PrintTower(temp,dest)
        source.validMove(dest)
        moves +=1        
        source.PrintTower(temp,dest)
        temp.validMove(dest)
        moves +=1        
        source.PrintTower(temp,dest)
        if dest.size() == num:
            break
