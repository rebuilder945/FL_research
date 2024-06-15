a=list(input())
if len(a)!=18:
    print('Error')
else:
    b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    c=['1','0','x','9','8','7','6','5','4','3','2']
    s=0
    for i in range(len(b)):
        s+=int(a[i])*b[i]
    d=s%11
    if c[d]==a[-1]:
        print('Correct')
    elif d==2:
        if a[-1]==10:
            print('Correct')
        else:
            print('Wrong')
    else:
        print('Wrong')


