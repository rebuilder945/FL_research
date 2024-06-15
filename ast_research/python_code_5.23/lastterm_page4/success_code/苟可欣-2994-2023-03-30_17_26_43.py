ls=list(map(int,input().split(",")))
n,m=eval(input())
if n < len(ls)+2:
    for x in range(m):
        ls.append(ls[n])
    print(ls)
else:
    print("error")

