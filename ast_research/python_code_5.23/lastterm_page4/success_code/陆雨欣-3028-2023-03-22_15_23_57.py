n, m, l = map(int, input().split(','))
array = [n]
for i in range(m - l):
    n = n + l
    array.append(n)
print(array)
