


money=input()
if money[0]in['&']:
    C=float(money[1:5])/6.78
    print("$%.2f"%C)
elif money[0:3]in['RMB']:
    C=float(money[3:9])/6.78
    print("USD%.2f"%C)
elif money[0]in['$']:
    U=float(money[1:5])*6.78
    print("&%.2f"%U)
elif money[0:3]in['USD']:
    U=float(money[3:9])*6.78
    print("RMB%.2f"%U)
else:
    print("Error")    


