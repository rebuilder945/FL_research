a = eval(input())
b = a[:]
for x in a:
    if x == 0:
        del x
c = a + [0]*(len(b)-len(a))
print(c)

