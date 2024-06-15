def leapyear(x):
   if year%400 == 0 or (year%4 == 0 and year%100 != 0):
           return leapyear(x)
       else:
           return False
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

