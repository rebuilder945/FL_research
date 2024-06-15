def leapyear(x):
       if x%400==0:
           return 1 == 1
       else:    
           if x%100==0:
               return 1 == 0
           elif x%4==0:
               return 1 == 1
           else:
               return 1 == 0

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

