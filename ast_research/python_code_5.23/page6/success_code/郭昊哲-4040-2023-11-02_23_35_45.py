money=input()
if money[0] in ['$']:
    C=(eval(money[1:]))*6.78
    print("&%.2f"%(C))
elif money[0] in ['&']:
    C=(eval(money[1:]))/6.78
    print("$%.2f"%(C))
elif money[0] in ['R']:
    C=(eval(money[3:]))/6.78
    print("USD%.2f"%(C))
elif money[0] in ['U']:
    C=(eval(money[3:]))*6.78
    print("RMB%.2f"%(C))
else:
    print("Error")



