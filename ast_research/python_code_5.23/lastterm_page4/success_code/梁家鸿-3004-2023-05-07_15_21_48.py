a = eval(input())
for i in a:
    if i == 1:
        a.remove(1)
    elif i == 2:
        pass
    else:
        for y in range(2,i):
            if (i % y) == 0:
                a.remove(i)
        break
print(a)
