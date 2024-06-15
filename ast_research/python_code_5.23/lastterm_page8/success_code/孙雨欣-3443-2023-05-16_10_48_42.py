def leapyear(x):
       f=True
       if x %400==0:
           return f
       elif x%4==0 and x%100!=0:
           return f
       else:
           f=False
           return f 
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

