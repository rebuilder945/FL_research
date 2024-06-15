def shulie(n):
    a=2
    b=1
    c=0
    while n>0:
        d=a/b
        c+=d
        n-=1
        e=b
        b=a
        a=a+e
        
    print("{:.4f}".format(c))
n=eval(input())
shulie(n)


