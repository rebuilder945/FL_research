n1 = eval(input())
n2 = []
n3 = []
for x in n1:
    for y in range(2,x):
        if x !=1 and x % y ==0:
            n2.append(x)
for z in n1:
    if z not in n2 and z !=0 or 1:
        n3.append(z)
print(n3)
