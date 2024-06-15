a = input()
if a[0] == '$':
    a=eval(a[1:])*6.78
    print("&%.2f"%a)
elif a[0:3] =="USD":
    a = eval(a[3:])*6.78
    print("RMB%.2f"%a)
elif a[0] =='&':
    a = eval(a[1:])/6.78
    print("$%.2f"%a)
elif a[0:3] =='RMB':
    a = eval(a[3:]) / 6.78
    print("USD%.2f"%a)
else:
    print('Error')

