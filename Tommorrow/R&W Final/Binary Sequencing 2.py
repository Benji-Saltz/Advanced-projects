#By: Benji Saltz
#Date: 03/15/18
#R&W Q4
in_file=open('in_file.txt','r')
in_seq=in_file.read()
in_file.close()

out_seq=''
exit_now=False
in_list=in_seq.split(' ')
print("Input:",in_seq)
for item in in_list:
    if(exit_now==False):
        for c in item:
            if(exit_now==False):
                if c<'0' or c>'9':
                    print('Illigal input: use numbers only')
                    exit_now=True
                
if len(in_list)<2:
    print('Illigal input: too short')
    exit_now=True
    
if(exit_now==False):
    if(int(in_list[0])==0):
        c=' 1'
        out_seq='0'
        for l in in_list[1:]:
            out_seq+=c*int(l)
            if c==' 1':
                c=' 0'
            else:
                c=' 1'
    else:
        if(int(in_list[0]) != (len(in_list)-1)):
            print('Illigal input: length doesn\'t match')
        else:
            c=' 0'
            count=0
            for l in in_list[1:]:
                count+=int(l)
                out_seq+=c*int(l)
                if c==' 1':
                    c=' 0'
                else:
                    c=' 1'
            out_seq=str(count)+out_seq
out_file=open('out_file.txt','w')
out_file.write(out_seq)
out_file.close()
print("Output:",out_seq)
