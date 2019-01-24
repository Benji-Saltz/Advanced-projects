#Benji Saltz
#20/02/18
#Question1- 2D Dice Matrix: The rows represent one die, while the columns represent another die, all rolls are added up as such 
dice=[]
for i in range(1,7):#makes a 6x 6 2D matrix
    dice.append([])
    for j in range(1,7):#Fills the 2D matrix with the combined rolls of dice
        dice[-1].append(i+j)
for i in range(len(dice)):#prints the possible rolls with proper formatting
    for j in dice[i]:
        if j>9:
            print(' '+str(j)+' |',end='')
        else:
            print('  '+str(j)+' |',end='')
    print('')
    print('_'*30)
