def leapyear(x):
   return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

