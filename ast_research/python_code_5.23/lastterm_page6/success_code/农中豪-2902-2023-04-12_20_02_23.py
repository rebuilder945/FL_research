n=int(input())
a=2
b=1
c=0
for i in range(n):
    c+=a/b
    a=a+b
    b=a-b
print('%.4f'%c)
