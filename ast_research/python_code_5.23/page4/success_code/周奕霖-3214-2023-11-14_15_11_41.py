a = eval(input())
b = a[:]
for x in range(len(b)):
    if a[x] == 0:
        del a[x]
c = a + [0]*(len(b)-len(a))
print(a)

