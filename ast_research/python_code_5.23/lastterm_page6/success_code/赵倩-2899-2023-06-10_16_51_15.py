a=input().split()
n,m=map(int,a)
l=[i for i in range(n,m)]
c=[]
if len(l)<3:
    print("illegal input")
else:
    for x in l:
        for y in l:
            for n in l:
                if x!=y and x!=n and n!=y:
                    s=x*100+y*10+n
                    if s>99:
                        c.append(s)
    print(*c)




















