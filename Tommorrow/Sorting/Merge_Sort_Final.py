##By: Benji Saltz
##Date:01/04/18
##Descripton: This program includes sort selection
def sortArray(l_lst,r_lst,beep):
    len_l=len(l_lst)
    len_r=len(r_lst)
    cnt_l=0
    cnt_r=0
    cnt=0
    while(cnt_l<len_l and cnt_r<len_r):
        if(l_lst[cnt_l]<r_lst[cnt_r]):
            beep[cnt]=(l_lst[cnt_l])
            cnt_l+=1
            cnt+=1
        else:
            beep[cnt]=(r_lst[cnt_r])
            cnt_r+=1
            cnt+=1
    while(cnt_l<len_l):
        beep[cnt]=(l_lst[cnt_l])
        cnt_l+=1
        cnt+=1
    while(cnt_r<len_r):
        beep[cnt]=(r_lst[cnt_r])
        cnt_r+=1
        cnt+=1
            

def merge_sort(beep):
    if len(beep) < 2:
        return 
    else:
        middle = len(beep)//2
        left=beep[0:middle]
        right=beep[middle:len(beep)]
        merge_sort(left)
        merge_sort(right)
        sortArray(left, right,beep)

boop=[2,3,4,5,1]
print("Input List:",boop)
merge_sort(boop)
print("Output List:",boop)
