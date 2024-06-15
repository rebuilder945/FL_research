n,m=map(int,input().split())
a=m-n
if a<3:
    print("illegal input")
elif n==0:
    for x in range(1,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and y!=z and x!=z:
                    b=100*x+10*y+z 
                    print(b,end=' ')
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and y!=z and x!=z:
                    b=100*x+10*y+z 
                    print(b,end=' ')
