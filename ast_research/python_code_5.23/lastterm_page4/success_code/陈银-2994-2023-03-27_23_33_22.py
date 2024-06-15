a=eval(input())
n,m=eval(input())
c=list(a)
e=len(c)
if n > 0:
    if n > e-1:
        print("error")
    else:
        d=[c[n]]*m
        f=c+d
        print(f)
else:
    if n < -e:
        print("error")
    else:
        d=[c[n]]*m
        f=c+d
        print(f)
        
    
