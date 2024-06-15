d = {}
while True:
    s = input()
    if s == 'q':
        break
    d[s] = d.get(s, 0) + 1

m = max(d.values())
for x, y in d.items():
    if y == m:
        print(x, y)
        break

