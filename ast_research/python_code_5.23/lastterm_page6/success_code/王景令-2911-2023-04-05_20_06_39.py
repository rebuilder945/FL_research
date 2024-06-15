a = input()
c = ''
for i in a:
    b = str((int(i) + 5) % 10)
    c += b
d = c[::-1]
print(d)


