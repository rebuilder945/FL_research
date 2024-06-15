su = []
for i in eval(input()):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        su.append(i)
su.remove(1)
print(su)
