money=input("")
if money[0]=='$':
   M=eval(money[1:])*6.78
   print("&%.2f"%(M))
elif money[0]=='&':
   N=eval(money[1:])/6.78
   print("$%.2f"%(N))
elif money[0:3]=='USD':
   X=eval(money[3:])*6.78
   print("RMB%.2f"%(X))
elif money[0:3]=='RMB':
   Y=eval(money[3:])/6.78
   print("USD%.2f"%(Y))
else:
   print("Error")
