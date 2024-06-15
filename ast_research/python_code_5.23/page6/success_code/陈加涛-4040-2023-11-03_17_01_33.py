money = input()
if money[0:1] in ["$"]:
    rmb=eval(money[1:])*6.78
    print("&""%.2f"%(rmb))
elif money[0:1] in ["&"]:
    usd=eval(money[1:])/6.78
    print("$""%.2f"%(usd))
elif money[0:3] in["USD"]:
    RMB=eval(money[3:])*6.78
    print("RMB""%.2f"%(RMB))
elif money[0:3] in["RMB"]:
    USD=eval(money[3:])/6.78
    print("USD""%.2f"%(USD))
else:
    print("Error")


