def leapyear(x):
   if x%4==0:
           if x%100==0:
               if x%400==0:
                   True
               else:
                   False
       else:
           False

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

