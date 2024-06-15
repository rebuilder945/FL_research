n,m=input().split(" ")
n,m=int(n),int(m)
text=[]
if 0<n<m:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and i!=k and j!=k:
                    text.append(str(i)+str(j)+str(k))
    print(" ".join(x for x in text))
else:
    print("illegal input")
