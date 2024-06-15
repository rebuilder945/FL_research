def leapyear(x):
   leapyear=0
       if x%400==0 or (x%4==0 and x%100!=0):
           leapyear+=1
       return leapyear

year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

