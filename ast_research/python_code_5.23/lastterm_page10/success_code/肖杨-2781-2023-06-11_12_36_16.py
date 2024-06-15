a=list(input())
if len(a)!=18:
    print('Error')
else:
    b=0
    c=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for i in range(17):
        b+=eval(a[i])*c[i]
    d=b%11
    e=[0,1,2,3,4,5,6,7,8,9,10]
    f=[1,0,'X',9,8,7,6,5,4,3,2]
    for i in range(11):
        if d==e[i]:
            g=f[i]
    if a[-1]==str(g):
        print('Correct')
    else:
        print('Wrong')


