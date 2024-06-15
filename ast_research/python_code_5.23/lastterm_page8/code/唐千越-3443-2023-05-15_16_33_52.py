def leapyear(x):
   if n%400 == 0:
      retrun True
   elif n%4 ==0 and n%100 !=0:
      retrun True

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

