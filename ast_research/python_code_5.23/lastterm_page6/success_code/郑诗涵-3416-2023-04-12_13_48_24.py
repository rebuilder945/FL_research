money = input()
if money[0] in ['$']:
    C = (eval(money[1:])) * 6.78
    print("&%.2f" % (C))
elif money[0] in ['&']:
    F = eval(money[1:]) / 6.78
    print("$%.2f" % (F))
elif money[0] in ['R']:
    C1 = (eval(money[3:])) / 6.78
    print("USD%.2f" % (C1))
elif money[0] in ['U']:
    F2 = eval(money[3:]) * 6.78
    print("RMB%.2f" % (F2))
else:
    print("Error")
