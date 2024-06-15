n,m=map(eval,input().split())
lst = []
num = []
if n<=m-3 and m<11 and n>=0:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and b !=c and c != a:
                    lst.append(a)
                    lst.append(b)
                    lst.append(c)
                    lst1=str(lst)
                    lst2=int(lst1)
                    if lst2>99:
                        num.append(lst2)
    print(*num)                                 
else:
     print("illegal input")
    


