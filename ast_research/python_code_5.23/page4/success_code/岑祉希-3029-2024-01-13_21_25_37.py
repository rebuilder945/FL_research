money = input()
if money[0]=='$':
    result = (eval(money[1:])) * 6.78
    print("&%.2f" % (result))
elif money[0] == '&':
    result = (eval(money[1:])) / 6.78
    print("$%.2f" % (result))
elif money[0:3] in ["USD"]:
    result = (eval(money[3:])) * 6.78
    print("RMB%.2f" % (result))
elif money[0:3] in ["RMB"]:
    result = (eval(money[3:])) / 6.78
    print("USD%.2f" % (result))
else:
    print("Error")

