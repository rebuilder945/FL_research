n, m, l = input().split(',')
n, m, l = int(n), int(m), int(l)
lst = [n + i*l for i in range(m)]
print(lst)
