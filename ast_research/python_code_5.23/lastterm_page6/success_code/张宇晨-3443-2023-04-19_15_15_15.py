def leapyear(x):
       if x%400==0:
           a=1
       elif x%4:
           a=0
       else:
           a=1
       return a
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

