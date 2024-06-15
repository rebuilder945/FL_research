n = int(input())
a = [2,3]
b = [1,2]
sum = 0.0
for i in range(n):
    sum += a[i]/b[i]
    a.append(a[i]+a[i+1])
    b.append(b[i]+b[i+1])
print("%.4f"%(sum))
