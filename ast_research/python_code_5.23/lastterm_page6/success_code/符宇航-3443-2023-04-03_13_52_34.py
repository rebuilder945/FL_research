def leapyear(x):
   if x // 400 == 0 or x//4==0 and x//100 != 0:
         n = 1
   else:
         n = 0
   return n
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

