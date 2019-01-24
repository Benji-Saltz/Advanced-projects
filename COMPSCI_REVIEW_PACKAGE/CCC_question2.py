import sys
input=sys.stdin.readline
N=int(input())
chart=[]
for i in range(N):
    chart.append(list(map(int,input().split())))
good=False

while good==False:
    good=True
    for i in range(len(chart)-1):
        if chart[0][i]>=chart[0][i+1]:
            good=False
    for i in range(len(chart)-1):
        if chart[i][0]>=chart[i+1][0]:
            good=False
    if good== False:
        rotated = list(zip(*reversed(chart)))
        for i in range(len(chart)):
            for j in range(len(chart[0])):
                chart[i][j] = rotated[i][j]
for i in range(len(chart)):
    for j in range(len(chart[i])):
        if j>0:
            print(" ", end= '')

        print(str(chart[i][j]), end='')
    print()
                
    
                
                
