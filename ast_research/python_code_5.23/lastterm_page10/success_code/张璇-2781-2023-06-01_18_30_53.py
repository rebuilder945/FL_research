a=list(input())
b=len(a)
if b!=18:
    print('Error')
else:
    c=['7','9','10','5','8','4','2','1','6','3','7','9','10','5','8','4','2']
    d=0
    for x in range(b-1):
        b=b+int(a[x])*int(c[x])
    n=b%11
    m=(12-n)%11
    if n==2 and m==10:
        m="X"
        if str(m)==a[17]:
            print('Correct')
        else:
            print('Wrong')
    elif n!=2:
        m=m
        if str(m)==a[17]:
            print('Correct')
        else:
            print('Wrong')


