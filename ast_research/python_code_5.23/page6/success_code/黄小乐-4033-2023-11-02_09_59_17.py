def leapyear(x):
       x=int(x)    
       x%400==0 or x%4==0
   
       
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

