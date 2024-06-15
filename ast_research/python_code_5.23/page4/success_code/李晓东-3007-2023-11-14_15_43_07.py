list = eval(input())
n,m = map(int,input().split(","))
if n<=m and len(list)>m:
    for i in range(n,m):
        del list[i]
    print(list)
else:
    print("error")
