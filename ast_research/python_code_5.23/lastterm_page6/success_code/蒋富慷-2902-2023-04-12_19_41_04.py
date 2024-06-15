n = eval(input())
a = 1
b = 2
sums = 0
for i in range(n):
    c = b/a
    d = a
    a = b
    b = b + d
    sums += c
print('%.4f'%sums)
