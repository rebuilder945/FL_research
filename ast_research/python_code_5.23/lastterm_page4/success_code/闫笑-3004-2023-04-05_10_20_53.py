su = []
for i in eval(input()):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        su.append(i)
if su[0] == 1:
    su.remove(1)
print(su)
