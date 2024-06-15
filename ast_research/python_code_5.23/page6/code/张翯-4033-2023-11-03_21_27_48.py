def leapyear(x):
   if year%400==0 or (year%==0 and year%100!=0):
      return 1
   else：
      return 0
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

