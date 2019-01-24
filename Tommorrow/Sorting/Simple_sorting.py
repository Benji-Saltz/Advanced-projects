##By: Benji Saltz
##Date: 01/04/18
##Descripton: This program includes bubble, selection and insertion sort
def bubble(beep):
    for i in range(0, len(beep)-1): 
        for j in range(0,len(beep)-1-i):
            if beep[j]>beep[j+1]: #If the left is greater than the right
                beep[j],beep[j+1]=beep[j+1],beep[j]#the numbers switch places in the list
    return beep

def selection(beep):
    for i in range(0,len(beep)-1):
        min_index=i #hold min number out of sorted list
        for j in range(i+1,len(beep)):
            if beep[j]<beep[min_index]:#if the next number in the list is less than the min number unsorted
                min_index=j #that number becomes the min_index
        if min_index !=i: #if the min_index is not the next number, the min and lowest number switch places
            beep[i],beep[min_index]=beep[min_index],beep[i]
    return beep

def insertion(beep):
    for i in range(1, len(beep)):
        for j in range(i-1,0,-1):#starts at last number and works back to zero
            if beep[j]>beep[j+1]: #if the left is greater than the j, switch places
                beep[j],beep[j+1]=beep[j+1],beep[j]
            else:
                break #if not, break
    return beep


boop=[2,3,4,5,1]
print("Input list: ",boop)
print(bubble(boop))
print(selection(boop))
print(insertion(boop))
