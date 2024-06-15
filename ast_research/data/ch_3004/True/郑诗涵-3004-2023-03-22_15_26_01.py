z = eval(input())
l = []
for i in z:
    if i >= 2:
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            l.append(i)
print(l)
