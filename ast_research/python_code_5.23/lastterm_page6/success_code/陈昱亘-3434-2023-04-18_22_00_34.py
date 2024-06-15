a=input()
b=input()
origin={'red','blue','yellow'}
if a!=b and {a,b}.issubset(origin):
    if {a,b}=={'red','blue'}:
        print('purple')
    elif {a,b}=={'red','yellow'}:
        print('orange')
    else: print('green')
else: print('error')
