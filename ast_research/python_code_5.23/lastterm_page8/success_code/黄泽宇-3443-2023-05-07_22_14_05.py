def leapyear(x):
   
    if x%4 != 0 and (x%100 == 0 and x%400 != 0):
     flag=True
    else:
     flag=False
    return flag
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

