a = input()
b = []
for i in range(len(a)):
    b.append(eval(a[i]))
c = []
for i in b:
    j = (i+5)%10
    c.append(j)
d = c.copy()
d[0] = c[-1]
d[-1] = c[0]
d[1] = c[-2]
d[-2] = c[1]
for i in d:
    print(i,end="")
