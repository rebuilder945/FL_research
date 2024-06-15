money=input()
if money[0]=='#':
    RMB=6.78*float(money[1:])
    print("&%.2f"%RMB)
elif money[0]=='&':
    dollar=float(money[1:])/6.78
    print("$%.2f"%dollar)
elif money[:3]=='RMB':
    dollar=float(money[3:])/6.78
    print("USD%.2f"%dollar)
elif money[:3]=='USD':
    RMB=6.78*float(money[3:])
    print("RMB%.2f"%RMB)
else:
    print('Error')

