def leapyear(x):
   a=0
   if a==x%4:
      pass
      return a==x%4
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

