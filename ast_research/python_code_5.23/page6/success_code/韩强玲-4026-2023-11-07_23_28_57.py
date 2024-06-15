n = eval(input())
a = 2
b = 1
c = 0
for i in range(n):
    c+=a/b
    a,b=a+b,a
print('%.4f'%c)
