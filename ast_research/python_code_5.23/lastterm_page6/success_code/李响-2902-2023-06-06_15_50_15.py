n = int(input())
a = 1
b = 2
s = 0 
for i in range(n):
    s = b/a + s
    b = b + a
    a = b - a
print('{:.4f}'.format(s))



