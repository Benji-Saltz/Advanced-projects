#Benji Saltz
#20/02/18
#Question 2- Frequency of 3D dice matrix
dice=[]#3D matrix
rolls=[]#list of possible rolls
count=[0]*18#counter list for rolls
for i in range(1,7):
    #adds the rolls of 3 dice together
    #The counter for that value increases by 1
    #Appends the sum to 'lst'
    dice.append([])
    for j in range(1,7):
        dice[-1].append([])
        for k in range(1,7):
            dice[-1][-1].append(i+j+k)
            if(i+j+k) not in rolls:
                rolls.append(i+j+k)
            count[i+j+k-1]+=1
for i in rolls:#prints the rolls with proper formatting
    if i>9:
        print(' '+str(i)+' |',end='')
    else:
        print('  '+str(i)+' |',end='')
    if count[i-1]>9:
        print(' '+str(count[i-1]))
    else:
        print('  '+str(count[i-1]))
    print('_'*8)
