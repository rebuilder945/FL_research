def leapyear(x):
   def  leapyear(x):
       if year%400==0:
           print("In %d February has 29 days"%year)
       elif (year%4==0) and (year%100!=0):
           print("In %d February has 29 days"%year)
       else:
           print("In %d February has 28 days"%year)
           
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

