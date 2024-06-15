def leapyear(x):
   x//400 or not x//100 or x//4
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

