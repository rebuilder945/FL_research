money = input()
if money[0] == '$':
    s = eval(money[1:])*6.78
    print("&%.2f"%s)
elif money[0] == '&':
    s = eval(money[1:])/6.78
    print("$%.2f"%s)
elif money[:3] == 'RMB':
    s = eval(money[3:])/6.78
    print("USD%.2f"%s)
elif money[:3] == 'USD':
    s = eval(money[3:])/6.78
    print("RMB%.2f"%s)
else:
    print("Error")
