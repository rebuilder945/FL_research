def leapyear(x):
       if years%400 == 0 or (years%4 == 0 and years%100!=0):
           return True
       else:
           return False
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

