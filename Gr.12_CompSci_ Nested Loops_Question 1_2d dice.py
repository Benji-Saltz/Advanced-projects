#Benji Saltz
#20/02/18
#Question 1- 2D Dice Matrix: The rows represent one die, while the columns represent another die, all rolls are added up as such 
print("Welcome to the 2D Dice Matrix! Here you will see the addition of dice rolls from least to greatest, with rows representing one die, and the columns representing the other. the Rolls of one die and the other will be added and put into the matrix ")
dice=[]
for i in range(1,7):#creates the 6 by 6 2D matrix
    dice.append([])
    for j in range(1,7):#Adds rolls of each die from least to greatest
        dice[-1].append(i+j)
for i in range(len(dice)):#prints the possible rolls with proper formatting
    for j in dice[i]:
        if j>9:
            print(' '+str(j)+' |',end='')
        else:
            print('  '+str(j)+' |',end='')
    print('')
    print('_'*30)
