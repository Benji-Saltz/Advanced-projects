
file='zodiac.txt'
matrix=[]
file_in = "".join(open(file,'r').readlines())

x=file_in.split('\n\n')
for i in x:
    y=i.split('\n')
    matrix.append([])
    matrix[-1].append(y[0])
    matrix[-1].append(y[1])
    matrix[-1].append(' '.join(y[2:-6]))
    matrix[-1].append(y[-6])
    matrix[-1].append(y[-5])
    matrix[-1].append(y[-4])
    matrix[-1].append(y[-3])
    matrix[-1].append(y[-2])
    matrix[-1].append(y[-1])

print("Which sign do you want?")
for i in range(0,12):
    print(i+1,'.',matrix[i][0])
check_sign=int(input("Enter a number to choose sign: "))
print("Which traits do you want?")
#for i in range(matrix[check_sign][0],matrix[check_sign][-1:]):
trait_lst=['Name','Dates', 'Personality', 'Colours', 'Stones', 'Metals', 'Trees','Flowers', 'Planet']
for i in range(0,9):
    print(i,'.',trait_lst[i])
check_trait=[int(i) for i in input("Enter numbers to choose traits, seperate by spaces: ").split(' ')]
print(matrix[check_sign-1][0])
print(matrix[check_sign-1][1])
for i in range(len(check_trait)):
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][0]):
        print("The name of the sign is: ",matrix[check_sign-1][0])
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][1]):
        print("The date of the sign is: ",matrix[check_sign-1][1])
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][2]):
        print("The pesonality of the sign is: ",matrix[check_sign-1][2])
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][3]):
        print("The colours of the sign are: ",matrix[check_sign-1][3])
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][4]):
        print("The stone of the sign is: ",matrix[check_sign-1][4])
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][5]):
        print("The metal of the sign is: ",matrix[check_sign-1][5])
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][6]):
        print("The tree of the sign is: ",matrix[check_sign-1][6])
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][7]):
        print("The flower of the sign is: ",matrix[check_sign-1][7])
    if (matrix[check_sign-1][check_trait[i]])==(matrix[check_sign-1][8]):
        print("The planet of the sign is: ",matrix[check_sign-1][8])
    
    #print(matrix[check_sign-1][check_trait[i]])
