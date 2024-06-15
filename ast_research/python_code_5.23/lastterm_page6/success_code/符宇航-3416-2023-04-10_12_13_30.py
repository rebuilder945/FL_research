money = input()
if money[0] in ['$']:
    rmb = (eval(money[1:]))*6.78
    print("&%.2f"%(rmb))
elif money[0] in ['U']:
    rmb = (eval(money[3:]))*6.78
    print("RMB%.2f"%(rmb))
elif money[0] in ['&']:
    mei = (eval(money[1:]))/6.78
    print("$%.2f"%(mei))
elif money[0] in ['R']:
    mei = (eval(money[3:]))/6.78
    print("USD%.2f"%(mei))
else:
    print("Error")



