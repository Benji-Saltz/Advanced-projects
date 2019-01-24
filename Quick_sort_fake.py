def quickone(beep):
    quicktwo(beep,0,len(beep)-1)

def quicktwo(beep,low,high):
    if low<high:
        p=partition(beep,low,high)
        quicktwo=(beep,low,p-1)
        quicktwo=(beep,p+1,high)
        
def gepivot(beep,low,high):
    mid=(high+low)//2
    pivot=high
    if beep[low]<beep[mid]:
        if beep[mid]<beep[high]:
            pivot=mid
    elif beep[low]<beep[high]:
        pivot=low
    return pivot

def partition(beep,low,high):
    pivot_index=get_pivot(beep,low,high)
    pivot_value=beep[pivot_index]
    beep[pivot_index],beep[low]=beep[low],beep[pivot_index]
    border=low

    for i range(low,((high)+1)):
        if beep[i]<pivot_value:
            border+=1
            beep[i],beep[border]=beep[border],beep[i]
    beep[low],beep[border]=beep[border],beep[low]
    return border
boop=[2,3,4,5,1]
print(quickone(boop))
            

    
