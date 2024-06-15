def leapyear(x):
   if not x%400:
       return('Ture')
   elif not x%4 and x%100:
       return('Ture')
   else:
       return()
       
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

