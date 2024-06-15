money = input ()
if money[0] in ['&']:
    a = float(money[1:] )/ 6.78
    print("$%.2f"%a)
elif money[0] in ['$']:
    a = float(money[1:]) * 6.78
    print("&%.2f"%a)
elif money[0:3] in ['USD']:
    a = float(money[3:]) * 6.78
    print("RMB%.2f"%a)
elif money[0:3] in ['RMB']:
    a = float(money[3:]) / 6.78
    print("USD%.2f"%a)
else :
    print("Error")
