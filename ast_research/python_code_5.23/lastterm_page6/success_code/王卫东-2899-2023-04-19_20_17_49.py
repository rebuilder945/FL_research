n,m=map(int,input().split())
if n-m>2:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                 while x!=y or x!=z or y!=z:
                    s=x*100+y*10+z
                    if s>=100:
                        print(s,end=" ")
else:
    print("illegal input")                        

