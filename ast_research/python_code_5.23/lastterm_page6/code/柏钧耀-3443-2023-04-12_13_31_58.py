def leapyear(x):
   if year%4=0：
       a=True
   else:
       a=False
   return a
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

