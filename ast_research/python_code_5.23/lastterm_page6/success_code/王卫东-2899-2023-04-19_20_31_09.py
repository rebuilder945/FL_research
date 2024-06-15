n,m=map(int,input().split())
a=[]
if m-n>2:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                 while x!=y and x!=z and y!=z:
                    s=x*100+y*10+z
                    if s>=100:
                       a.append(s) 
    print(a)
else:
    print("illegal input")                        

