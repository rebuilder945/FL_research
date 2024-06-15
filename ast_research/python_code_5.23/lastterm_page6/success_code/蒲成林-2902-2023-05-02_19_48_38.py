n = int(input())
a, b = 2, 1
sum = 0
for i in range(n):
    sum += a / b
    a, b = a + b, a
print(f'{sum:.4f}')
