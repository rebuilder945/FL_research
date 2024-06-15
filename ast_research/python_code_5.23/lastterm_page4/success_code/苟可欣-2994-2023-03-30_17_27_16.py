ls=list(map(int,input().split(",")))
n,m=eval(input())
ls1=ls.copy()
if n < len(ls)+2:
    for x in range(m):
        ls1.append(ls[n])
    print(ls1)
else:
    print("error")

