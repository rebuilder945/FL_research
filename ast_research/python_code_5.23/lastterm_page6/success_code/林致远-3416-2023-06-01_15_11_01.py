Currency=input()
if Currency[0] in ['R','r']:
    m=eval(Currency[3:])/6.78
    print('USD%.2f' % m)
elif Currency[0] in ['U','u']:
    m=6.78*eval(Currency[3:])
    print('RMB%.2f' % m)
elif Currency[0] == '&':
    m=eval(Currency[1:])/6.78
    print('$%.2f' % m)
elif Currency[0] == '$':
    m=6.78*eval(Currency[1:])
    print('&%.2f' % m)
else :
    print("Error")
