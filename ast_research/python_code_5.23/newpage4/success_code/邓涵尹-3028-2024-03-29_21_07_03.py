def ps(n, m, l):
    ssr = [n]
    for _ in range(1, m):
        ssr.append(ssr[-1] + l)
    return ssr

n, m, l = map(int, input().split(','))
print(ps(n, m, l))
