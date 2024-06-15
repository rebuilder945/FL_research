def leapyear(x):
   if x/400 == int(x/400) :
       return True
   else:
       if x / 4 == int(x / 4) and x / 100 != int(x / 100):
           return True
       else:
           return False
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

