def leapyear(x):
       if x % 400 == 0:
           return 0 == 0
       elif x % 4 == 0:
           if x % 100 == 0:
               return 0 == 1
           else:
               return 0 == 0
       else:
           return 0==1
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

