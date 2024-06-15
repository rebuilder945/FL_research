a = input()
c = []
for i in range (len(a)):
    c.append(int(a[i]))
for n in range(len(c)):
    c[n] = (c[n]+5)%10
c.reverse()
for m in range(len(c)):
    print(c[m],end='')
