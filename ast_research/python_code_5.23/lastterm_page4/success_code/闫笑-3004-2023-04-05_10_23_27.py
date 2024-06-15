su = []
for i in eval(input()):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        su.append(i)
for x in eval(su):
    if x == 1:
        su.remove(1)
    if x == 0:
        su.remove(0)          
print(su)
