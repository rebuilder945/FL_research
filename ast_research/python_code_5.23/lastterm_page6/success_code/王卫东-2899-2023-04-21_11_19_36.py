n,m=map(int,input().split())
a=[]
b=[]
if m-n>2:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    s=x*100+y*10+z
                    a.append(s)
    for x in a:
        if x>100:
            b.append(x)
    print(" ".join(map(str,b)))

else:
    print("illegal input")                        

