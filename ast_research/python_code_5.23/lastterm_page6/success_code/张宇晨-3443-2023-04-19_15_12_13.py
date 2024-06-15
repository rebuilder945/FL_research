def leapyear(x):
       if x%400:
           a=0
       elif x%4:
           a=0
       else:
           a=1
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

