a = eval(input())
b = []
for x in range(len(a)):
    for s in range(2,a[x]):
        if a[x]%s!=0:
            b.append(a[x])
            break
if 2 in a:
    b.insert(0,2)
print(b)

