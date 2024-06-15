def leapyear(x):
   def leapydeear(n):
       if n%100!=0 and n%4==0:
           return True
       elif n%100==0 and n%400==0:
           return True
           
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

