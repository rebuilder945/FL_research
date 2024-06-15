money = input()
if money[0] == '$':
    A1 = eval(money[1:])
    q = A1 * 6.78
    print("&%.2f"%(q))
elif money[0] =='&':
    A2 = eval(money[1:])
    m = A2 / 6.78
    print("$%.2f"%(m))
elif money[0:3] =='RMB':
    A3 = eval(money[3:])
    v = A3 / 6.78
    print("USD%.2f"%(v))
elif money[0:3] =='USD':
    A4 = eval(money[3:])
    k = A4 * 6.78
    print("RMB%.2f"%(k)) 
else:
    print("Error")

