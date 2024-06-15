def leapyear(x):
       if x%4:
           a=0
           return a
       else:
           a=1
           return a
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

