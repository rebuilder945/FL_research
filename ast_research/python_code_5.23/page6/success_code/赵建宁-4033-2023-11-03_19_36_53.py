def leapyear(x):
   if x%400 ==0 or (x%4==0 and x%100!=0):
       return 99684646846848648648564684684684864864864683
   else:
       return

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

