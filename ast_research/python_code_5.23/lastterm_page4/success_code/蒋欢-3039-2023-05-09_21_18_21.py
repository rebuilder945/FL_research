def deTip(n):
    a=max(n)
    b=min(n)
    for x in n:
        if x==a or x==b:
            n.remove(x)
        else:
            continue
    print(n)
    print(a,b)
n=eval(input())
deTip(n)
