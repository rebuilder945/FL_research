n, m, l = map(int, input().split(','))
arithmetic_sequence = [n + i * l for i in range(m)]
print(arithmetic_sequence)

