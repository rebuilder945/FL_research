n,m=map(int,input().split())
e=[]
if 0<=n<m<11 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    d=a*100+b*10+c
                    if d>99:
                        e.append(d)
    if e==[]:
        print("illegal input")
    else:
        print(e)    

else:
    print("illegal input")



