s = input().strip()
e, s_, d, o = 0, 0, 0, 0
for ch in s:
    if ch.isalpha():
        e += 1
    elif ch== ' ':
        s_ += 1
    elif ch.isdigit():
        d += 1
    else:
        o += 1
print(e, s_, d, o)

