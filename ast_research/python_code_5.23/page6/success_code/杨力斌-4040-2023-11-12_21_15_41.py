money1 = input()
if money1[0] in ["$"]:
    money2=eval(money1[1:5])*6.78
    print("&%.2f"%money2)
elif money1[0:3] in ["USD"]:
    money2=eval(money1[3:8])*6.78
    print("RMB%.2f"%money2)
elif money1[0] in ["&"]:
    money2=eval(money1[1:5])/6.78
    print("$%.2f"%money2)
elif money1[0:3] in ["RMB"]:
    money2=eval(money1[3:8])/6.78
    print("USD%.2f"%money2)
else :
    print("Error")

