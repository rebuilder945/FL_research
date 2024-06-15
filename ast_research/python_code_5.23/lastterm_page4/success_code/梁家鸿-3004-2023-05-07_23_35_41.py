a = eval(input())
b = []
for i in a:
    if i == 1:
        continue
    elif i == 0:
        continue
    elif i == 2:
        b.append(i)
    else:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            b.append(i)
print(b)
