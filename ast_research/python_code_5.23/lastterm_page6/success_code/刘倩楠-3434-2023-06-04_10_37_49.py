n,m=input().split()
n=int(n)
m=int(m)
if n>=m or (m-n)!=3 or n<0 or m<0 or n>8:
    print("illegal input")
else:
    ls=[x for x in range(n,m)]
    lt=[]
    for x in ls:
        for y in ls:
            for z in ls:
                if x!=y and x!=z and y!=z:
                    lt.append(str(x)+str(y)+str(z))
                else:
                    pass

    print("".join(str(x)) for x in lt)
