def leapyear(x):
   ( x//4 and not x//100 )  or x//400
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

