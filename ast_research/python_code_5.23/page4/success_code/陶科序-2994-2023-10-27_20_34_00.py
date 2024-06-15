a = input().split(",")
n,m = input().split(",")
if int(n)>len(a):
    print("error")
else:
    for i in range(m):
        a.append(a[n])
print(a)


