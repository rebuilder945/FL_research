n = eval(input())
sum = 0
a = 2
b = 1
for x in range(n):
    sum += (a/b)
    a = a + b
    b = a - b
print('%.4f'%sum)
