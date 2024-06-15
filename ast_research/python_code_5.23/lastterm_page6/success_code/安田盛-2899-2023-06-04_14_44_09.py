n,m=map(int,input().split())
d=[]
if 0<=n<m<=10 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                s=a*100+b*10+c
                if a!=b and b!=c and a!=c and s>99:
                    d.append(s)
                    print(s,end=" ")
elif d==[]:
    print("illegal input")
else :
    print("illegal input")

    





