a=eval(input())
e=0
if a>=153:
    for i in range(153,a+1):
        f=i
        while i>0:
            b=i%10
            e+=(b**3)
            i=i//10
        if e==f:
            print(f)
elif a<153:
    print('none')

