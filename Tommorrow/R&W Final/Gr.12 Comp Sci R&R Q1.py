#By: Benji Saltz
#Date: 15/03/18
#Q1
file = 'data.txt'

in_file = open(file,'r')
data = in_file.read()
data = data.split(' ')
data = data[:-1]
frequency = {}
numbers = []
for i in data:
    if i not in numbers:
        if i != ' ':
            numbers.append(i)
print(numbers)
for i in data:
    frequency[i] = frequency.get(i,0)+1
in_file.close()

out_file = open('frequency.txt','w')
out_file.write(str(frequency))
out_file.close()
