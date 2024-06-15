def leapyear(x):
   if (n%4==0 and n%100!=0) or (n%400==0):
       return True
   else:
       return False
       
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

