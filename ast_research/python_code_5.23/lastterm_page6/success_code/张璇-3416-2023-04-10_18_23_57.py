money =input()
if money[:1]in['&']:
    a = eval(money[1:])/6.78
    print("$%.2f"%(a))
elif money[:3]in['RMB']:
    c = eval(money[3:])/6.78
    print("USD%.2f"%(c))
elif money[:1]in['$']:
    b = eval(money[1:])*6.78
    print("&%.2f"%(b))
elif money[:3]in['USD']:
    d = eval(money[3:])*6.78
    print("RMB%.2f"%(d))
else:
    print("Error")

