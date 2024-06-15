a = list(eval(input()))
print(a)
n,m = input().split(",")
if int(n)>len(a):
    print("error")
else:
    d = a[int(n)]
    for i in range(int(m)):
        a.append(d)
print(a)


