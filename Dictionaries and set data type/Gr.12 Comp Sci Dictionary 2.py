#Benji Saltz
#20/02/18
#Dictionary Q2: Class mark organizer- Organizes students into lists with equal marks
s_to_m= {'Benji':95,'Jerry':90,'Larry':80,'Harry':75,'Barry':70,'Gary':85,'Terry':70,'Sari':85,'Carrey':32,'Richard':85} #dictionary containing marks
print("The original list of class marks is: ",s_to_m)
m_to_s={}
for i in s_to_m: #sorts students into lists with equal marks
    marks=s_to_m[i]
    if not (marks in m_to_s):
        m_to_s[marks]=[i]
    else:
        m_to_s[marks].append(i)
print("The class organized with same marks: ", m_to_s)
