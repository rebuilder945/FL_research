n = int(input())
sum = 0
a = 2
b = 1
for i in range(n):
    sum += a/b
    b,a = a,a+b
print("{:.4f}".format(sum))
