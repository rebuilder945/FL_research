def leapyear(x):
   if not x%400 or (not x%4 and x%100):
           return("In %d February has 29 days."%x)
   else:
           return("In %d February has 28 days."%x)
           
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

