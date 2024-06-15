def leapyear(x):
   a=False
   if x%400==0:
       a=True
   elif x%4==0 and x%100 !=0:
       a=True
   return a
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

