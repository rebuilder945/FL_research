a=input()
if  a[:1]in['$']:
   b=eval(a[1:])*6.78
   print("&%.2f"%(b))
elif a[0:3]in['USD']:
    c=eval(a[3:])*6.78
    print("RMB%.2f"%(c))
elif a[:1]in['&']:
    d=eval(a[1:])/6.78
    print("$%.2f"%(d))
elif a[0:3]in['RMB']:
    e=eval(a[3:])/6.78
    print("USD%.2f"%(e))
else:
     print("Error")


