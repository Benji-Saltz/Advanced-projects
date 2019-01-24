#Benji Saltz
#February 7th, 2018
#Question 5 - Letter Game
from random import randint as r
startagain=True
string='qwertyuiopasdfghjklzxcvbnm' ##Input of all possible characters
win==0
while startagain==True:
    letter=string[r(0,len(string))]
    print(letter)
    points=50
    while points>0:##Makes sure points are greater than zero
        if points!=50:
            print('You have '+str(points)+' points.')
        while startagain==True:
            try:
                guess=str(input("Enter a word: "))
                break
            except:
                print("That is not an input")##Makes sure inputs are 
        if guess.count(letter)==1:
            print('There is 1 secret letter in that word')
        else:       
            print('There are '+str(guess.count(letter))+' secret letters in that word')
        if guess.count(letter)<1:## If no letters are guessed, player loses 10 points
            points-=10
        elif guess.count(letter)>=1 and guess.count(letter)<5:## If player guesses the letter but it is less than 5, they lose 5 points that round
            points-=5
        else:
            break
    if points<=0:
        print('You lose :(')
        break
    else:
        print('Congratulations, you won!')
        win++1
        print(win)

            
        
        
        
    

        
