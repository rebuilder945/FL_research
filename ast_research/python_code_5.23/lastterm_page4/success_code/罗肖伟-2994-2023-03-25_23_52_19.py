ls=list(eval(input()))
n,m=map(eval,input().split(","))
if 0<=n<=len(ls)-1:
    for i in range(m):
        ls.append(ls[n])
    print(ls)
if n<0 and 1<=-n<=len(ls):
    for i in range(m):
        ls.append(ls[n])
else:
    print("error")
