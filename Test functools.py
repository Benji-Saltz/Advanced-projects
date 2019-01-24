from functools import lru_cache

@lru_cache(maxsize=1000)
def fabonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fabonacci(n-1)+fabonacci(n-2)
for n in range(1,50):
    print(n,":",fabonacci(n))
        
