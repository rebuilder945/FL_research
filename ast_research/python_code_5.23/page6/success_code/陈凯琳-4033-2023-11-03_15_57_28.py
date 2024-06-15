def leapyear(x):
   if not x%400 or (not x%4 and x%100):
           return(x)
   else:
           return(None)
           
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

