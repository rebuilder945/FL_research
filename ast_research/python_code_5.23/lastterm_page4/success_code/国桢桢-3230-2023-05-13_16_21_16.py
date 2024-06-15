l = eval(input())
l.reverse()
b = len(l)
for i in range(b):
    a = a + (l[i]*10**(b-1))
    b = b-1
print(a)
