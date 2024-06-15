def leapyear(x):
   a=1
   if x%400==0:
               a=1
   elif x%4==0 and x%100!=0:
       a=1
   else:
       a=0
   return a
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

