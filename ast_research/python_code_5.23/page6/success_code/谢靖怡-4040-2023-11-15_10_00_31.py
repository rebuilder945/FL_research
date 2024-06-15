x=input()
if x[0] in("$"):
   z=(eval(x[1:]))*6.78
   print("&%.2f"%z)
elif x[0:3] in("USD"):
   Z=(eval(x[3:]))*6.78
   print("RMB%.2f"%Z)
elif x[0] in("&"):
   z=(eval(x[1:]))/6.78
   print("$%.2f"%z)
elif x[0:3] in("RMB"):
   z=(eval(x[3:]))/6.78
   print("USD%.2f"%z)
else:
   print("Error")
