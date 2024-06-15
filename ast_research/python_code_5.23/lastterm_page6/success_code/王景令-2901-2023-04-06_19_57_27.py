
n = 0
m = []
a = 0
while a != '#':
    b = input()
    if b == '#' :
        break
    else:
        n += 1
        m.append(int(b))
print(n,sum(m),sep = ' ')
