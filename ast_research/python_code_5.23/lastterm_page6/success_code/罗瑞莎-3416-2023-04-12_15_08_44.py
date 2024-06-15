money = input()
if money[0] == '$':
    s = eval(money[1:])*6.78
    print("&%.2f"%s)
elif money[0] == '&':
    s = eval(money[1:])/6.78
    print("$%.2f"%s)
elif money[:2] == 'RMB':
    s = eval(money[2:])/6.78
    print("USD%.2f"%s)
elif montey[:2] == 'USD':
    s = eval(money[2:])/6.78
    print("RMB%.2f"%s)
