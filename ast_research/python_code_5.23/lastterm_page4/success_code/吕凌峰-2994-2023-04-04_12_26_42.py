lst1 = list(map(eval,input().split(",")))
n,m = map(eval,input().split(","))
if n >= len(lst1):
    print("error")
else:
    x = lst1[n]
    for i in range(m):
        lst1.append(x)
    print(lst1)
