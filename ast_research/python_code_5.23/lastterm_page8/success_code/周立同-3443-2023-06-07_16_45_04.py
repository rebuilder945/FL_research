def leapyear(x):
       if x/400==x//400:
           return True
       elif x/4==x//4 and x/100!=x//100:
           return True
       else:
           return False

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

