def leapyear(x):
   if x//400 or (x//4 and not x // 100):
       return 1
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

