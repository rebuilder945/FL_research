a = eval(input())
b = []
for i in a:
    for j in range(2,i):
        if i%j == 0:
            pass
        else:
            b.append(i)
print(b)


