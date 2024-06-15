def leapyear(x):
   if  x//400:
       return 1
   elif  (x//4 and not x//100):
       return 1
   else:
       return 0
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

