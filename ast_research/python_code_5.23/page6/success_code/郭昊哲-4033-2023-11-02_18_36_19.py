def leapyear(x):
   a=0
   if x//400==0 or x//4==0:
       a=1
   return a
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

