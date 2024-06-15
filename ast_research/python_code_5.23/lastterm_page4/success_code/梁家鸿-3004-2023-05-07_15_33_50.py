a = eval(input())
for i in a:
    if i == 1:
        a.remove(1)
    elif i == 2:
        continue
    else:
        for j in range(2,i):
            if (i % j) == 0:
                a.remove(i)
                break
            else:
                continue
print(a)
