def leapyear(x):
   if int(year)%400=0 or int(year)%4=0
     return True
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

