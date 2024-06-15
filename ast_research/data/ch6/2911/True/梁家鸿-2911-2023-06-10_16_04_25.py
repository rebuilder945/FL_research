a = input()
a = a[::-1]
b = ''
for x in a:
    x = str((int(x) + 5)%10)
    b += x
print(b)
