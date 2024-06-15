n, m, l = map(int, input().strip().split(','))

lst = [n + i * l for i in range(m)]

print(lst)

