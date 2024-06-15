money = input()
if money[0] in['$']:
    C = (eval(money[1:len(money)+1]))*6.78
    print("&%.2f"%(C))
elif money[0] in['U']:
    C = (eval(money[3:len(money)+1]))*6.78
    print("RMB%.2f"%(C))
elif money[0] in['&']:
    M = (eval(money[1:len(money)+1]))/6.78
    print("$%.2f"%(M))
elif money[0] in['R']:
    M = (eval(money[3:len(money)+1]))/6.78
    print("USD%.2f"%(M))
else:
    print("Error")
