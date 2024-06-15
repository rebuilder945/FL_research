a = eval(input())
y = []
for i in range(len(a)):
    k = 2
    while k <= a[i]-1:
        r = a[i] % k
        if r == 0:
            break
        else:
            k = k+1
    if k == a[i]:
        y.append(k)
print(y)
