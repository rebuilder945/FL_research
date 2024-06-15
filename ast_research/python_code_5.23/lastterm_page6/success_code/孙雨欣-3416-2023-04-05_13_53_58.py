money=input()
if money[:1] in ["&"]:
    b=float(money[1:])/6.78
    print("$%.2f"%b)
elif money[:3] in ['RMB']:
    b=eval(money[3:])/6.78
    print("USD%.2f"%b)
elif money[:1] in ['$']:
    b=eval(money[1:])*6.78
    print("&%.2f"%b)
elif money[:3] in ['USD']:
    b=eval(money[3:])*6.78
    print("RMB%.2f"%b)
else:
    print("Error")

