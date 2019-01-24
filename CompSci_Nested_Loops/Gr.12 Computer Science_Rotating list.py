#Benji Saltz
#20/02/18
#Question 5- Rotating list
from random import randint as r
while True:
    try:
        num=int(input('Enter the number of rows or columns you want there to be in a 2D list: '))
        if 3<=num<=6:
            break
        else:
            print('Invalid size')
    except:
        print('Invalid input')
randlist=[]
for i in range(num):
    randlist.append([])
    for j in range(num):
        randlist[-1].append(r(0,9))
print('Your list is: ')
for i in range(len(randlist)):
    for j in randlist[i]:
        print(' '+str(j)+' |',end='')
    print('')
    print('____'*num)
    
print(randlist)
def rot(lst):
    newlist=[]
    for i in range(len(lst)):
        newlist.append([])
        for j in range(len(lst[0])-1,-1,-1):
            newlist[-1].append(lst[j][i])
    
    print('Your list rotated 90 degrees is: ')
    for i in range(len(newlist)):
        for j in newlist[i]:
            print(' '+str(j)+' |',end='')
        print('')
        print('____'*num)
rot(randlist)

