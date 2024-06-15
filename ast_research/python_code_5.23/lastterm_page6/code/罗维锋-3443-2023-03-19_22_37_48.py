def leapyear(x):
   if x%400==0:
      s=1
   elif:
        x%4==0 and x%100!=0
       s=1
   else:
       s=0
   return s
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

