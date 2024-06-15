def leapyear(x):
   leap=false
   if x%4==0:
     if x %100==0:
       if x%400==0:
         leap=true
   return leap

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

