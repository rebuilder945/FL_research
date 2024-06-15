def leapyear(x):
   if int(x) %400==0:
       return True
   elif int(x)%4==0 and int(x)%100!=0:
       return True
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

