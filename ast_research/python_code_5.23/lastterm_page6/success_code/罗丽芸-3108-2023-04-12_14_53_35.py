a=eval(input())
b=""
for i in range(len(a)):
    b += a[i]
c=list(b)
d=["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(d)):
    if c.count(d[i])!=0:
        print("%s,%d"%(d[i],c.count(d[i])))
    else:
        pass


