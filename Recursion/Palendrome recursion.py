##By: Benji Saltz
##Date March 27, 2018
##Description: Program finds out if a word is a palendrome or not.
from functools import lru_cache
@lru_cache(maxsize=1000)
def Pal(word1):
    word1=word1.lower()
    if len(word1)<=1:#if the word is a letter or less, then return the letter as it is its own word.
        return True
    else:
        if word1[0]==word1[-1]:          #this sequence covers that if the first and last letter are the same, then the function will call itself again but only includes inner letters,
            return Pal(word1[1:-1])      #and will shut down until all letters are checks to be the same starting on the outer layer and checking inward.
        else:
            return False

word1=str(input("Enter a word to check if it is a palendrome: "))
if Pal(word1)==True:
    print("the word",word1,"is a palendrome")
else:
    print("The word",word1,"is not a palendrome!")
