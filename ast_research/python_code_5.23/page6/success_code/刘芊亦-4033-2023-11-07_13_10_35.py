def leapyear(x):
      if(year%400==0):
             return True
      elif(year%4==0 and year%100!=0):
             return True
      else: 
             return False
year=int(input())
if leapyear(year):
    print("In %d February has 29 days."%year)
else:
    print("In %d February has 28 days."%year)

