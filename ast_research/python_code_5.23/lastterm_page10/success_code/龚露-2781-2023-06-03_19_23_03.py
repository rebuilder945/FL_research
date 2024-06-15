a=input()
if len(a)!=18:
    print('Error')
else:
    if a[-1] != 'X':
        c=list(map(int,a))
        d=sum(c)-c[-1]
        n=d%11
        m=(12-n)%11
        if m==c[-1]:
            print('Correct')
        else:
            print('Wrong')
    else:
        c=list(map(int,a[:-1]))
        d=sum(c)
        n=d%11
        m=(12-n)%11
        if m=="X":
            print('Correct')
        else:
            print('Wrong')

