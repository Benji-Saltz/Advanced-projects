##Benji Saltz
##02/05/17
##Programs 1,2,3,4

##1. List of Factors
##Description: Prints factors 
for i in range(2,21): ##Loop that runs through numbers 2 to 20
    list_=[]
    for j in range(1,i+1):##Loop that runs through numbers and later adds combinations to a list 
        if i%j==0:
            list_.append(j)##adds factors to a list 
    print(list_)##Prints lists 

##2. Day of the Year
##Description: To run the program to find the day of the year, type dayYear(enter a day here, enter a month here) then run to find day of the year
days=[31,28,31,30,31,30,31,31,30,31,30,31]## list that has all the months days stored
print("Welcome to the program which outputs a day of the year!")
day=int(input("Enter the day of a month as a number: "))
month=int(input("Enter the number that represents a month: "))
def dayYear(day, month): ## allows the user to input an amount of days and a month ex. dayYear(15,5)
    final=0
    for i in range(month-1):## due to lists starting from 0, month sets back one to start calling months from january, which is [0]
        final+=days[i]##adds days from months to final days
    final+=day##adds days remaining to days 
    return final## returns final amounth of days
print("They day of the year is",dayYear(day,month))



## 3. Natural Number
##Description: Finds value e 
num1 = 1
print("Watch numbers equal to e")
def naturalNum(num):##Creates e
    final = num
    for i in range(num-1, 0, -1):
        final *= i
    return final
for i in range(1,11):
    num1 += 1/naturalNum(i)# takes num1 (1) and divides it by numbers from 1 to 10 to get the number 'e'
    print("e= 1 divided by",str(i)+'!'," = ",num1)
print("The number e equals ",num1)

##4. Prints and Patterns
##Description: Will be prompted to write an input to be used as a pattern
word= input("Enter a word to insert into a Pattern!: ")## Input a word
for i in range(len(word)):
    print(word[i:])#Prints word and removes the starting letter and runs until there is no more letters to delete
print()
for i in range(len(word)):
    print(" "*i+word[i:])#Prints word but adds spaces to replace starting letters which are deleted
print()
for i in range(len(word)):
    for j in range(i):
        print(" ",end= "")## makes pyramid like spaces 
    for j in range(len(word)-i):
        if j+1 == len(word)-i:
            print(word[j])
        else:
            print(word[j]+'-',end= "")##prints word with dashes in between letters and deletes a letter each line
print()
for i in range(len(word)):
    print(' '*i, end='')
    print(word[::-1]+ word)##inverts and deletes last letter in word each line
    word=word[:len(word)-1]
    

        
    
            


