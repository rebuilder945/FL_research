a = input()
c = []
for i in range(len(a)):
    c.append(int(a[i]))
for j in range(len(a)):
        c[j] = (c[j]+5)%10
c.reverse()
for k in range(len(c)):
    print(c[k], end='')
