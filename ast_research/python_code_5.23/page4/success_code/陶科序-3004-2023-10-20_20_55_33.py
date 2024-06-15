a = input().split(',')
b = []
for i in a :
    if i == 1 or 2:
        b.append(i)
    else:
        for j in range(2,i):
            if i%j == 0:
                pass
        else:
            b.append(i)
print(b)


