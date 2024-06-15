a = input().split(",")
n,m = input().split(",")
d = int(a[n])
if int(n)>len(a):
    print("error")
else:
    for i in range(int(m)):
        a.append(d)
print(a)


