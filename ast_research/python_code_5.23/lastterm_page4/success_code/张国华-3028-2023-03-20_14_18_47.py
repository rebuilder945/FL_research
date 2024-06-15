n, m, l = map(int, input().split(","))
seq = [n + i * l for i in range(m)]
print(seq)
