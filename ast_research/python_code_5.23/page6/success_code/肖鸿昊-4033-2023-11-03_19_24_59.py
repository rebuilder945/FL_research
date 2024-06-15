def leapyear(x):
   if year%4==0 and year%100!=0:
       if year%400==0:
            return True
       else: 
           return Flase 
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

