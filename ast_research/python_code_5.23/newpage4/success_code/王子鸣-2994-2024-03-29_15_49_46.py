l1=list(map(int,input().split(",")))
n,m=list(map(int,input().split(",")))
if n>=len(l1):
    print("error")
else:
    for i in range(m):
        l1.append(l1[n])
    print(l1)
