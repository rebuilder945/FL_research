money=input()
if money[0:1] in["$"]:
    rmb=eval(money[1:])*6.78
    print("&{:.2f".format(rmb))
elif money[0:1]in["&"]:
    usd=eval(money[1:])/6.78
elif money[0:3]in["RMB"]:
    rmb=eval(money[3:])/6.78
elif money[0:3]in["USD"]:
    usd=eval(money[3:])*6.78
    print("RMB{:.2f}".format(usd))
else:
    print("Error")
