n = int(input())
sum = 0
a, b = 2, 1
for i in range(n):
    sum += a / b
    a, b = a + b, a
print("%.4f" % sum)

