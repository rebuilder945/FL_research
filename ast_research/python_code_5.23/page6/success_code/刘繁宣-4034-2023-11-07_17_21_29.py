a=input()
b=input()
if a==b or not a in ['red','blue','yellow'] or not b in ['red','blue','yellow'] :
    print('error')
else:
    if a[0] in ['r'] or b[0] in ['r']:
        if b[0] in ['y'] or a[0] in ['y']:
            print('orange')
        if b[0] in ['b'] or a[0] in ['b']:
            print('purple')
    else:
        print('green')
