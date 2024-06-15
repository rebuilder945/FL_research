def leapyear(x):
   if x%4==0 or x%400==0:
           0=Flase
   else:
           1=Flase
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

