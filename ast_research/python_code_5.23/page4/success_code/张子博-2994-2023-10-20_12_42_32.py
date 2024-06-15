i=input().split(",")
v=list(map(int,i))
n,m=eval(input())
if n>len(i):
    print("error")
else:
    k=v[n]
    for l in range(m):
        v.append(k)
    print(v)

