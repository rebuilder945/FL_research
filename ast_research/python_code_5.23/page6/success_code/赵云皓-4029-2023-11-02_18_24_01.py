a=input().split()
a=list(map(int,a))
c=[]
if a[1]>a[0]+2 and a[0]>-1 and a[1]<10:
    for x in range(a[0],a[1]):
        for i in range(a[0],a[1]):
            for y in range(a[0],a[1]):
                if x!=i and x!=y and y!=i and x!=0:
                    d=x*100+i*10+y
                    c.append(d)
                else:
                    c=c
    c=list(map(str,c))
    print(" ".join(c))
else:
    print("illegal input")                



