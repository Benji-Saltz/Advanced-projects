#Benji Saltz
#20/02/18
#Dictionary Q1: Dice- Creates a list of dice rolls
frequency={}
matrix=[i+j for i in range(1,7) for j in range(1,7)]
for i in matrix:
    frequency[i]= frequency.get(i,0)+1
print("The frequncy at the moment is: ", frequency)
