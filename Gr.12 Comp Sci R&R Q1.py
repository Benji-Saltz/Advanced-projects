file='data.txt'
file_in = open(file,'r')     # read()
data = file_in.read()         # Returns one string containing the entire file.
equal=[]
for i in data:
    if i not in equal:
        numbers.append(i)
print (equal)
file_in.close()
