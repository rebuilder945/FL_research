su = []
for i in eval(input()):
    for j in range(2,i):
        if i % j == 0:
            break
        if i == 1:
            break
    else:
        su.append(i)
print(su)
