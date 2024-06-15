def leapyear(x):
       a=x%400
       b=x%4
       c=x%100
       if a==0:
           return year
       elif b==0 and c!=0:
           return year
       
           
           
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

