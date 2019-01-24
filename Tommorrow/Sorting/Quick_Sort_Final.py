##By: Benji Saltz
##Date: 01/04/18
##Description: This program includes quick selection, which contains a pivot point, and the program will move a digit left or right of the point if the integer is less or greater 
def quick_sort(beep):
    if len(beep) < 2:
        return beep
    else:
        pivot = beep[0]
        left_piv = []#Saves left of pivot
        right_piv = []#Saves right of pivot
        piv = []
        for i in beep:#Sorts to left of right of chosen pivot point, else it stays
            if i>pivot:
                right_piv.append(i)
            elif i<pivot:
                left_piv.append(i)
            else:
                piv.append(i)
    return quick_sort(left_piv)+piv+quick_sort(right_piv)
boop = [2,3,4,5,1]
print("Input list: ",boop)
print("Output lsit: ",quick_sort(boop))
    
