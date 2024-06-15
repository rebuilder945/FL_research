a=list(input().split(" "))
b=list(input().split(" "))
n,m=eval(b[0]),eval(b[1])
c=a[n]
d=a[m]
if n>0:
    if m>0:
        a.remove(c)
        a.remove(d)
        a.insert(n,d)
        a.insert(m,c)
    else:
        a.remove(c)
        a.remove(d)
        a.insert(n,d)
        a.insert(m+1,c)
elif m> 0:
    if n>0:
         a.remove(c)
         a.remove(d)
         a.insert(n,d)
         a.insert(m,c)
    else:
        a.remove(c)
        a.remove(d)
        a.insert(n+1,d)
        a.insert(m,c)
print(a)
