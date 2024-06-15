a = eval(input())
a.sort()

b = 0
for i in range(len(a)):
    b = b+a[i]*10**i
print(b)
