##Benji Saltz
##02/05/17
##7.Standard Deviation
##Description: input 20 marks and the program will output the standard deviation

marks = []
total = 0
differences = []
totalDifference = 0
count=1
print("Enter 20 marks to calculate standard deviation: ")

for i in range(20):
    countstr=str(count)
    if count>=1 and count<=10:## Makes for count to allow pronouns to be added to the numbers
        if count%10==1:
            countstr+='st'
        elif count%10==2:
            countstr+='nd'
        elif count%10==3:
            countstr+='rd'
        else:
            countstr+='th'
    else:
        countstr+='th'
    while True:
        try:
            marks.append(int(input("Enter the "+countstr+" mark: ")))
            break
        except:
            print("Try again")## If a mark is not given
    count+=1

for i in marks:
    total += i

mark = total // len(marks)

for i in marks:#starting of calculation of marks
    differences.append((i-mark)**2)

for i in differences:
    totalDifference += i

average = totalDifference / len(differences)

standardDeviation = round(average**0.5,2)

print("The standard deviation of the 20 marks is:", standardDeviation)##Prints standard deviation

