a=list(map(int,input().split(",")))
n,m=eval(input())
if n>len(a)-1:
    print("error")
else:
    dick=a[n]
    for i in range(m):
        a.append(int(dick))
    print(a)
