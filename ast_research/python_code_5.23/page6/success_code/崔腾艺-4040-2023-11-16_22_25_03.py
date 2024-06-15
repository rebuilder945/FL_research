a=input()
def r(x): return x/6.78
def m(x): return x*6.78
if a[0]=='$':
    b=m(float(a[1:]))
    print('&%.2f'%b)
elif a[:3]=='USD':
    b=m(float(a[3:]))
    print('RMB%.2f'%b)
elif a[0]=='&':
    b=r(float(a[1:]))
    print('$%.2f'%b)
elif a[:3]=='RMB':
    b=m(float(a[3:]))
    print('USD%.2f'%b)
else:
    print('Error')
