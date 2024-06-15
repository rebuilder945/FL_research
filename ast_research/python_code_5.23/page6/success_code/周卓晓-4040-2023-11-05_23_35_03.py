a = input()
if a[0] in ["$"]:
   b=eval(a[1:])*6.78
   print("&%.2f"%(b))
elif a[0] in ["&"]:
   c = eval(a[1:])/6.78
   print("$%.2f"%(c))
elif a[0:3] in ["RMB"]:
   x = eval(a[3:])/6.78
   print("USD%.2f"%(x))
elif a[0:3] in ["USD"]:
   y= eval(a[3:])*6.78
   print("RMB%.2f"%(y))
else:
   print("Error")
