a = eval(input())
b = [x for x in range(1,a+1)]
c = []+[0]*a
for x in range(a):
    c[x-1]=b[x]
print(c)
