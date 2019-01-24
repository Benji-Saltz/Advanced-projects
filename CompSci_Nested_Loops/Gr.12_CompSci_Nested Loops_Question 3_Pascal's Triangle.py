#By: Benji Saltz
#20/02/18
#Question 3- Pascals triangle printed 
tri=[]
for i in range(10):
    tri.append([])
    for i in range(10):
        tri[-1].append(1)
for i in range(len(tri)):
    for j in range(len(tri[i])):
        if i is not 0 and j is not 0:
            tri[i][j]=int(tri[i][j-1]+tri[i-1][j])
for i in range(len(tri)):
    for j in tri[i]:
        print(' '*(8-len(str(j))),end='')
        print(j,end='')
    print('')
    
