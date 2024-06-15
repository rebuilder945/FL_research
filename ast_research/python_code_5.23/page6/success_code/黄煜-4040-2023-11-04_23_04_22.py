money=input()
if money[0:3]in['USD']:
    a=(eval(money[3:]))*6.78
    print("RMB%.2f"%(a))
elif money[0:3]in['RMB']:
    b=(eval(money[3:]))/6.78
    print("USD%.2f"%(b))
elif money[0]in['$']:
    c=(eval(money[1:]))*6.78
    print("&%.2f"%(c))
elif money[0]in['&']:
    d=(eval(money[1:]))/6.78
    print("$%.2f"%(d))
else:
    print("Error")

