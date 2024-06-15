money = input()

if money[0] in ['$']:

    r = (eval(money[1:]) )*6.78

    print("&%.2f"%r)

elif money[0] in ['U']:

    r = (eval(money[3:]) )*6.78

    print("RMB%.2f"%r)
elif money[0] in ['&']:
    r=(eval(money[1:]))/6.78
    print("$%.2f"%r)
elif money[0] in ['R']：
    r=(eval(money[3:]))/6.78
    print("USD%.2f"%r)
else:

    print("Error")
