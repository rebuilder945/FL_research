a=eval(input())
b=range(1,11)
c=range(11,19)
d=range(19,29)
e=range(29,37)
f=0
if a<=0 or a>36:
    print('error')
else:
    if a in b:
        if a%2==0:
            print('black')
        else:
            print('red')
    if a in c:
        if a%2==0:
            print('black')
        else:
            print('red')
    if a in d:
        if a%2==0:
            print('black')
        else:
            print('red')
    if a in e:
        if a%2==0:
            print('black')
        else:
            print('red')
    if a==0:
        print('green')
