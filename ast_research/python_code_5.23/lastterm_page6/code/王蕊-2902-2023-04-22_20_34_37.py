x=2
y=1
n=eval(input())
i=0
whil n>0:
    s+=x/y
    m=x
    x=y
    x+=m
    n-=1
print("%.4f"%s)

