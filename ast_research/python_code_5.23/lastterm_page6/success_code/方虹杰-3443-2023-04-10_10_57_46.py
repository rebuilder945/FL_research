def leapyear(x):
           n=year
           if n%4==0:
                   return leapyear
           else:
                   return None
         
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

