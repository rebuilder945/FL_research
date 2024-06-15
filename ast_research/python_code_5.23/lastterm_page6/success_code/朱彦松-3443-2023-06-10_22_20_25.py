def leapyear(x):
   if mon % 400 == 0:
       print("In %d February has 29 days." % mon)
   elif mon % 4 == 0 and mon % 100 != 0 :
       print("In %d February has 29 days." % mon)
   else:
       print("In %d February has 28 days." % mon)
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

