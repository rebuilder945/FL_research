n,m=map(int,input().split())
if  m<0 or n <0 or (m-n)!=3 or type(m)!=type(1) or type(n)!=type(1) :
    print("illegal input")
else:
    if n==0:
        print(" ".join([str(x)+str(y)+str(z) for x in range(1,m) for y in range(m) for z in range(m) if x!=y and x!=z and y!=z]))
    else:
        print(" ".join([str(x)+str(y)+str(z) for x in range(n,m) for y in range(n,m) for z in range(n,m) if x!=y and x!=z and y!=z]))
    


