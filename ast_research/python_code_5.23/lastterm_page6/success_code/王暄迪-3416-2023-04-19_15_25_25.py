money=input()
if money[0]in['$']:
    RMB=(eval(money[1:]))*6.78
    print("&%.2f"%(RMB))
elif money[:3]in['USD']:
    RMB=(eval(money[3:]))*6.78
    print("RMB%.2f"%(RMB))
elif money[0]in['&']:
    USD=eval(money[1:])/6.78
    print("$%.2f"%(USD))
elif money[:3]in['RMB']:
    USD=eval(money[3:])/6.78
    print("USD%.2f"%(USD))
else:
    print("Error")
