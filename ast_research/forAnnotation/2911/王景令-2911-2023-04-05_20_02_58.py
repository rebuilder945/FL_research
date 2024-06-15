a = input()
c = ''
for i in a:
    b = str((int(i) + 5) % 10)
    c += b
reversed(c)
d = c
print(int(d))

