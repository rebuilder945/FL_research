money_str=input()
if money_str[0] in ['&']:
    m=(eval(money_str[1:]))/6.78
    print("$%.2f"%m)
elif money_str[0] in ['$']:
    m=(eval(money_str[1:]))*6.78
    print("&%.2f"%m)
elif money_str[0:3] in ['USD']:
    m=(eval(money_str[3:]))*6.78
    print("RMB%.2f"%m)
elif money_str[0:3] in ['RMB']:
    m=(eval(money_str[3:]))/6.78
    print("USD%.2f"%m)
else:
    print("Error")


