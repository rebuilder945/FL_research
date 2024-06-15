def leapyear(x):
   if x%4!=0:
       return False
   else:
       if x%100!=0:
           return False
       else:
           return True
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

