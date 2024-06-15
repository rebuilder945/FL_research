def leapyear(x):
       if x%100!=0 and x%4==0:
           a=0
       return a
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

