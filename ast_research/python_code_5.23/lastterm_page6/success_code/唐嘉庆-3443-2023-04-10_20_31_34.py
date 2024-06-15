def leapyear(x):
   if year%400==0:
       return 29
   if year%4==0 and year%100 !=0:
       return 29
   else:
       return 28
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

