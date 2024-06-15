ls=input().split(",")
ls=list(ls)
n,m=input().split(",")
if n > len(ls) or n <= -len(ls):
    print("error")
else:
    ls.append(ls[n]*m)
    print(ls)
