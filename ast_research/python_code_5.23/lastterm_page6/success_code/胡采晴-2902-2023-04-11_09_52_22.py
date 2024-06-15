
a = 2
b = 1
sum = 0
n = int(input())
for i in range(n):
    sum = a / b + sum
    a, b = (a + b), a
print(sum)

