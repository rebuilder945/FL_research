def um(s):
    if s>1:
        for i in range(2,s):
            if s%i==0:
                return 0
    return 1

def hui(s):
    num=str(s)
    s=num[::-1]
    if s==num:
        return s

n=float(input())
if n-int(n)>0 or int(n)<1:
    print("illegal input")
else:
    n=int(n)
    xss=[]
    s=2
    for x in range(2,n):
        if um(x) and hui(x):
            xss.append(x)
    for x in range(len(xss)):
        print("%d"%xss[x],end=' ')

