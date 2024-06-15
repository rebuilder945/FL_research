money=input()
if money[:1] in ["&"]:
    mei=(eval(money[1:]))/6.78
    print("$%.2f"%(mei))
elif money[:1] in ["$"]:
    zhong=(eval(money[1:]))*6.78
    print("&%.2f"%(zhong))
elif money[:3] in ['RMB']:
    meea=(eval(money[3:]))/6.78
    print('USD%.2f'%(meea))
elif money[:3] in ['USD']:
    zhon=(eval(money[3:]))*6.78
    print('RMB%.2f'%(zhon))
else:
    print('Error')

