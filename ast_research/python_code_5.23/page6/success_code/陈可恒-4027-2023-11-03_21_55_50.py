a = input()
b = 0
c = 0
while a:
    if a == '#':
        break
    b = b+int(a)
    c = c+1
    a = input()
print(c,b,end='')
