Ist=eval(input())
a=list(eval(input()))
b=[x for x in range(a[0],a[1])]
for j in b:
    Ist.pop(j)
print(Ist)
