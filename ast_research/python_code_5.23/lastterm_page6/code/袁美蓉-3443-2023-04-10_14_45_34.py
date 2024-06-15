def leapyear(x):
   if x//400 and x//4 not x//100:
      print(x)
   else:
       print(x)
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

