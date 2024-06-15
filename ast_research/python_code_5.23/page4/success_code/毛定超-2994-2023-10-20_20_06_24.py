a1=input().split(",")
n,m=eval(input())
if n>len(a1):
    print("error")
else:
    for i in range(m):
        a1.append(a1[n])
    print(a1)

