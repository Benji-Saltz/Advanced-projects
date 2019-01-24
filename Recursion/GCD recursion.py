##By: Benji Saltz
##Date March 27, 2018
##Description: Finds the greatest common divisor of two numbers
from functools import lru_cache
@lru_cache(maxsize=1000)
def GCD(num1,num2): #function finds the greatest common divisor. This is done by recycling in the numbers until a result is given with no remainder, then takes the greater integer.
    answer=num1%num2
    if answer==0:
        return num2
    else:
        return GCD(num2, answer)   
num1=(int(input("Enter a number: ")))
num2=(int(input("Enter another number: ")))
print("GCD is: ", str(GCD(num1,num2)))
