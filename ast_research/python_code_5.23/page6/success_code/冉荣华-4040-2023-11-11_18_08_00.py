a=input()
def r(x):return x/6.78
def m(x):return x*6.78
if a[0]=='$':
    b=m(float(a[1:]))
    print(f'&{b:.2f}')
elif a[0:3]=='USD':
    b=m(float(a[3:]))
    print(f'RMB{b:.2f}')
elif a[0]=='&':
    b=r(float(a[1:]))
    print(f'${b:.2f}')
elif a[0:3]=="RMB":
    b=r(float(a[3:]))
    print(f'USD{b:.2f}')
else:
    print('error')
