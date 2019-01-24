fibonacci_cache={}

def fabonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fabonacci(n-1)+fabonacci(n-2)
    fibonacci_cache[n]=value
    return value
for n in range(1,50):
    print(n,':',fabonacci(n))
