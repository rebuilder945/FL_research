def leapyear(x):
   x=int(input())
   if x%400==0 or (x%4==0 and x%100 !=0):
       print("in %d February has 29 days."%x)
   else:
       print("in %d February has 28 days."%x)
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

