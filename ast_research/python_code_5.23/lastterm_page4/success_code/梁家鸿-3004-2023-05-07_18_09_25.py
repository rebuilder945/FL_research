a = eval(input())
for i in a:
    if i == 1:
        a.remove(i)
    elif i == 0:
        a.remove(i)
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
