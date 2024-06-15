lst = eval(input())
a = []
for i in lst:
    if i == 2:
        a.append(i)
    else:
        for x in range(2,i):
            if i % x == 0:
                break
            elif i not in a:
                a.append(i)
print(a)

