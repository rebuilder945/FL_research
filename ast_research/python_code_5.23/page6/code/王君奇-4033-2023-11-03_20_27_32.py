def leapyear(x):
   if x//400==1 or (x//4==1 and x//4:=1):
      return 1
   else:
      return 0
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

