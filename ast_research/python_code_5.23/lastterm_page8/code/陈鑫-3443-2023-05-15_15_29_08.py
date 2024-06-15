def leapyear(x):
   if year%4==0:
       if year%400==0:
           retrun True
       elif year%100==0:
           return False
       else:
           retrun True
   else:
       return False
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

