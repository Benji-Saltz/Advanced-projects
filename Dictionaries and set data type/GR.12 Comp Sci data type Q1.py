#Benji Saltz
#20/02/18
#Set data type Q1: Students in sports- Students are placed into lists which is sorted by different criteria 

FOOTBALL= set(['John', 'Jack', 'Jason', 'Justin', 'Ivan', 'Ryan', 'Paul', 'Simon', 'Leon', 'Noah'])
SOCCERBALL= set(['Noah', 'Mark', 'Michael', 'Ivan', 'Gal', 'Daniel', 'Ben', 'Ryan'])
BASKETBALL=set(['Lucas', 'Noah', 'Andrew', 'Jason', 'Leon', 'Paul', 'David'])

#Shows students in all three sports
print('This is a list of the students who play any of the three sports: ', FOOTBALL|SOCCERBALL|BASKETBALL)
#Students in only soccer and basketball
print('This is a list of students who play only soccer and basketball: ', SOCCERBALL&BASKETBALL)
#Students who only play one sport
print('This is a list of the students who play only a single sport: ', FOOTBALL^SOCCERBALL^BASKETBALL)
#Students who play all three of the sports
print('This is a list of the students who play all of the three sports: ', FOOTBALL&SOCCERBALL&BASKETBALL)
#Students who only play football and soccer
print('This is a list of people who play football and soccer exclusivly: ',(FOOTBALL&SOCCERBALL)-BASKETBALL)
