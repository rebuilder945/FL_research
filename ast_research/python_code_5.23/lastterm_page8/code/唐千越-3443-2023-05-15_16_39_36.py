def leapyear(x):
   if x%400 == 0 or (n%4 ==0 and n%100 !=0):
      retrun True
   else:
      retrun False

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

