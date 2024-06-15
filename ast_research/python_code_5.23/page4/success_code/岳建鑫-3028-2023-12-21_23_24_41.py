def solution(n, m, l):
    sequence = [n + i * l for i in range(m)]
    return sequence
n, m, l = map(int, input().split(','))

result = solution(n, m, l)
print(result)

