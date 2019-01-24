#Benji Saltz
#20/02/18
from random import randint as r
randnum=(r(-1,9))
lstrange=int(input("Enter how many collumns and rows you want: "))
lst=[]
for n in range(1):
    for i in range(0,lstrange):
        lst.append([])
        for j in range(0,lstrange):
            lst[-1].append(r(0,9))
    for i in lst:
        for j in i:
            if j>9:
                print(' '+str(j)+' |',end='')
            else:
                print('  '+str(j)+' |',end='')
        print('')
    
##    print("Edited: ")
##        if j=0
##    for i in range(len(lst)):
##        for j in lst[i]:
##            print(' '+str(j)+' |',end='')
##        print('')
        
    
    
    #print('_'*(5*(len(str(lstrange)))))
