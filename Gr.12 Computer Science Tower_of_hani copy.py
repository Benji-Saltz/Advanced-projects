#Benji Saltz
#15/03/18
#tower of hanoi
class Stack:
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
    
    def validMove(self,other):
        if self.items != [] and (other.items == [] or self.peek() < other.peek()):
            other.push(self.pop())
        elif other.items != [] and (self.items == [] or other.peek() < self.peek()):
            self.push(other.pop())
            
    def PrintTower(self,other,another):
        print ("Move", moves,"\n",source.items,"\n",temp.items,'\n',dest.items,'\n')      

source = Stack()
temp = Stack()
dest = Stack()
moves = 0
num = int(input("enter the number of disks you want: "))
for a in range(num,0,-1):
    source.push(a)
    
source.PrintTower(temp,dest)
if num%2 == 1:
    while True:        
        source.validMove(dest)
        moves +=1        
        source.PrintTower(temp,dest)
        if dest.size() == num:
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
