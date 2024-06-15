def leapyear(x):
   a=0
   b=x%4
   a==b
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

