su = [2,3]
for i in range(eval(input())):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        su.append(i)
print(su)
