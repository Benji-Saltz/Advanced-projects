#Benji Saltz
#20/02/18
#Question 4- Zero Function
from random import randint as r
while True:
    try:
        lstrange=int(input("Enter how many collumns and rows you want: "))
        break
    except:
        print('Invalid input')
        
def zero(lst):
    lstzeros=[]
    for i in range(len(lst)):
        lstzeros.append([])
        for j in lst[i]:
            if j==0:
                lstzeros[-1].append(True)
            else:
                lstzeros[-1].append(False)
    for i in range(len(lstzeros)):
        for j in range(len(lstzeros[i])):
            if lstzeros[i][j]:
                for k in range(len(lst)):
                    lst[k][j]=0
                    for l in range(len(lst[k])):
                        lst[i][l]=0
    
    print('Your edited list is: ')
    for i in range(len(randlist)):
        for j in randlist[i]:
            print(' '+str(j)+' |',end='')
        print('')
        print('____'*lstrange)
   
randlist=[]
for i in range(lstrange):
    randlist.append([])
    for j in range(lstrange):
        randlist[-1].append(r(0,9))
print('Your list is: ')
for i in range(len(randlist)):
    for j in randlist[i]:
        print(' '+str(j)+' |',end='')
    print('')
    print('____'*lstrange)
zero(randlist)

