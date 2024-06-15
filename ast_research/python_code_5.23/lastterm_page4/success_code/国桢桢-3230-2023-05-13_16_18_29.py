l = eval(input())
l.reverse()
a = 0
b = len(l)
for i in range(len(l)):
    a = a + (l[i]*10**(b))
    b = b-1
print(a)
