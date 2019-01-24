from functools import lru_cache
@lru_cache(maxsize=1000)
def ana(word2):
    if len(word2)==0:
        return ['']
    else:
        lst=[]
        for i in ana(word2[1:]):
            for j in range(len(i)+1):
                lst.append(i[:j]+word2[0]+i[j:])
        return list(set(lst))

word=input(str('Enter a word to get its anagrams: '))
word1=input(str('Enter another word to check if it is an anagram of the word '+word+':  '))

lst=ana(word)
word2=''
for i in lst:
    word2+=i+', '
word2=word2[:-6]+'and '+word2[-6:-2]+'.'
    
print('The anagrams of your word are: '+word2)
if word1 in ana(word):
    print(word1+' is an anagram of '+word+'.')
else:
    print(word1+' is not an anagram of '+word+'.')
