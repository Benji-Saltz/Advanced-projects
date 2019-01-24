#By: Benji Saltz
#Date: 03/15/18
#R&W Q4
out_seq=''
in_list=[]
in_file=open('q4A.txt','r')
file_data=in_file.read()
in_file.close()
in_list=file_data.split(' ')
print("Input:",file_data)
wrong_char=False
exit_now=False
for item in in_list:
    if wrong_char==False:
        for c in item:
            if(c<'0' or c>'9'):
                wrong_char=True
                exit_now=True
                print('Illegal input: use numbers only')
                break
        
if(len(in_list) < 2):
    print('Illegal input: sequence is too short')
    exit_now=True
        
if(exit_now == False):
    if(int(in_list[0]) == 0):
        if(int(in_list[1])!=1):
            exit_now=True
            print('Illegal input: second number must be 1')
        else:
            out_seq+='0'
            if(len(in_list) == 2):
                out_seq+=' 1'
            else:
                count=1
                for i in range(len(in_list)-2):
                    if(in_list[i+2] == in_list[i+2-1]):
                        count+=1
                    else:
                        out_seq+=' '
                        out_seq+=str(count)
                        count=1
                out_seq+=' '
                out_seq+=str(count)               
                               
    else:
        if(int(in_list[0]) != len(in_list)-1):
            exit_now=True
            print('Illegal input: length doesn\'t match')
        else:
            if(len(in_list) == 2):
                out_seq+='1 1'
            else:
                total=0
                count=1
                for i in range(len(in_list)-2):
                    if(in_list[i+2] == in_list[i+2-1]):
                        count+=1
                    else:
                        out_seq+=' '
                        out_seq+=str(count)
                        count=1
                        total+=1
                out_seq+=' '
                out_seq+=str(count)
                total+=1
                out_seq=str(total)+out_seq
if(exit_now == False):
    print('Output:',out_seq)
