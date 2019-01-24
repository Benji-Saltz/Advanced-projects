import sys
input=sys.stdin.readline
N=int(input())
v=[]
r=[]
b=[]
for i in range(N):
    v.append(int(input()))
v.sort()

for i in range (len(v)-1):
    r.append((v[i]+v[i+1])/2)
for i in range(len(r)-1):
    b.append(r[i+1]-r[i])
print(min(b))



