ls=input().split(",")
ls=list(ls)
n,m=input().split(",")
if n not in len(ls):
    print("error")
else:
    ls.append(ls[n]*m)
    print(ls)
