def leapyear(x):
   if x//400 or x//4 and x not %100==0:
     print(True)
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

