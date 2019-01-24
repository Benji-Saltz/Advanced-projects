import math
def checkPunc(p_list, char):
    found = False
    for p in p_list:
        if p == char:
            found = True
            break
    return found
w1 = str(input("Enter the first word: "))
w2 = str(input("Enter the second word: "))
index_1 = []
index_2 = []
index = []
d_index1 = 0
d_index2 = 0
distance = 0
file = "frankenstein.txt"
#file='testing_read.txt.txt'
in_file = open(file, 'r')
data = in_file.read()
punctuation = [".","'",",","?","!","","/",'"',":",";","(",")","-","*"]
for i in data:
    if checkPunc(punctuation, i) == True:
        data = data.replace(i,'')
data = data.split()
for i in range(len(data)):
    if w1.lower() == data[i].lower():
        index_1.append(i)
    if w2.lower() == data[i].lower():
        index_2.append(i)
minimum = len(data)+1
for i in index_1:
    for j in index_2:
        distance = abs(i-j)
        index.append(abs(i-j))
        if distance < minimum:
            minimum = distance
            d_index1 = i
            d_index2 = j
if distance > 0:
    print("The shortest distance between the two words is",min(index))
    if d_index1>d_index2:
        print("The passae between the two words is: ",data[d_index2:d_index1+1])
    else:
        print("The passae between the two words is: ",data[d_index1:d_index2+1])
if len(index) == 0:
    print("These words don't exist")
if(w1==w2):
    print("You have selected two of the same words")

                          

