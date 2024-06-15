def generate_arithmetic_sequence(n, m, l):
    sequence = [n + i * l for i in range(m)]
    return sequence

input_str = input()
n, m, l = map(int, input_str.split(','))
result = generate_arithmetic_sequence(n, m, l)
print(result)

