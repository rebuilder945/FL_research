def leapyear(x):
   a = x%4
   if int(a) =  0:
    print("In  %d  February  has  29  days."%x)
    
    
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

