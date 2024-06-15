def generate_arithmetic_sequence(n, m, l):
    return [n + i * l for i in range(m)]

n, m, l = map(int, input().split(','))

result = generate_arithmetic_sequence(n, m, l)

print(result)
