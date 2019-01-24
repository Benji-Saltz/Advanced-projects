##Benji Saltz
##02/05/17
##6.Combinations and Duplicates
##Description: type combandDup() to be prompted to input letters and numbers which will be sorted into combinations and duplicates
string="qwertyuiopasdfghjklzxcvbnm"
isString=False
def combandDup(l):
    combination=[]
    duplicate=[]
    if isString:
        for i in (l):
            for j in (l):
                if i==j: ## Finds duplicates as the value if it runs twice will find its equal value
                    duplicate.append(str(i) + str(j))
                else:## Creates all possible combinations
                    combination.append(str(i) + str(j))
    else:
        for i in (l):
            for j in (l):
                if i==j: ## Finds duplicates as the value if it runs twice will find its equal value
                    duplicate.append(int(str(i) + str(j)))
                else:## Creates all possible combinations
                    combination.append(int(str(i) + str(j)))
    
    print(" The duplicates are: ",'\n',duplicate)##Prints duplicates and combinations
    print("The combinations are: ",'\n',combination)

while True:
    try:
        input_list= (input(str("Type numbers to find the combinations and duplicates, but put spaces between values: "))).split()
        input_list=list(input_list)
        for i in string:
            if i in input_list:
                isString=True
        if isString:
            for i in range(len(input_list)):
                input_list[i]=str(input_list[i])
            break
        else:
            for i in range(len(input_list)):
                input_list[i]=int(input_list[i])
            break
    except:
        print('Invalid input')
combandDup(input_list)
