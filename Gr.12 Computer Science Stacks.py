#By: Benji Saltz
#Date: 19/03/18
#Stacks and Ques
#Stacks- Need to reverse binary sequence due working from the top
#Ques- Due to working from the back to the front, no need for reversing the sequence
class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items ==[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
stck=Stack()
lst= (int(input("Enter a number to convert to binary: ")))#allows user to input a number to convert to binary

while(lst/2 !=0):
    stck.push(lst%2)#takes remainder of top number
    lst=int(lst/2)
print(stck.items)
while not stck.isEmpty():#checks to see if the stack is empty
    print(stck.pop(),end='')# pops from top of stack so the squence reverses when it prints
print()

class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items ==[]

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
que=Queue()
qlst= (int(input("Enter a number to convert to binary: ")))#allows user to input a number to convert to binary
while (qlst/2 !=0):
    que.enqueue(qlst%2)#takes remainder of last entered number
    qlst=int(qlst/2)
print(que.items)

    
