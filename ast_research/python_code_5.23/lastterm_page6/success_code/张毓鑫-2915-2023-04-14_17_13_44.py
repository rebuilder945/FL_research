def shui(a,e,d):
        f=a
        if a>0:
            b=a%10
        e+=b**3
        a=a//10
        shui(a,e,d)
        if a==0 and e==d:
             print(e)
a=eval(input())
e=0
if a>=153:
     for i in range(153,a+1):
        k=shui(i,e,i)
elif a<153:
    print('none')

