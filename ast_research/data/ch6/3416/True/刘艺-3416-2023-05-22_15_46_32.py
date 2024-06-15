money = input()
if money[0] in ['$']:
    a = eval(money[1:])*6.78
    print("&%.2f"%(a))
elif money[0] == 'U':
    b = eval(money[3:])*6.78
    print("RMB%.2f"%(b))
elif money[0] == '&':
    c = eval(money[1:])/6.78
    print("$%.2f"%(c))
elif money[0] == 'R':
    d = eval(money[3:])/6.78
    print("USD%.2f"%(d))
else:
    print("Error")
