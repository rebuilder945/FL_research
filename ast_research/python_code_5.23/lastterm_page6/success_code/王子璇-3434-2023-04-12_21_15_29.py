c1=input()
c2=input()
if c1 in ['red','blue','yellow'] and c2 in ['red','blue','yellow'] and c1!=c2:
    if c1 in ['red','blue']and c2 in ['red','blue']:
        print("purple")
    elif c1 in ['red','yellow']and c2 in['red','yellow']:
        print('orange')
    else:
        print('green')
else:
    print('error')



