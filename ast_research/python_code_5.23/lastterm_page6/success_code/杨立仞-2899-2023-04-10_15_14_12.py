n,m=input().split()
n=int(n)
m=int(m)
if m-n<2 or m>=10 or n<0:
    print("illegal input")
else:
    for q in range(n,m):
        for w in range(n,m):
            for e in range(n,m):
                if q!=w!=e and q!=e:
                    a=int(str(q)+str(w)+str(e))
                    print(a,end=" ")
