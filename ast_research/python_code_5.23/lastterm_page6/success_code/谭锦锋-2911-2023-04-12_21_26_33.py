a = input()
c = []
for x in range(len(a)):
    c.append(a[x])
    for x in range(len(a)):
        x = (x+5)%10
c.reverse()
for i in range(len(c)):
    print(c[i], end='')
