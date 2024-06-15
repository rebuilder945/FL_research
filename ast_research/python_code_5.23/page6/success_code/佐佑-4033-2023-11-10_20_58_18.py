def leapyear(x):
   def  leapyear(x):
       if x%4==0:
           True
     
       else:
           False
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

