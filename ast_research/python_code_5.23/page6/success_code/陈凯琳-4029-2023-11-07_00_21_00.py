n,m=input().split(" ")
n=int(n)
m=int(m)
if m-n<3 or n>=8 or n<0 or m<0 or m<n:
    print("illegal input")
else:
    for i in range(n,m):
        for a in range(n,m):
            for b in range(n,m):
                if i!=a and i!=b and i !=0 and b!=a:
                    s=i*100+a*10+b*1
                    print(s,end=' ')




