def leapyear(x):
   if year%4==0:
       if year%400==0:
           return True
       elif year%100!=0:
           return True
       else:
           return False
   
   else:
       return False
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

