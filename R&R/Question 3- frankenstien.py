file='frankenstein.txt'
matrix=[]
file_in =(open(file,'r').readlines())
abc='qwertyuiopasdfghjklzxcvbnm'
for i in file_in(len(matrix)):
    for j in matrix[i]:
        if j not in abc:
            matrix[i]=matrix[i].replace(j,'')
word_1=input('Enter a word to find: ')
word_2=input('Enter a word to find: ')
word_num1= file_in[word_1]
word_num2= file_in[word_2]
for i in file_in(word_num1,word_num2):
    print(file_in[word_num1:word_num2])
##length=len[word_1:word_2]


