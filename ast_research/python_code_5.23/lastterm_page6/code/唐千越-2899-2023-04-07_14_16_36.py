n,m=map(eval,input().split())
lst = []
if n<=m-3 and m<11 and n>=0:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and b !=c and c != a:
                   s=100*a+10*b+c
                    if s>99:
                        lst.append(s)
    print(*lst)                                 
else:
     print("illegal input")
    


