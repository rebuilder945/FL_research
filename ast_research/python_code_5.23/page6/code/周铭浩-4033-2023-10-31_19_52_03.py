def leapyear(x):
       if x>=400:
           if x%400==0:
               reverse 1==1
           else:
               reverse 1==2
       else:
           if x%4==0 and x%100!=0:
               reverse 1==1
           else:
               reverse 1==2
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

