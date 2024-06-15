a = input()
b = []
for i in range(len(a)):
    b.append(eval(a[i]))
c = []
for i in b:
    j = (i+5)%10
    c.append(j)
c[0],c[1],c[-2],c[-1] = c[-1],c[-2],c[1],c[0]
for i in c:
    print(i,end="")
