a = input().split(',')
b = []
for i in a :
    if i == 1 or i == 2:
        b.append(i)
    else:
        for j in range(2,eval(i)):
            if eval(i)%j == 0:
                pass
        else:
            b.append(i)
print(b)


